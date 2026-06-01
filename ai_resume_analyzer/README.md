AI Resume Analyzer

An AI-powered Resume Analyzer built using Python, Streamlit, OpenAI API, and PyPDF2.
This application helps job seekers analyze their resumes against job descriptions and get ATS-friendly improvement suggestions.

🚀 Features
Upload Resume in PDF format
Extract resume text using PyPDF2
Paste Job Description
AI-powered resume analysis
Skill match evaluation
Missing skills identification
Resume improvement suggestions
Suggested ATS-friendly resume bullet points
Interactive Streamlit web interface

🛠️ Tech Stack
Frontend
Streamlit
Backend
Python
AI Integration
OpenAI API
PDF Processing
PyPDF2
Environment Variable Management
python-dotenv

📂 Project Structure
ai_resume_analyzer/
│
├── app.py
├── requirements.txt
├── .env
├── README.md

⚙️ Installation
1️⃣ Clone Repository
git clone <your-repository-link>
2️⃣ Move into Project Folder
cd ai_resume_analyzer
3️⃣ Install Required Libraries
pip install -r requirements.txt

🔑 Setup API Key

Create a .env file and add:

OPENAI_API_KEY=your_api_key_here

▶️ Run Application
streamlit run app.py

How It Works

User uploads resume PDF
        ↓
PyPDF2 extracts text
        ↓
User enters Job Description
        ↓
Resume + JD sent to OpenAI API
        ↓
AI analyzes content
        ↓
Displays:
- Match Score
- Missing Skills
- Suggestions
- ATS Improvements