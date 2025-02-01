# Hinglish Mental Health Chatbot

🌸 **Hinglish Mental Health Support Chatbot** is a Streamlit-based chatbot designed to provide emotional support and mental well-being assistance in Hinglish (a blend of Hindi and English). It uses the Gemini Pro model to generate empathetic and uplifting responses.

## Features

- 🗣 **Conversational Support**: Provides friendly and compassionate responses in Hinglish.
- 🌟 **Positive Affirmations**: Generates motivational messages to uplift users.
- 🧘‍♀️ **Guided Meditation**: Offers short meditation guides for relaxation.
- 🗑 **Chat History Management**: Saves conversation history and allows clearing it when needed.

## Technologies Used

- **Python**
- **Streamlit**
- **Google Generative AI (Gemini-Pro)**
- **dotenv** (for environment variables)
- **JSON** (for conversation history storage)

## Installation & Setup

### Prerequisites
- Python 3.x installed
- Google Generative AI API Key (Gemini API)

### Steps to Run the Chatbot

1. **Clone the repository**
   ```sh
   git clone https://github.com/your-repo/hinglish-mental-health-chatbot.git
   cd hinglish-mental-health-chatbot
   ```
2. **Create a virtual environment (optional but recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set up environment variables**
   - Create a `.env` file in the root directory.
   - Add your API key:
     ```
     GEMINI_API_KEY=your_gemini_api_key_here
     ```
5. **Run the chatbot**
   ```sh
   streamlit run chatbot.py
   ```

## Usage

- Type your thoughts in the chat input box and receive empathetic responses.
- Click on **Positive Affirmation** for a motivational message.
- Click on **Guided Meditation** for relaxation techniques.
- Use the **Clear Chat History** button to reset conversations.

## Example Interaction

**User:** Mujhe aaj bahut stress ho raha hai. 😞  
**Bot:** Koi baat nahi, sab theek ho jayega! Thoda deep breathing karo aur ek chhoti si walk pe chale jao. 😊

## Future Enhancements

- 🎙️ **Voice Input Support**
- 📱 **Mobile App Version**
- 📊 **Sentiment Analysis for Better Responses**

## Contributors
- **Vinayak Mittal** (Developer & Maintainer)

## License
This project is licensed under the MIT License. Feel free to modify and improve it!

🚀 **Happy chatting!** 😊

