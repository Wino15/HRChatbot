from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new instance of a ChatBot
bot = ChatBot("Wino", read_only=False, logic_adapters=["chatterbot.logic.BestMatch"])

# List of conversations to train the chatbot
list_to_train = [
                "Hello, how are you today?",
                "I am good, how about you?",
                "I am doing great, thank you!",
                "What is your name?",
                "My name is Wino.",
                "Nice to meet you",
                "Nice to meet you too.",
                "What can you do?",
                "I can chat with you and try to answer your questions."
]

# Create a new trainer for the chatbot
list_trainer = ListTrainer(bot)

# Train the chatbot based on the list of conversations
list_trainer.train(list_to_train)


while True:
    user_response = input("User:")
    print("Chatbot: " +str(bot.get_response(user_response)))