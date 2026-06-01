import streamlit as st 
import PyPDF2 
import os
from openai import OpenAI
from dotenv import load_dotenv 

load_dotenv()

client = OpenAI(
    api_key = os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def analyze_resume(resume_text, job_description):
    prompt = f"""
    You are an expert resume analyzer.

    Compare the resume with the job description.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Give output in this format:
    1. Match Score:
    2. Missing Skills:
    3. Resume Improvement Suggestions:
    4. Suggested Resume Bullet Points:
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

st.title("AI Resume Analyzer")
st.write("Upload your resume and job description to analyze match score")

uploaded_resume = st.file_uploader("Upload your resume PDF", type=["pdf"])

job_description = st.text_area("Paste the job description here") 

if uploaded_resume is not None:
    st.success("Resume uploaded successfully")
    
    pdf_reader = PyPDF2.PdfReader(uploaded_resume)
    
    resume_text = "" 
    for page in pdf_reader.pages:
        resume_text += page.extract_text()
    
    st.subheader("Extracted Resume Text:")
    st.write(resume_text[:500])
    
if job_description:
    st.success("Job description added successfully")
    
if st.button("Analyze Resume"):
    if uploaded_resume is not None and job_description:
        st.info("Analyzing resume...")

        result = analyze_resume(resume_text, job_description)

        st.subheader("Analysis Result")
        st.write(result)

    else:
        st.warning("Please upload resume and enter job description.")