import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize chatbot
class MentalHealthChatbot:
    def __init__(self):
        self.system_prompt = "Aap ek supportive mental health chatbot hain jo Hinglish mein baat karta hai. Aapko logon ko motivate karna hai aur unka emotional support karna hai. Aapke responses Hindi aur English dono scripts mein ho sakte hain."

    def get_response(self, user_input):
        try:
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(f"Hinglish mein reply dijiye: {user_input}")
            return response.text.strip()
        except Exception as e:
            return "Mujhe abhi kuch technical dikkat ho rahi hai. Thodi der baad try karein!"

# Streamlit UI
def main():
    st.title("🌸 Hinglish Mental Health Chatbot")
    chatbot = MentalHealthChatbot()

    user_input = st.text_input("Apne thoughts share karein... (Share your thoughts...)")

    if user_input:
        response = chatbot.get_response(user_input)
        st.write(f"🤖 Chatbot: {response}")

if __name__ == "__main__":
    main()
