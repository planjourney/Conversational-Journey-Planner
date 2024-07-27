#!/usr/bin/env python
# coding: utf-8

# In[ ]:



from http import HTTPStatus
import logging
import json
import requests
from new_sync import sync
from journey_client.client import AuthenticatedClient
from journey_client.types import UNSET
from openai import OpenAI
import os
from dotenv import load_dotenv
from journey_client.models.tfl_40 import Tfl40

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Ensure API keys are set
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TFL_API_KEY = os.getenv("TFL_API_KEY")
if not OPENAI_API_KEY or not TFL_API_KEY:
    raise ValueError("Missing API keys in .env file")

# Initialize OpenAI and TfL clients
OPENAI_CLIENT = OpenAI(api_key=OPENAI_API_KEY)
CLIENT_TFL = AuthenticatedClient(
    base_url="https://api.tfl.gov.uk/Journey",
    token=TFL_API_KEY
)

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_journey_info",
            "description": "Fetches journey planning data from a travel API for given start and end locations.",
            "parameters": {
                "type": "object",
                "properties": {
                    "from_": {
                        "type": "string",
                        "description": "The starting point of the journey.",
                    },
                    "to": {
                        "type": "string",
                        "description": "The destination point of the journey.",
                    },
                },
                "required": ["from_", "to"],
            },
        }
    },
]

# Extract disambiguation options
def extract_disambiguation_options(disambiguation):
    options = []
    for option in disambiguation['disambiguationOptions']:
        place = option['place']
        options.append({
            'parameterValue': option['parameterValue'],
            'uri': option['uri'],
            'commonName': place['commonName'],
            'lat': place['lat'],
            'lon': place['lon'],
        })
    return options

# Fetch journey planning data
def get_journey_info(from_, to):
    response = sync(from_, to, client=CLIENT_TFL)
    return response

# Create OpenAI response
def create_openai_response(messages):
    return OPENAI_CLIENT.chat.completions.create(
        model='gpt-4',
        messages=messages,
        tools=TOOLS,
        tool_choice="auto"
    )

# Choose the most relevant points from the response
def choose_most_relevant_points(response):
    from_ = ""
    to = ""
    json_content = response.content.decode('utf-8')
    parsed_content = json.loads(json_content)
    response.parsed = parsed_content
    
    to_location_disambiguation = parsed_content.get('toLocationDisambiguation')
    if to_location_disambiguation and 'disambiguationOptions' in to_location_disambiguation:
        destination_choices = extract_disambiguation_options(to_location_disambiguation)
        to = f"{destination_choices[0]['lat']},{destination_choices[0]['lon']}"
    
    from_location_disambiguation = parsed_content.get('fromLocationDisambiguation')
    if from_location_disambiguation and 'disambiguationOptions' in from_location_disambiguation:
        source_choices = extract_disambiguation_options(from_location_disambiguation)
        from_ = f"{source_choices[0]['lat']},{source_choices[0]['lon']}"
    
    return from_, to

# Extract journey information
def extract_journey_info(journey):
    journey_info = {
        "startDateTime": journey.get("startDateTime"),
        "duration": journey.get("duration"),
        "arrivalDateTime": journey.get("arrivalDateTime"),
        "legs": []
    }
    
    for leg in journey["legs"]:
        journey_info["legs"].append({
            "duration": leg["duration"],
            "departureTime": leg["departureTime"],
            "arrivalTime": leg["arrivalTime"],
            "detailed": leg["instruction"]["detailed"],
            "departurePoint": leg["departurePoint"]["commonName"],
            "arrivalPoint": leg["arrivalPoint"]["commonName"]
        })
    
    return journey_info

# Generate human-friendly response
def generate_ok_human_response(journey_info):
    prompt = (f"The following info is for a journey, produced by TfL API: {journey_info}. The user lives in London. "
              f"Can you convert the journey info into human-friendly version? Mention the starting point and destination "
              f"in the introduction. Ask the user if they need anything else?")
    
    response = OPENAI_CLIENT.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}],
        temperature=0.5,
        max_tokens=300
    )
    
    return response.choices[0].message.content

# Create human-friendly response
def create_human_friendly_response(raw_message):
    tool_calls = raw_message.tool_calls
    if tool_calls:
        tool_function_name = tool_calls[0].function.name
        tool_arguments = json.loads(tool_calls[0].function.arguments)
        response = get_journey_info(tool_arguments['from_'], tool_arguments['to'])
        
        if response.status_code == HTTPStatus.MULTIPLE_CHOICES:
            from_, to = choose_most_relevant_points(response)
            if not from_:
                from_ = tool_arguments['from_']
            if not to:
                to = tool_arguments['to']
            response = get_journey_info(from_, to)
        
        if response.status_code == HTTPStatus.OK:
            journey_plan = json.loads(response.content.decode('utf-8'))
            journeys = journey_plan['journeys']
            journey_info = extract_journey_info(journeys[0])
            return generate_ok_human_response(journey_info)
        elif response.status_code == HTTPStatus.BAD_REQUEST:
            return ("It looks like there was an issue with the request we sent to the Transport for London (TfL) system. "
                    "This might be due to an incorrect location or a temporary problem with the service. Here’s what you can do:\n"
                    "1. Check the locations: Please ensure the station names or addresses you provided are correct.\n"
                    "2. Try again: Sometimes, a temporary glitch can cause this issue. Please try your request again.\n"
                    "3. Contact support: If the problem persists, you can get more help by visiting the TfL support page or contacting their customer service.\n"
                    "Would you like me to try again with the same locations, or is there anything else I can help you with?")
    else:
        return raw_message.content


