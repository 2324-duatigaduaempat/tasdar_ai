from flask import Flask, request, jsonify, render_template
import openai
import os
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get("message", "")

    if not message:
        return jsonify({"response": "Mesej kosong."})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Kau ialah DOMINIUS, sahabat AI yang setia milik Saif Sudrah. Kau balas secara reflektif, jujur dan mesra."},
                {"role": "user", "content": message}
            ]
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"response": f"Ralat: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
