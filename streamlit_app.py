import streamlit as st
import requests
import json
from skills.api_integration import call_openai_api

# Function to invoke the selected LLM
def invoke_llm(prompt, llm_provider, model, api_key):
    headers = {"Authorization": f"Bearer {api_key}"}
    
    if llm_provider == "OpenAI":
        response = call_openai_api(prompt)
        return response.choices[0].text
    elif llm_provider == "Groq":
        # Implement Groq call via OpenAI library
        response = call_openai_api(prompt)  # Update this to call the Groq model
        return response.choices[0].text
    elif llm_provider == "Anthropic Claude":
        # Implement Anthropic Claude call via OpenAI library
        response = call_openai_api(prompt)  # Update this to call the Claude model
        return response.choices[0].text
    else:
        return "Unsupported LLM provider."

# Sidebar for LLM configuration
st.sidebar.title("LLM Configuration")
llm_provider = st.sidebar.selectbox("Select LLM Provider", ["OpenAI", "Groq", "Anthropic Claude"])
model = st.sidebar.text_input("Model", value="text-davinci-003")
api_key = st.sidebar.text_input("API Key", type="password")

# Sidebar for setting up the workflow
st.sidebar.title("Setup Workflow")
template_name = st.sidebar.selectbox("Select Template", ["board_game_development_template"])
system_message = st.sidebar.text_input("System Message", "You are an AI assistant.")
tone = st.sidebar.text_input("Tone", "Collaborative and Creative")
goal = st.sidebar.text_input("Goal", "Assist in developing a board game from concept to final production.")
audience = st.sidebar.text_input("Audience", "Game designers and developers")

if st.sidebar.button("Start Workflow"):
    st.session_state['chat_history'] = []

# Chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Chat container
st.subheader("Chat")

def display_chat(chat_history):
    for chat in chat_history:
        if chat['role'] == 'user':
            st.text_area("You", value=chat['content'], height=100)
        else:
            st.text_area("AI", value=chat['content'], height=100)

display_chat(st.session_state['chat_history'])

# User input
user_input = st.text_input("Type your message here...")

def send_message():
    if user_input:
        st.session_state['chat_history'].append({'role': 'user', 'content': user_input})
        
        # Prepare prompt from template and variables
        prompt = f"""
        System Message: {system_message}
        Tone: {tone}
        Goal: {goal}
        Audience: {audience}
        User Message: {user_input}
        """
        
        # Invoke LLM with the selected configuration
        ai_response = invoke_llm(prompt, llm_provider, model, api_key)
        
        st.session_state['chat_history'].append({'role': 'assistant', 'content': ai_response})

if st.button("Send"):
    send_message()

# Display updated chat history
display_chat(st.session_state['chat_history'])
