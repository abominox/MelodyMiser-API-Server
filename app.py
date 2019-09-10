#!/usr/bin/python3
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1/convert', methods=['POST'])
def convert_csv():
    return jsonify(request.json)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)