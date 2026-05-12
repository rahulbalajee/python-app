from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
        'name': 'John Doe',
        'age': 30,
        'email': 'john.doe@example.com'
    }), 200

if __name__ == '__main__':
    app.run()
