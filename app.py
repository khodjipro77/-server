from flask import Flask, jsonify, request

app = Flask(__name__)

# Parollar ro'yxati - siz o'zgartirasiz
PASSWORDS = {
    "abcd": "active",
    "1234": "active", 
    "5678": "active",
}

@app.route('/check', methods=['POST'])
def check_password():
    data = request.get_json()
    password = data.get('password', '')
    
    if password in PASSWORDS and PASSWORDS[password] == "active":
        return jsonify({"status": "ok", "message": "Kirish muvaffaqiyatli"})
    else:
        return jsonify({"status": "error", "message": "Notogri parol"})

@app.route('/')
def home():
    return "VPN Server ishlayapti!"

if name == '__main__':
    app.run()
