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

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        message = data.get("message", "")

        if not message:
            return jsonify({"error": "No message provided"}), 400

        # Sambung MongoDB
        client = MongoClient(mongo_uri)
        db = client["tasdar_db"]
        collection = db["chat_history"]

        # Simpan mesej pengguna
        collection.insert_one({"role": "user", "message": message})

        # Panggil GPT
        openai.api_key = openai_api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}]
        )

        gpt_reply = response.choices[0].message.content

        # Simpan balasan GPT
        collection.insert_one({"role": "assistant", "message": gpt_reply})

        return jsonify({"reply": gpt_reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
