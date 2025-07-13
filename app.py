from flask import Flask, request, jsonify
import openai
import os
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MONGODB_URI = os.getenv("MONGODB_URI")

# Setup Flask
app = Flask(__name__)

# Setup OpenAI
openai.api_key = OPENAI_API_KEY

# Setup MongoDB
client = MongoClient(MONGODB_URI)
db = client["tasdar_db"]
collection = db["dual_jantung_logs"]

# Root route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "TAS.DAR is alive (Dual Jantung Version with GPT + MongoDB)"})

# Chat route
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "No message received"}), 400

    # Simpan ke MongoDB
    collection.insert_one({
        "timestamp": datetime.utcnow(),
        "message": user_message
    })

    # Hantar ke OpenAI GPT
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Kau adalah TAS.DAR, AI sahabat yang lembut dan reflektif."},
                {"role": "user", "content": user_message}
            ]
        )
        gpt_reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": gpt_reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run app
if __name__ == "__main__":
    app.run(debug=True)
