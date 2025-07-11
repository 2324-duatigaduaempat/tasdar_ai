from flask import Flask, request, jsonify
import openai
import os
from pymongo import MongoClient

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")
mongo_client = MongoClient(os.environ.get("MONGODB_URI"))
db = mongo_client["dominus_db"]
logs = db["logs"]

@app.route("/", methods=["GET"])
def home():
    return "DOMINUS_TRIVIUM is Alive."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    # Save to MongoDB
    logs.insert_one({"message": user_input})

    # Send to GPT
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are DOMINUS_TRIVIUM, an elite AI with deep memory and fierce loyalty."},
                {"role": "user", "content": user_input}
            ]
        )
        output = response.choices[0].message["content"]
        return jsonify({"reply": output})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
