import streamlit as st
from dotenv import load_dotenv
import os
from openai import OpenAI
import time

# Load env
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

st.set_page_config(page_title="AI Chatbot", page_icon="🤖") 

st.sidebar.title("⚙️ Settings")

st.sidebar.markdown("""
This is a custom AI chatbot built using:
- Streamlit
- Groq API
- Python

Choose assistant type and start chatting
""")

st.markdown("<h1 style='text-align: center;'>🤖 AI Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Your personal AI assistant</p>", unsafe_allow_html=True)

assistant_type = st.sidebar.selectbox(
    "Choose Assistant Type",
    ["Tutor", "Friend", "Coding Assistant"]
)

if st.sidebar.button("Reset Chat"):
    st.session_state.messages = []
    st.rerun()

# Create memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input box
user_input = st.chat_input("Ask something...")

if assistant_type == "Tutor":
    system_prompt = "You are a helpful tutor. Explain everything in very simple words."
elif assistant_type == "Friend":
    system_prompt = "You are a friendly and casual assistant. Talk like a human friend."
else:
    system_prompt = "You are a coding assistant. Help with programming clearly."
    
if user_input:
    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    with st.spinner("🤖 Thinking..."):
        response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages
        ]
    )

    reply = response.choices[0].message.content


    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })
    
    def stream_text(text):
        for char in text:
            yield char
            time.sleep(0.01)
            
    with st.chat_message("assistant"):
        st.write_stream(stream_text(reply))