from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

# Create a new instance of a ChatBot
bot = ChatBot('Wino', read_only=False, logic_adapters=["chatterbot.logic.BestMatch"])

# Train the chatbot with some data
trainer = ListTrainer(bot)
trainer.train([
    "Hello, how are you today?",
    "I am good, how about you?",
    "What is your name?",
    "My name is Wino.",
    "Nice to meet you",
    "Nice to meet you too!",
])

# Serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Handle POST requests
@app.route('/get', methods=['POST'])
def get_bot_response():
    user_text = request.json.get('msg')
    response = bot.get_response(user_text)
    return jsonify({"response": str(response)})

if __name__ == "__main__":
    app.run(debug=True,port=5000)


