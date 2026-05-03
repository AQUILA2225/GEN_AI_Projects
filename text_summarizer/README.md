# AI Text Summarizer App

## Overview

The **AI Text Summarizer App** is a Streamlit-based web application that summarizes long text or PDF documents into concise and meaningful content using Generative AI.

It supports **multiple Indian languages**, different summary lengths, and flexible output formats, making it useful for students, researchers, and professionals.


## Features

* Summarize long text instantly
* Upload and summarize PDF documents
* Choose summary length (Short / Medium / Detailed)
* Bullet-point or paragraph format
* Multilingual support (All major Indian languages)
* Download summary as a text file
* Error handling and input validation


## Tech Stack

* **Python**
* **Streamlit** (Frontend UI)
* **OpenAI API** (Text summarization)
* **PyPDF2** (PDF text extraction)
* **python-dotenv** (Environment variable management)


## 📂 Project Structure

text_summarizer_app/
│
├── app.py                # Main application file
├── .env                  # API key (not shared publicly)
├── requirements.txt      # Dependencies
└── README.md             # Project documentation


## Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/text_summarizer_app.git
cd text_summarizer_app


### 2️⃣ Install Dependencies

pip install -r requirements.txt


### 3️⃣ Add API Key

Create a `.env` file and add:

OPENAI_API_KEY=your_api_key_here

##  Run the App

streamlit run app.py

The app will open in your browser.


## How It Works

1. User selects input type (Text or PDF)
2. Enters text or uploads a PDF
3. Chooses:

   * Summary length
   * Output format
   * Language
4. App sends request to AI model
5. AI generates summary
6. User can view and download the result


## Key Highlights

* Clean and user-friendly UI
* Scalable language support system
* Prompt engineering for better accuracy
* Handles large input safely
* Real-world use case project


## Future Enhancements

* Auto language detection
* Voice input support
* PDF highlighting
* Save summary history
* Deploy on cloud (Streamlit Cloud / Render)



