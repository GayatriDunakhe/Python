from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Calculator App!'

@app.route('/add')
def add():
    result = 25 + 5
    return f'The result of 25 + 5 is {result}'

@app.route('/sub')
def subtract():
    result = 25 - 5
    return f'The result of 25 - 5 is {result}'

@app.route('/mul')
def multiply():
    result = 25 * 5
    return f'The result of 25 * 5 is {result}'

@app.route('/div')
def divide():
    result = 25 / 5
    return f'The result of 25 / 5 is {result}'

app.run(debug=True)
