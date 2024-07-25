from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

# Create a new instance of a ChatBot
chatbot = ChatBot("HR Bot")

# Train the chatbot with a corpus of pre-defined responses
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Placeholder for FAQs (you can add more FAQs here)
faqs = {
    "What are the office hours?": "Our office hours are from 9 AM to 6 PM, Monday to Friday.",
    "Where is the office location?": "Our office is located at Anantara Towers, 27th Floor, Business Bay, Dubai",
    "How can I reset my password?": "You can reset your password by visiting the IT department or using the self-service portal.",
    "What is the company's dress code?": "The company's dress code is business casual."
}

def get_response(user_message):
    # Check if the user message matches any FAQ
    if user_message in faqs:
        return faqs[user_message]
    else:
        # If not, get a response from the chatbot
        bot_response = chatbot.get_response(user_message)
        return str(bot_response)

# Keep the chat running to allow continuous conversation
while True:
    try:
        user_response = input("User: ")
        response = get_response(user_response)
        print("HR Bot: " + response)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
