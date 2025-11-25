# 🤖 Gemini Chatbot

A simple and powerful **Generative AI Chatbot** built using the **Google Gemini API**, developed entirely inside **GitHub Codespaces**.  
This project includes:

- 🧠 Python terminal chatbot  
- 🌐 Streamlit-based Web Chat UI  
- 🔐 Secure `.env` usage for API keys  
- ⚡ New Gemini API (2025 version)

---

## 🚀 Features

### ✔ Terminal Chatbot
Run a Gemini-powered chatbot directly in your terminal using Python.

### ✔ Web-based Chat Interface
A clean and simple **Streamlit Web App**:

- Chat with Gemini in your browser  
- Chat history  
- Emoji-enhanced UI  
- Fully interactive

### ✔ Modern Google Gemini API
Uses the **latest 2025 Google Gemini API** with:

- `genai.Client()`
- `client.models.generate_content()`
- `gemini-2.5-flash` model

---

## 📁 Project Structure

gemini-chatbot/
│
├── app/
│ ├── main.py # Terminal chatbot
│ └── web_app.py # Streamlit web UI
│
├── .env # API key (not tracked in GitHub)
├── .gitignore # Prevents .env from uploading
├── requirements.txt # Python dependencies
└── README.md # Project documentation



---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/gemini-chatbot.git
cd gemini-chatbot

Create a Virtual Environment (Optional)
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows

Install Dependencies
pip install -r requirements.txt

Add Your Gemini API Key

Create a .env file:

GEMINI_API_KEY=your_key_here

Run the Terminal Chatbot
python app/main.py

Run the Web App (Streamlit)
streamlit run app/web_app.py

Then open the forwarded link (8501 port) in your browser.