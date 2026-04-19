from flask import Flask, jsonify, request, render_template_string
from flask_cors import CORS
import requests
import random
import string
import time

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "SULAV API RUNNING"

@app.route('/generate', methods=['GET'])
def generate():
    name = request.args.get('name', 'SULAV')
    password = request.args.get('password', 'SULAV')

    uid = str(random.randint(100000000, 999999999))
    final_pass = password + "_" + ''.join(random.choice(string.ascii_uppercase+string.digits) for _ in range(4))

    return jsonify({
        "status": "success",
        "account": {
            "name": name,
            "uid": uid,
            "password": final_pass
        }
    })

# Vercel entry
app = app
