import json

import requests
import streamlit as st
import numpy as np

import random

api_url = st.secrets["API_BASE_URL"]


st.set_page_config(page_title="Chat with PlantaAI", page_icon='🌱', layout='wide')

st.title("PlantaAI Chat Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask PlantaAI"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

# Display assistant response in chat message container
with st.chat_message("assistant"):
    message_placeholder = st.empty()
    full_response = ""

    if prompt:
        progress = st.progress(0)
        r = requests.post(f'{api_url}/query', json.dumps({'q': prompt}), stream=True)
        i = 1
        for chunk in r.iter_lines(decode_unicode=True, delimiter=' '):
            print(chunk)
            progress.progress(i)
            full_response += chunk + " "
            message_placeholder.markdown(full_response + "▌")
            i += 1

        message_placeholder.markdown(full_response)
        progress.empty()
    else:
        assistant_response = random.choice(
            ["Hello there! How can I assist you today?", "Hi there! Is there anything I can help you with?",
                "Do you need help?", ]
        )

        full_response = assistant_response

        st.markdown(full_response)
        st.markdown(f" I'm PlantaAI Chat Bot. ")
        st.markdown(f" I can help you with plant-based and meat/dairy products. ")
        st.markdown(f"I can specially help you with below scenarios.")
        st.markdown(f"1.  Compare a given \
            plant-based product and a given meat/dairy product based on prices, weight, ingredients, nutrition's, \
            and much more.")
        st.markdown(
            f"2. Select the best plant-based product based on your preferences."
            )

# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": full_response})