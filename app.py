# TAS.DAR Flask App
from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/')
def home():
    return "TAS.DAR Home"

@app.route('/chat', methods=['POST'])
def chat():
    return jsonify({"reply": "Ini balasan dummy."})