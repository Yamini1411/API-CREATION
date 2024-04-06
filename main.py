from flask import Flask, request, jsonify
import json
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    data_set = {'page': 'home', 'message': 'successfully loaded the home page', 'timestamp': time.time()}
    return jsonify(data_set)

@app.route('/user/', methods=['GET'])
def request_page():
    user_query = request.args.get('user')
    if user_query:
        data_set = {'page': 'request', 'message': f'successfully got the request for {user_query}', 'timestamp': time.time()}
        return jsonify(data_set)
    else:
        return jsonify({'error': 'User parameter is missing.'}), 400

if __name__ == '__main__':
    app.run(port=7777)
