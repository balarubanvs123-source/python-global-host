

from flask import Flask, request

app = Flask(__name__)   # 🔥 VERY IMPORTANT

@app.route('/')
def home():
    return "API working!"

@app.route('/data', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        data = request.json
        print("Received:", data)
        return {"status": "POST success"}
    else:
        return "This is GET request"