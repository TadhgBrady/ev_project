import json
import os
from flask import Flask, request, jsonify
import redis
HOST = os.environ.get('REDIS_HOST', 'localhost')
PORT = os.environ.get('REDIS_PORT', 6379)
PASWORD = os.environ.get('REDIS_PASSWORD', 'password')
DB = os.environ.get('REDIS_DB', 0)
app = Flask(__name__)
r = redis.Redis(host=HOST, port=PORT, password=PASWORD, db=DB)

@app.route('/home')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)