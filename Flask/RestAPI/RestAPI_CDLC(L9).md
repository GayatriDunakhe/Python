# Gayatri Dunkahe
# Wave2-B1-Python

# Test your skill

1. How would you structure a Flask application to handle multiple endpoints, including "/api", and return custom messages for each endpoint?

- To structure a Flask application to handle multiple endpoints, including "/api," and return custom messages for each endpoint, we organize into separate routes for each endpoint.

```python
from flask import Flask, jsonify

app = Flask(__name__)

data = {
    '/api': 'Hello, Ram!',
    '/home': 'Welcome to Home Page',
    '/about': 'Welcome to About Page',
    '/gayatri': 'Gayatri Here!',
}

@app.route('/api', methods=['GET'])
def api():
    return jsonify({'msg': data['/api']})

@app.route('/home', methods=['GET'])
def home():
    return jsonify({'msg': data['/home']})

@app.route('/about', methods=['GET'])
def about():
    return jsonify({'msg': data['/about']})

@app.route('/gayatri', methods=['GET'])
def gayatri():
    return jsonify({'msg': data['/gayatri']})

if __name__ == '__main__':
    app.run(debug=True)

```