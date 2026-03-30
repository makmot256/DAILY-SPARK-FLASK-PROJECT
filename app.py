from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

quotes = [
    {"text": "The only way to do great work is to love what you do.", "author": "Steve Jobs", "category": "inspiration"},
    {"text": "In the middle of every difficulty lies opportunity.", "author": "Albert Einstein", "category": "inspiration"},
    {"text": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius", "category": "motivation"},
    {"text": "Life is what happens when you're busy making other plans.", "author": "John Lennon", "category": "life"},
    {"text": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt", "category": "inspiration"},
    {"text": "Spread love everywhere you go.", "author": "Mother Teresa", "category": "life"},
    {"text": "When you reach the end of your rope, tie a knot in it and hang on.", "author": "Franklin D. Roosevelt", "category": "motivation"},
    {"text": "Always remember that you are absolutely unique. Just like everyone else.", "author": "Margaret Mead", "category": "humor"},
    {"text": "Don't judge each day by the harvest you reap but by the seeds that you plant.", "author": "Robert Louis Stevenson", "category": "life"},
    {"text": "The secret of getting ahead is getting started.", "author": "Mark Twain", "category": "motivation"},
]

jokes = [
    {"text": "Why don't scientists trust atoms? Because they make up everything!", "category": "science"},
    {"text": "I told my wife she was drawing her eyebrows too high. She looked surprised.", "category": "classic"},
    {"text": "Why did the scarecrow win an award? Because he was outstanding in his field.", "category": "classic"},
    {"text": "I'm reading a book about anti-gravity. It's impossible to put down.", "category": "puns"},
    {"text": "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.", "category": "puns"},
    {"text": "Why do cows wear bells? Because their horns don't work.", "category": "classic"},
    {"text": "I would tell you a joke about construction, but I'm still working on it.", "category": "puns"},
    {"text": "Why can't you give Elsa a balloon? Because she'll let it go.", "category": "classic"},
    {"text": "What do you call fake spaghetti? An impasta!", "category": "puns"},
    {"text": "I asked my dog what two minus two is. He said nothing.", "category": "animals"},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/random")
def random_any():
    all_items = [{"type": "quote", **q} for q in quotes] + [{"type": "joke", **j} for j in jokes]
    return jsonify(random.choice(all_items))

@app.route("/api/quote")
def random_quote():
    quote = random.choice(quotes)
    return jsonify({"type": "quote", **quote})

@app.route("/api/joke")
def random_joke():
    joke = random.choice(jokes)
    return jsonify({"type": "joke", **joke})

if __name__ == "__main__":
    app.run(debug=True)
