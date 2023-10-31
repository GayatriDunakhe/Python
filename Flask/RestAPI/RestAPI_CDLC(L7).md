# Gayatri Dunkahe
# Wave2-B1-Python

# Test

1. How you can create a REST API in Python using Flask that responds with the message "Hello, Ram!" when a POST request is made to the "/api" endpoint?

```python
from flask import Flask, jsonify

app = Flask(__name__)

data = {'message': 'Hello, Ram!'}

@app.route('/api', methods=['POST']) # gives Method not allowed
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

```

In this code it dosen't allow to access `Hello, Ram!` message on screen by `POST` method so I do 

```python
@app.route('/api', methods=['GET', 'POST'])
```