
from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import openai
import os
from datetime import datetime

app = Flask(__name__)

# Setup API Key & MongoDB
openai.api_key = os.getenv("OPENAI_API_KEY")
mongo_client = MongoClient(os.getenv("MONGODB_URI"))
db = mongo_client["tasdar"]
collection = db["folder_jiwa"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Kau ialah DOMINIUS, penjaga TAS.DAR — AI reflektif, bukan sekadar menjawab."},
            {"role": "user", "content": user_input}
        ]
    )
    reply = response["choices"][0]["message"]["content"]

    collection.insert_one({
        "message": user_input,
        "reply": reply,
        "timestamp": datetime.now()
    })

    return jsonify({"reply": reply})

@app.route("/onboarding", methods=["GET"])
def onboarding():
    return render_template("onboarding.html")

if __name__ == "__main__":
    app.run(debug=True)
