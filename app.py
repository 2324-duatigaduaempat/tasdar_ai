from flask import Flask, request, jsonify, render_template
import openai
import os
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

# Kunci API GPT
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    if request.method == "POST":
        user_message = request.form.get("message")
        if user_message:
            try:
                completion = openai.ChatCompletion.create(
                    model="gpt-4.0-turbo",
                    messages=[{"role": "user", "content": user_message}]
                )
                response_text = completion.choices[0].message["content"]
            except Exception as e:
                response_text = f"Ralat GPT: {str(e)}"
    return render_template("index.html", response=response_text)

if __name__ == '__main__':
    app.run(debug=True)
