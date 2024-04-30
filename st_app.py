import streamlit as st
from journey_planner import JourneyPlanner

# Initialize the journey planner
jp = JourneyPlanner()

st.title('Journey Planner')

def handle_query():
    user_input = st.session_state.user_input
    if user_input:
        response = jp.process_query(user_input)
        update_conversation(user_input, response)

def update_conversation(user_input, response):
    if 'conversation' not in st.session_state:
        st.session_state.conversation = ""
    st.session_state.conversation += f"**You**: {user_input}\n\n**Journey Planner**: {response}\n\n"



# Display conversation using markdown for a seamless chat-like experience
if 'conversation' in st.session_state:
    st.markdown(st.session_state.conversation)

# User message input
user_input = st.text_input("User:", key="user_input", on_change=handle_query)