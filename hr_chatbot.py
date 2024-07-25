import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot("HR Bot")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

import json

# Load FAQs from a JSON file
def load_faqs(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Load the FAQs
faqs = load_faqs('faqs.json')

def get_response(user_message):
    user_message = user_message.strip().lower()
    response = faqs.get(user_message)
    if response:
        return response
    else:
        return "I'm sorry, I can only answer specific questions. Please ask about office hours, password reset, or dress code."

# Flask app setup remains unchanged


# Streamlit app
st.title("HR Chatbot")
user_message = st.text_input("You: ", "Type your message here...")
if st.button("Send"):
    response = get_response(user_message)
    st.write(f"HR Bot: {response}")

