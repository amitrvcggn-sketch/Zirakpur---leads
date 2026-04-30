from flask import Flask, request, jsonify
app = Flask(_name_)

# Health check ke liye
@app.route('/')
def home():
    return "Webhook is running!", 200

# Meta webhook verification ke liye
@app.route('/webhook', methods=['GET'])
def verify():
    if request.args.get('hub.mode') == 'subscribe' and request.args.get('hub.verify_token') == 'zirakpur_verify_token_123':
        return request.args.get('hub.challenge'), 200
    return 'Forbidden', 403

# Lead aane pe yahan data aayega
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Lead received:", data)  # Logs me dikhega
    return 'OK', 200

if _name_ == '_main_':
    app.run()

app = Flask(_name_)

# Health check ke liye
@app.route('/')
def home():
    return "Webhook is running!", 200

# Meta webhook verification ke liye
@app.route('/webhook', methods=['GET'])
def verify():
    if request.args.get('hub.mode') == 'subscribe' and request.args.get('hub.verify_token') == 'zirakpur_verify_token_123':
        return request.args.get('hub.challenge'), 200
    return 'Forbidden', 403

# Lead aane pe yahan data aayega
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(data)  # Logs me dikhega
    return 'OK', 200

if _name_ == '_main_':
    app.run()
