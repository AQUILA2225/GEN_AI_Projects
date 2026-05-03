import streamlit as st 
import os 
from dotenv import load_dotenv
from openai import OpenAI

st.set_page_config(
    page_title="AI Content Generator",
    page_icon="🧠",
)

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

st.title("AI Content Generator")
st.write("Generate blogs, LinkedIn Posts, and Tweets using AI")

topic = st.text_input("Enter Topic")

tone = st.selectbox(
    "Select Tone",
    ["Formal", "Casual", "Technical", "Creative"] 
)

content_type = st.selectbox(
    "Select Content Type",
    ["Blog Post", "LinkedIn Post", "Twitter Thread"]
)

word_limit = st.slider("Word Limit", 50, 500, 150)

generate_btn = st.button("Generate Content") 
if generate_btn:
    if topic == "":
        st.warning("Please enter a topic")
    else:
        with st.spinner("Generating Content..."):
            prompt = f"""
                You are an expert content creator.

                Create a {content_type} about: {topic}

                Requirements:
                - Tone: {tone}
                - Word limit: around {word_limit} words
                - Make the content engaging and useful
                - Use clear formatting
                - Avoid unnecessary repetition

                If the format is:
                Blog Post: include title, introduction, main points, and conclusion.
                LinkedIn Post: include hook, body, and call-to-action.
                Twitter Thread: create numbered tweets.
                """
        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are a professional content writer."},
                    {"role": "user", "content": prompt}
                ]
            )

            output = response.choices[0].message.content
            st.subheader("Generated Content")
            st.markdown(output)
            
            st.download_button(
                label = "Download Content",
                data = output,
                file_name = "generated_content.txt",
                mime = "text/plain"
            )
        
            # st.code(output)
        except Exception as e:
            st.error("Something went wrong. Please check your API key or internet connection.")
            st.write(e)
