from flask import Flask,render_template

app = Flask(__name__)

@app.route('/login')
def login():
    return "I am in login page"

@app.route('/signup')
def signup():
    return "I am in Signup page"

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

app.run(debug=True)