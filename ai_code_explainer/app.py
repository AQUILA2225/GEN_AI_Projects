import streamlit as st 
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv("groq_api_key"),
    base_url = "https://api.groq.com/openai/v1"
)

st.title("AI Code Explainer Tool")

st.write("Paste your code and get AI-powered explanations.")

language = st.selectbox(
    "Choose Programming Langunage",
    ["Python", "Java", "JavaScript", "C", "C++"]
)

mode = st.radio(
    "Choose Explanation Mode",
    ["Beginner", "Advanced"]
)

bug_check = st.checkbox("Check for bugs also")

code_input = st.text_area(
    "Paste Your Code Here",
    height=300
)

explain_button = st.button("Explain Code")

if explain_button:
    if code_input.strip() == "":
        st.warning("Please paste some code first.")
    else:
        bug_instruction = ""

        if bug_check:
            bug_instruction = """
Also check the code for:
1. Syntax errors
2. Logical errors
3. Runtime errors
4. Possible improvements
"""

        with st.spinner("AI is explaining your code..."):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert programming tutor. Explain code clearly."
                    },
                    {
                        "role": "user",
                        "content": f"""
Explain this {language} code in {mode} mode.

Code:
{code_input}

Give:
1. Simple overview
2. Line-by-line explanation
3. Important concepts used
4. Output if possible

{bug_instruction}
"""
                    }
                ]
            )

            explanation = response.choices[0].message.content

            st.success("Explanation Generated Successfully")

            with st.expander("📘 View AI Explanation"):
                st.write(explanation)

            with st.expander("💻 Your Submitted Code"):
                st.code(code_input, language=language.lower())