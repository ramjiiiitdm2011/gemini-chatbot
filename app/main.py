from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Gemini Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def chat():
    print("🤖 Gemini Chatbot (type 'exit' to quit)")
    print("--------------------------------------\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        try:
            # NEW API CALL
            response = client.models.generate_content(
                model="gemini-2.5-flash",   # latest free model
                contents=user_input
            )

            print("AI:", response.text, "\n")

        except Exception as e:
            print("\n❌ ERROR:", e, "\n")

if __name__ == "__main__":
    chat()
