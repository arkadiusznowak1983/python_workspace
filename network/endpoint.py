from flask import Flask, jsonify
import time

app = Flask(__name__)


@app.route('/endpoint', methods=['GET'])
def get_tasks():
    return jsonify({'resp': time.time()})

if __name__ == '__main__':
    app.run(debug=True)
