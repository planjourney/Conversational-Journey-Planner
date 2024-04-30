#!/usr/bin/env python
# coding: utf-8

# In[5]:


import openai
from datetime import datetime, timedelta
import urllib.parse
import urllib.request
import json
import uuid
from openai import OpenAI
import streamlit as st
import requests

# API keys placeholders
OPENAI_API_KEY=" xxx"
TFL_API_KEY="xxx"
NOW = datetime.now() 
client = OpenAI(
        api_key = OPENAI_API_KEY)

class JourneyPlanner:
    def __init__(self):
        self.user_queries = []
        self.system_responses = []
        self.history = ''
        self.parameters = { 'source': None,
                            'destination': None,
                            'date': None,
                            'time': None 
                           }    
        self.tfl_api_request = ''
        self.tfl_api_response = ''
        self.ecode = 200
        
        
    def setparameters(self, source, destination, date, time):
        self.parameters['source'] = source
        self.parameters['destination'] = destination
        self.parameters['date'] = date
        self.parameters['time'] = time

    def add_query(self, query):
        self.user_queries.append(query)
        self.history += f"User: {query}\n"

    def add_response(self, response):
        self.system_responses.append(response)
        self.history += f"System: {response}\n"

    def is_journey_request(self, user_query):
        prompt = f"Write 1 if the following query asked to make a journey plan, otherwise write 0 as a repsonse.Query: {user_query}"
        response = self.generate_chat_response(prompt)
        if response == '1':
            return True
        else:
            return False
        
    def process_query(self, user_query):
        system_response = ''
        self.add_query(user_query)
        

        # Check if it's a journey request and process accordingly
        if self.is_journey_request(user_query):
           self.generate_tfl_api_params()
           if self.parameters:
              self.generate_tfl_api_request()
              self.send_tfl_api_request()
              print(self.ecode)
              print(self.tfl_api_response)
              if self.ecode == 300:
                 system_response = self.generate_chat_response(f"""Multiple choices are detected from the following json text:{self.tfl_api_response}
                 Can you give the choices to the user in a user friendly way so that the correct journey can be planned?""")
              else:     
                 system_response = self.generate_chat_response(user_query)

        # Add the generated response to session history
        self.add_response(system_response)
        return system_response

    # Other methods remain unchanged...
    def generate_tfl_api_params(self):
            # Generate TfL API request using OpenAI GPT model"
        prompt = f"""Given a chat history for a journey, extract the following parameters for the most updated journey 
                 the user intends to plan:
                 source, destination, date and time. 
                 The response must only include the value of parameters in the given order seperated by &.
                 Today's date and time are {NOW}.
                 If the user hasn't explicitly mention the date and time, use current date and time.
                 Format the date as  YYYYMMDD and
                 the time as HHMM .Chat history: \"{self.history}\""""
        param_string = self.generate_chat_response(prompt)
        
        parameters = self.parse_param_string(param_string)

    def parse_param_string(self, param_string):
        
        parameters_list = param_string.split("&")
        keys = ['source', 'destination', 'date', 'time']
        self.parameters.update({key: value for key, value in zip(keys, parameters_list)})
        
        
    def generate_tfl_api_request(self):
        source_encoded = urllib.parse.quote(self.parameters['source'].strip())
        destination_encoded = urllib.parse.quote(self.parameters['destination'].strip())
        base_url = "https://api.tfl.gov.uk/Journey/JourneyResults"
        # Optional parameters with placeholder values
        optional_params = { 'date': self.parameters['date'].strip(),
                            'time': self.parameters['time'].strip(),
    
        }

        # Construct the URL with optional parameters
        self.tfl_api_request = f"{base_url}/{source_encoded}/to/{destination_encoded}"
    
        # Add optional parameters to the URL
        self.tfl_api_request +="?"
        self.tfl_api_request += "&".join([f"{key}={urllib.parse.quote_plus(str(value))}" for key, value in optional_params.items()])
        self.tfl_api_request = f"{self.tfl_api_request}&app_key={TFL_API_KEY}"
    
    def send_tfl_api_request(self):
        
        # Send the generated TfL API request
        
        print(self.tfl_api_request)
        response = requests.get(self.tfl_api_request)

        # Raise an exception if the request was unsuccessful
        response.raise_for_status()

        # Return the JSON response as a Python dictionary
        print(response.json())
        
    def format_journey_response(self):

        prompt = (f"""can you convert the following text below (produced as a result of https request to TfL API) 
                 into a conversational form and answer the user: {self.tfl_api_response}. Please write your response as 
                 if you are talking to the user directly. If there are multiple choices present the choices to the user.""")

        return self.generate_chat_response(prompt)

    def generate_chat_response(self, prompt):
        # Format the prompt to include interaction history
        
        
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=300
        )
        return response.choices[0].message.content







