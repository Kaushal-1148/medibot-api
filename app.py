from flask import Flask, request, jsonify
from ai_bot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return "Prescripto AI Chatbot API is running"

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Message is required"}), 400

    message = data["message"]

    try:
        reply = get_response(message)
        return jsonify({"reply": reply})

    except Exception as e:
        print("Error:", e)
        return jsonify({"reply": "Server is busy. Please try again."}), 500

if __name__ == "__main__":
    app.run(debug=True)