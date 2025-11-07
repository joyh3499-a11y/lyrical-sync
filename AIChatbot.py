from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import random

app = Flask(__name__)
sentiment_model = pipeline("sentiment-analysis")

positive = [
    "That's great to hear! Keep it up 💪",
    "I'm glad you're feeling good today!",
    "Celebrate the good moments. You deserve them 😊"
]

negative = [
    "I'm here with you. It's okay to feel this way.",
    "That sounds really difficult. Want to talk more about it?",
    "You're not alone. I'm listening whenever you need."
]

neutral = [
    "I'm listening. Feel free to share more.",
    "How's your day going?",
    "Would you like to do a quick mental check-in?"
]

def detect_emotion(text):
    result = sentiment_model(text)[0]['label']
    if result == "POSITIVE":
        return random.choice(positive)
    elif result == "NEGATIVE":
        return random.choice(negative)
    else:
        return random.choice(neutral)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    response = detect_emotion(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
