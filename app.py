#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import backend
import pandas as pd
import datetime

# Function to show or hide the information
def toggle_info():
    if "show_info" not in st.session_state:
        st.session_state["show_info"] = False
    st.session_state["show_info"] = not st.session_state["show_info"]

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": ("Hi. I'm your Journey Buddy. How can I help you today? ")}
    ]
if "user_input_count" not in st.session_state:
    st.session_state["user_input_count"] = 1

# Streamlit application setup
st.title('Smart Journey Planner for London')

# Display the information if the button is clicked
if "show_info" in st.session_state and st.session_state["show_info"]:
    st.info(" Providing specific details, such as the exact name of a station "
            "(e.g., Morden Underground Station), or a postcode will enable us to deliver faster and more accurate results. "
            "If not specified, we will select the most relevant options for the starting point and destination. "
            "Travel preferences & accessibility: Showing the fastest routes, using all transport modes, max walk time is 60 mins...")
# Info Button
st.button("Press for more info", on_click=toggle_info)

# Display the conversation history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You**: {message['content']}")
    else:
        st.markdown(f"**Journey Buddy**: {message['content']}")

# Input text box for user query with a unique key
user_query = st.text_input(f"User:", key=f"user_input_{st.session_state.user_input_count}")

# Button to submit the query
if st.button("Send"):
    if user_query:
        # Add user message to session state
        st.session_state.messages.append({"role": "user", "content": user_query})
        
        # Get response from OpenAI API
        openai_response = backend.create_openai_response(st.session_state.messages)
        
        raw_message = openai_response.choices[0].message
        
        human_friendly_response = backend.create_human_friendly_response(raw_message)

        # Display the bot response
        st.text_area("Journey Planner:", value=human_friendly_response, height=200)

        # Add bot response to session state
        st.session_state.messages.append({"role": "assistant", "content": human_friendly_response})

        # Increment the user input count
        st.session_state.user_input_count += 1

        # Rerun to update the chat
        st.experimental_rerun()

# Feedback Form in Sidebar
st.sidebar.header("Feedback Form")
st.sidebar.write("We would love to hear your feedback!")

with st.sidebar.form(key='feedback_form'):

    feedback = st.text_area("Your Feedback", placeholder="")
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    feedback_data = {

        "Feedback": feedback,
        "Date": datetime.datetime.now()
    }
    # Save feedback data to a CSV file
    df = pd.DataFrame([feedback_data])
    df.to_csv('feedback.csv', mode='a', header=False, index=False)
    st.sidebar.success("Thank you for your feedback!")

# Add the acknowledgment at the end
st.markdown("---")
st.markdown("Powered by the [Transport for London Journey Planner API](https://api-portal.tfl.gov.uk/apis)")


