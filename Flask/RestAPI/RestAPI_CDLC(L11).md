# Gayatri Dunkahe
# Wave2-B1-Python

# Test your skill

1. Implement error handling in a Flask REST API so that it returns a custom error message when an invalid endpoint is accessed.

```python
from flask import Flask, jsonify

app = Flask(__name__)

data = {'message': 'Hello, Ram!'}

custom_error = {
    'error': 'The route you looking for is not availabe!' 
}

@app.route('/api', methods=['POST'])
def post_data():
    return jsonify(data)

@app.errorhandler(404)
def handle_not_found_error(error):
    return jsonify(custom_error), 404

if __name__ == '__main__':
    app.run(debug=True)

```