import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import openai
from dotenv import load_dotenv
import datetime

load_dotenv()

app = Flask(__name__)
CORS(app)

# Load keys from environment
openai.api_key = os.getenv("OPENAI_API_KEY")
mongo_uri = os.getenv("MONGODB_URI")

client = MongoClient(mongo_uri)
db = client["tasdar_db"]
collection = db["messages"]

@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "TAS.DAR is alive (Dual Jantung Version with GPT + MongoDB)"}), 200

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_message = data.get("message", "")

        # GPT response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        reply = response.choices[0].message.content

        # Save to MongoDB
        collection.insert_one({
            "message": user_message,
            "reply": reply,
            "timestamp": datetime.datetime.utcnow()
        })

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
