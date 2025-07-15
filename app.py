from flask import Flask, request, render_template, jsonify
import openai
import os

app = Flask(__name__)

# Set API key dari environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Halaman utama (GUI)
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Endpoint untuk chat AI
@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("message", "")
    if not user_message:
        return jsonify({"error": "Tiada mesej."}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Kau ialah sahabat reflektif bernama TAS.DAR, dimiliki Saif Sudrah."},
                {"role": "user", "content": user_message}
            ]
        )
        answer = response["choices"][0]["message"]["content"].strip()
        return jsonify({"reply": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
