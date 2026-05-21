from flask import Flask, jsonify, request

app = Flask(__name__)

PASSWORDS = {
    
    "9696": "active",
    
}

@app.route('/check', methods=['POST'])
def check_password():
    data = request.get_json()
    password = data.get('password', '')
    if password in PASSWORDS and PASSWORDS[password] == "active":
        return jsonify({"status": "ok"})
    return jsonify({"status": "error"})

@app.route('/')
def home():
    return "OK"
