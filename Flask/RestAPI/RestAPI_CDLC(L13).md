# Gayatri Dunkahe
# Wave2-B1-Python

# Test your skills

Can you create a Flask REST API that accepts POST requests at "/add" to add two numbers and returns the result in JSON format?


```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    
    if 'num1' not in data or 'num2' not in data:
        return jsonify(error='Missing input data'), 400

    num1 = data['num1']
    num2 = data['num2']

    try:
        result = float(num1) + float(num2)
        return jsonify(result=result)

    except ValueError:
        return jsonify(error='Invalid input data'), 400

if __name__ == '__main__':
    app.run(debug=True)

```