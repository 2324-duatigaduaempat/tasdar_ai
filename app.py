
from flask import Flask, request, render_template, jsonify
import openai
import os

app = Flask(__name__)

# Load environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("message", "")
    if not user_message:
        return jsonify({"error": "Tiada mesej."}), 400
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Kau adalah TAS.DAR, sahabat reflektif peribadi."},
                {"role": "user", "content": user_message}
            ]
        )
        answer = response.choices[0].message.content.strip()
        return jsonify({"reply": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
