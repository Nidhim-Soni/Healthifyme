import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

# Lets get the API Key from the environment

gemini_api_key = os.getenv('Google_API_Key2')

# Lets configure the model
model = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash-lite',
    api_key = gemini_api_key,
    temperature = 0.7
)

# Lets design the UI of application

st.title('HealthifyMe: Your personal Health Assistance')