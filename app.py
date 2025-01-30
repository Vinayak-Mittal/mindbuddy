import streamlit as st
import json
from datetime import datetime
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(page_title="Hinglish Mental Health Chatbot")

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Initialize session state for conversation history
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

class MentalHealthChatbot:
    def __init__(self):
        self.history_file = "chat_history.json"
        self.system_prompt = """You are a compassionate mental health support chatbot that communicates in Hinglish 
        (mix of Hindi and English). Provide empathetic, supportive responses while maintaining a professional tone. 
        Focus on active listening and offering practical suggestions when appropriate. Always respond in Hinglish 
        using both Devanagari and Roman scripts as needed. Keep responses concise but meaningful."""
        self.load_history()

    def load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r', encoding='utf-8') as f:
                self.history = json.load(f)
        else:
            self.history = []

    def save_history(self):
        with open(self.history_file, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, ensure_ascii=False, indent=2)

    def get_response(self, user_input):
        # Prepare conversation history for API
        messages = [{"role": "system", "content": self.system_prompt}]
        
        # Add recent conversation history (last 5 messages)
        for entry in self.history[-5:]:
            messages.append({"role": "user", "content": entry["user"]})
            messages.append({"role": "assistant", "content": entry["bot"]})
        
        # Add current user input
        messages.append({"role": "user", "content": user_input})
        
        try:
            # Get response from OpenAI API
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=150,
                temperature=0.7,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            
            bot_response = response.choices[0].message.content.strip()
            
            # Save to history
            chat_entry = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "user": user_input,
                "bot": bot_response
            }
            
            self.history.append(chat_entry)
            self.save_history()
            
            return bot_response
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
            return "I'm sorry, I'm having trouble responding right now. Please try again."

    def generate_affirmation(self):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Generate a positive affirmation in Hinglish that is motivating and uplifting."},
                    {"role": "user", "content": "Generate a positive affirmation"}
                ],
                max_tokens=50,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            st.error(f"Error: {str(e)}")
            return "Aap bohot strong hain. Har mushkil se deal kar sakte hain!"

    def generate_meditation_guide(self):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Generate a short meditation guide in Hinglish with steps for a 5-minute meditation session."},
                    {"role": "user", "content": "Create a meditation guide"}
                ],
                max_tokens=200,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
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
        st.session_state.conversation_history.append({
            "user": user_input,
            "bot": bot_response
        })

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