# 🧠 AI Content Generator

## Overview

AI Content Generator is a Generative AI web application that creates high-quality content such as **Blog Posts, LinkedIn Posts, and Twitter Threads** based on user input.

The application allows users to customize tone, format, and word limit, making it useful for **content creators, marketers, and professionals**.


## Features

* Generate content from any topic
* Multiple content formats:

* Blog Post
* LinkedIn Post
* Twitter/X Thread
* Tone selection:

* Formal
* Casual
* Technical
* Creative
* Word limit control
* Fast AI response using OpenAI API
* Loading spinner for better UX
* Download generated content
* Copy-friendly output
* Error handling for API issues
* Clean UI with Streamlit Sidebar

## Tech Stack

* **Python**
* **Streamlit**
* **OpenAI API**
* **python-dotenv**

## Project Structure


ai-content-generator/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│── .env (not included in repo)
│── venv/ (not included)


## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

git clone https://github.com/your-username/ai-content-generator.git
cd ai-content-generator

### 2️⃣ Create virtual environment

python -m venv venv
venv\Scripts\activate

### 3️⃣ Install dependencies

pip install -r requirements.txt

### 4️⃣ Add API Key

Create a `.env` file and add:

OPENAI_API_KEY=your_api_key_here


### 5️⃣ Run the application


streamlit run app.py

## 🧠 How It Works

* User provides topic, tone, and content type
* Application generates a structured prompt
* OpenAI API processes the request
* Output is displayed in a formatted way


## Use Cases

* Content writing automation
* Social media post generation
* Blogging assistance
* Marketing content creation


## Future Improvements

* Generate multiple variations
* Save content history
* Add user authentication
* SEO optimization features
* Integration with social media platforms


## Security Note

* API keys are stored in `.env` file
* `.env` and `venv` are excluded using `.gitignore`


