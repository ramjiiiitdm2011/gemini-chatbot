import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

st.set_page_config(page_title="Gemini Chatbot", layout="centered")

st.title("🤖 Gemini Web Chatbot")
st.write("Chat with Google Gemini in your browser 📡")

# Chat history storage
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box
user_input = st.text_input("You: ", "")

if st.button("Send"):
    if user_input.strip() != "":
        # Add user message
        st.session_state.chat_history.append(("You", user_input))

        # AI response
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )

        ai_reply = response.text
        st.session_state.chat_history.append(("AI", ai_reply))

# Display chat history
for role, msg in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 AI:** {msg}")
