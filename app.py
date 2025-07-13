from flask import Flask, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "TAS.DAR backend is alive (dual jantung version).",
        "status": "OK",
        "env_check": {
            "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", "not set"),
            "MONGODB_URI": os.getenv("MONGODB_URI", "not set")
        }
    })

if __name__ == "__main__":
    app.run(debug=True)
