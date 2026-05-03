import streamlit as st
import os  
from dotenv import load_dotenv 
from openai import OpenAI
from PyPDF2 import PdfReader 

load_dotenv()

client = OpenAI(
    api_key = os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text

def generate_summary(text, summary_length, bullet_points, summary_language):
    text = text[:50000]
    if bullet_points:
        format_instruction = "Write the summary in clear bullet points."
    else:
        format_instruction = "Write the summary in clear paragraph format."

    prompt = f"""
    You are an expert text summarizer.

    Your task:
    Summarize the given text clearly and accurately.

    Instructions:
    - Summary length should be: {summary_length}
    - Summary format should be: {format_instruction}
    - Summary language should be: {summary_language}
    - Keep the meaning of the original text unchanged
    - Do not add extra information outside the given text
    - Use simple and understandable language

    Text:
    {text}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You summarize text accurately, clearly, and in the requested language."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

st.set_page_config(page_title="Text Summarizer", layout="centered")

st.title("📝 AI Text Summarizer")

st.write("Upload a PDF or paste text to generate a summary.")

input_type = st.radio(
    "Choose Input Type",
    ["Text", "PDF Upload"]
)

user_text = ""
uploaded_file = None

if input_type == "Text":
    user_text = st.text_area("Enter your text here:")

elif input_type == "PDF Upload":
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

summary_length = st.selectbox(
    "Select Summary Length",
    ["Short", "Medium", "Detailed"]
)

bullet_points = st.checkbox("Show as Bullet Points")

summary_language = st.selectbox(
    "Select Summary Language",
    ["English", "Hindi", "Telugu", "Kannada"]
)

generate_btn = st.button("Generate Summary")

if generate_btn:
    final_text = ""

    if input_type == "Text":
        final_text = user_text
    elif input_type == "PDF Upload" and uploaded_file is not None:
        final_text = extract_text_from_pdf(uploaded_file)

    if final_text.strip() == "":
        st.warning("Please enter text or upload a PDF file.")
        
    elif len(final_text) > 15000:
        st.warning("Text is too large. Please upload or enter shorter text.")
        
    else:
        try:
            with st.spinner("Generating summary..."):
                summary = generate_summary(final_text, summary_length, bullet_points, summary_language)

            st.subheader("Generated Summary")
            st.write(summary)
            
            st.download_button(
                label="Download Summary",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )
        except Exception as e:
            st.error("Something went wrong while generating the summary.")
            st.write(e)