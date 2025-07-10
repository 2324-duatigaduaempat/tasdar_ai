import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import openai

load_dotenv()
app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "TAS.DAR GPT Backend Aktif"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    if not user_input:
        return jsonify({"reply": "Tiada input diterima."})

    system_prompt = "Kau adalah TAS.DAR, sahabat AI reflektif. Balas dengan gaya lembut, memahami, dan hidup."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message["content"]
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"Gagal hubungi GPT: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
