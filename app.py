from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple rule-based chatbot logic
def get_response(user_input):
    responses = {
        "hello": "Hi! How can I help you today?",
        "how are you": "I'm good, thank you for asking!",
        "bye": "Goodbye! Have a great day!",
        "good morning": "very good morning",
        "good afternoon": "very good afternoon",
        "good evening": "very good evening",
        "good night": "good night",
        
    }
    return responses.get(user_input.lower(), "Sorry, I don't understand that.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['GET', 'POST'])
def chat():
    user_input = request.form['user_input']
    bot_response = get_response(user_input)
    return jsonify({'response': bot_response})

if __name__ == "__main__":
    app.run(debug=True)
