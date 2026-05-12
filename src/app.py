from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
        'message': 'Hello World'
    }), 200

@app.route('/api/v1/healthz')
def healthz():
    return jsonify({
        'message': 'OK'
    }), 200

if __name__ == '__main__':
    app.run()
