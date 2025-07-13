from flask import Flask, request, jsonify
from pymongo import MongoClient
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load dari .env

app = Flask(__name__)

# Setup MongoDB
mongo_uri = os.getenv("MONGODB_URI")
mongo_client = MongoClient(mongo_uri)
db = mongo_client["tasdar_db"]
messages_collection = db["folder_jiwa"]

# Setup OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return jsonify({"message": "TAS.DAR is alive (Dual Jantung Version with GPT + MongoDB)"})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    # Simpan ke MongoDB
    messages_collection.insert_one({"role": "user", "message": user_message})

    # Hantar ke GPT
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    reply = completion.choices[0].message["content"]

    # Simpan balasan AI
    messages_collection.insert_one({"role": "assistant", "message": reply})

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
