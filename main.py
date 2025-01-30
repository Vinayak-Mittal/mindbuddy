import json
from datetime import datetime
import random
import os

class MentalHealthChatbot:
    def __init__(self):
        self.responses = {
            "greeting": [
                "Namaste! Kaise ho aap? Aaj kuch share karna chahenge?",
                "Hello! Kaisa chal raha hai? Main aapki help ke liye hun",
                "Hi! Aaj ka din kaisa ja raha hai? Kuch special hua kya?"
            ],
            "stress": [
                "Main samajh sakti hun. Stress bohot common hai. Deep breathing try karo - 4 seconds in, 4 seconds out",
                "Tension mat lo. Kuch relaxing activities try karte hain. Music sunna, walk pe jana, ya meditation help kar sakta hai",
                "Aapko stress feel ho raha hai? Chalo meditation karte hain. Aankhen band karke deep breaths lo"
            ],
            "sad": [
                "It's okay to feel sad. Baat share karna chahte ho? Main sun rahi hun",
                "Main hun na aapke saath. Kya hua? Kabhi kabhi baat share karne se dil halka ho jata hai",
                "Sadness temporary hai. Aap strong ho. Kya aapko kisi se baat karni chahiye? Family ya friends?"
            ],
            "anxiety": [
                "Anxiety normal hai. Deep breaths lo - 4 seconds in, 4 seconds out. Aap safe ho",
                "Abhi present moment pe focus karo. Sab theek ho jayega. 5 cheezein batao jo aap dekh sakte ho",
                "Anxiety ke time grounding exercises help karti hain. Apne surroundings pe focus karo"
            ],
            "happy": [
                "Bahut accha! Khush rehna important hai. Kya special hua aaj?",
                "Your happiness makes me happy! Aisa hi positive rehna. Celebration ka time hai!",
                "That's great! Ye khushi barkarar rakho. Kya plan hai aage ka?"
            ],
            "work": [
                "Work pressure common hai. Breaks lena important hai. Kya aap proper breaks le rahe ho?",
                "Office mein kya situation hai? Sometimes prioritizing tasks help karta hai",
                "Work-life balance zaroori hai. Aap apne liye time nikal rahe ho?"
            ],
            "family": [
                "Family matters sensitive hote hain. Aap apni feelings share karna chahte ho?",
                "Family ke saath communication important hai. Kya aap unse baat kar sakte ho?",
                "Ghar ki situation ke bare mein baat karna chahte ho? Main sun rahi hun"
            ],
            "relationship": [
                "Relationships mein ups and downs normal hain. Kya specific problem hai?",
                "Communication key hai relationships mein. Aapne partner se baat ki?",
                "Take your time to process feelings. Kya aap dono ne openly baat ki hai?"
            ],
            "health": [
                "Health first priority honi chahiye. Regular exercise aur proper diet follow kar rahe ho?",
                "Self-care bohot important hai. Kya aap apna dhyan rakh rahe ho?",
                "Mental aur physical health connected hai. Koi specific health concerns hain?"
            ],
            "motivation": [
                "Small steps bhi progress hai. Aap already bohot strong ho!",
                "Har din ek naya opportunity hai. Aap kya achieve karna chahte ho?",
                "Progress ki apni pace hoti hai. Khud pe vishwas rakho!"
            ],
            "bye": [
                "Take care! Dubara baat karenge. Apna khayal rakhna",
                "Alvida! Apna khayal rakhna. Kabhi bhi baat karni ho to main hun",
                "Bye bye! Jaldi milte hain. Stay positive!"
            ],
            "default": [
                "Main samajh rahi hun. Aur batao, kya feel kar rahe ho?",
                "Aapki baat sun rahi hun. Kuch specific share karna chahenge?",
                "I'm here to listen. Aage bolo, main aapke saath hun"
            ]
        }
        self.history_file = "chat_history.json"
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

    def analyze_mood(self, user_input):
        user_input = user_input.lower()
        if any(word in user_input for word in ["hi", "hello", "namaste", "hey", "hii", "helo"]):
            return "greeting"
        elif any(word in user_input for word in ["stress", "tension", "pareshan", "pressure", "load", "thak"]):
            return "stress"
        elif any(word in user_input for word in ["sad", "dukhi", "upset", "depression", "udas", "dard"]):
            return "sad"
        elif any(word in user_input for word in ["anxiety", "ghabrahat", "dar", "nervous", "panic", "worried"]):
            return "anxiety"
        elif any(word in user_input for word in ["happy", "khush", "accha", "great", "wonderful", "amazing"]):
            return "happy"
        elif any(word in user_input for word in ["office", "work", "job", "boss", "colleague", "career"]):
            return "work"
        elif any(word in user_input for word in ["family", "ghar", "parents", "mummy", "papa", "bhai", "behen"]):
            return "family"
        elif any(word in user_input for word in ["relationship", "boyfriend", "girlfriend", "partner", "love", "breakup"]):
            return "relationship"
        elif any(word in user_input for word in ["health", "bimari", "doctor", "medicine", "exercise", "diet"]):
            return "health"
        elif any(word in user_input for word in ["motivation", "inspire", "goal", "target", "achieve", "success"]):
            return "motivation"
        elif any(word in user_input for word in ["bye", "alvida", "goodbye", "tata", "phir milenge"]):
            return "bye"
        return "default"

    def get_response(self, user_input):
        mood = self.analyze_mood(user_input)
        response = random.choice(self.responses[mood])
        
        # Save to history
        self.history.append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "user": user_input,
            "bot": response
        })
        self.save_history()
        
        return response

    def show_history(self):
        if not self.history:
            return "Abhi tak koi conversation history nahi hai."
        
        history_text = "\nPichli baatcheet:\n"
        for entry in self.history[-5:]:  # Show last 5 conversations
            history_text += f"\nTime: {entry['timestamp']}\nAap: {entry['user']}\nBot: {entry['bot']}\n"
        return history_text

def main():
    print("Mental Health Chatbot (Hinglish)")
    print("--------------------------------")
    print("Aap se baat karke mujhe khushi hogi!")
    print("(Type 'bye' to exit, 'history' to see conversation history)")
    
    chatbot = MentalHealthChatbot()
    
    while True:
        user_input = input("\nAap: ").strip()
        
        if user_input.lower() == 'bye':
            print("\nBot:", chatbot.get_response("bye"))
            break
        
        if user_input.lower() == 'history':
            print(chatbot.show_history())
            continue
            
        response = chatbot.get_response(user_input)
        print("\nBot:", response)

if __name__ == "__main__":
    main()