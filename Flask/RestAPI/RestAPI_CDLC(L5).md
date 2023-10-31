# Gayatri Dunkahe
# Wave2-B1-Python

# Test

1. How you can create a REST API in Python using Flask that responds with the message "Hello, Ram!" when a GET request is made to the "/api" endpoint?

```python
from flask import Flask, jsonify

app = Flask(__name__)

data = {'message': 'Hello, Ram!'}

@app.route('/api', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
```