from flask import Flask, jsonify
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
        'time': datetime.now().isoformat(),
        'hostname': socket.gethostname()
    }), 200

@app.route('/api/v1/healthz')
def healthz():
    return jsonify({
        'status': 'healthy'
    }), 200

if __name__ == '__main__':
    app.run()
