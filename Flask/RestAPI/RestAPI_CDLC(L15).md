# Gayatri Dunkahe
# Wave2-B1-Python

# Test Your Skill

Write code to create a Flask API with authentication, allowing access only to authorized users for specific endpoints.


```python
from flask import Flask, jsonify, request

app = Flask(__name__)

username = "gayatri"
password = "gayu"

def check_auth(auth):
    return auth.username == username and auth.password == password


@app.route('/api/auth', methods=['GET'])
def home():
    auth = request.authorization

    if not auth or not check_auth(auth):
        return jsonify(message='Authentication failed'), 401

    return jsonify(message="Welcome to the protected resource!")

if __name__ == '__main__':
    app.run(debug=True)

```