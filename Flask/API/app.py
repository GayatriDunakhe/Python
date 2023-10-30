from flask import Flask, jsonify, request

app = Flask(__name__)

data = {
    '/api': 'Hello, Ram!',
    '/home': 'Welcome to Home Page',
    '/about': 'Welcome to About Page',
    '/gayatri': 'Gayatri Here!',
}

custom_error = {
    'error': 'The route you are looking for is not availabe!' 
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

@app.errorhandler(404)
def handle_not_found_error(error):
    return jsonify(custom_error), 404

@app.route('/add', methods=['GET', 'POST'])
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


username = "gayatri"
password = "gayu"

def check_auth(auth):
    return auth.username == username and auth.password == password

@app.route('/auth', methods=['GET'])
def authentication():
    auth = request.authorization

    if not auth or not check_auth(auth):
        return jsonify(message='Authentication failed'), 401

    return jsonify(message="Welcome to the protected resource!")

if __name__ == '__main__':
    app.run(debug=True)
