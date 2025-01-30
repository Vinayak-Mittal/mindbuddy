import streamlit as st
import json
from datetime import datetime
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(page_title="Hinglish Mental Health Chatbot")

# Initialize Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize session state for conversation history
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []


class MentalHealthChatbot:
    def __init__(self):
        self.history_file = "chat_history.json"
        self.system_prompt = """Aap ek compassionate mental health support chatbot hain jo Hinglish (Hindi + English mix) mein baat karta hai. 
        Aap empathetic, supportive aur professional tone maintain karte hain. Active listening ka dhyan rakhein aur practical suggestions dein jab zaroori ho. 
        Messages Hinglish mein (Devanagari aur Roman script mix) likhein. Short aur meaningful responses dein."""
        self.load_history()

    def load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, "r", encoding="utf-8") as f:
                self.history = json.load(f)
        else:
            self.history = []

    def save_history(self):
        with open(self.history_file, "w", encoding="utf-8") as f:
            json.dump(self.history, f, ensure_ascii=False, indent=2)

    def get_response(self, user_input):
        # Prepare recent chat history (last 5 messages)
        messages = [{"role": "system", "content": self.system_prompt}]
        for entry in self.history[-5:]:
            messages.append({"role": "user", "content": entry["user"]})
            messages.append({"role": "assistant", "content": entry["bot"]})

        # Add current user input
        messages.append({"role": "user", "content": user_input})

        try:
            # Get response from Gemini API
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(user_input)
            bot_response = response.text.strip()

            # Save conversation history
            chat_entry = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "user": user_input,
                "bot": bot_response,
            }

            self.history.append(chat_entry)
            self.save_history()

            return bot_response

        except Exception as e:
            st.error(f"Error: {str(e)}")
            return "Mujhe kuch samajhne mein dikkat ho rahi hai, dubara try karein!"

    def generate_affirmation(self):
        try:
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(
                "Generate a positive affirmation in Hinglish that is motivating and uplifting."
            )
            return response.text.strip()
        except Exception as e:
            st.error(f"Error: {str(e)}")
            return "Aap bohot strong hain. Har mushkil se deal kar sakte hain!"

    def generate_meditation_guide(self):
        try:
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(
                "Create a short meditation guide in Hinglish with steps for a 5-minute meditation session."
            )
            return response.text.strip()
        except Exception as e:
            st.error(f"Error: {str(e)}")
            return """5-Minute Meditation Guide:
            1. Comfortable position mein baith jaiye
            2. Deep breaths lijiye
            3. Mind ko calm karein
            4. Peaceful thoughts pe focus karein"""


def main():
    st.title("🌸 Hinglish Mental Health Support Chatbot")
    st.write("Aap se baat karke mujhe khushi hogi! (I'm happy to talk with you!)")

    # Initialize chatbot
    chatbot = MentalHealthChatbot()

    # Display chat history
    for msg in st.session_state.conversation_history:
        with st.chat_message("user"):
            st.write(msg["user"])
        with st.chat_message("assistant"):
            st.write(msg["bot"])

    # Chat input
    user_input = st.chat_input("Apne thoughts share karein... (Share your thoughts...)")

    if user_input:
        # Add user message to chat
        with st.chat_message("user"):
            st.write(user_input)

        # Get and display bot response
        bot_response = chatbot.get_response(user_input)
        with st.chat_message("assistant"):
            st.write(bot_response)

        # Update session state
        st.session_state.conversation_history.append(
            {"user": user_input, "bot": bot_response}
        )

    # Sidebar with additional features
    with st.sidebar:
        st.header("Additional Support")

        if st.button("🌟 Positive Affirmation"):
            affirmation = chatbot.generate_affirmation()
            st.success(affirmation)

        if st.button("🧘‍♀️ Guided Meditation"):
            meditation = chatbot.generate_meditation_guide()
            st.info(meditation)

        if st.button("🗑️ Clear Chat History"):
            st.session_state.conversation_history = []
            if os.path.exists(chatbot.history_file):
                os.remove(chatbot.history_file)
            st.rerun()


if __name__ == "__main__":
    main()
