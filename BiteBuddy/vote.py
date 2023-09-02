from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def score():
    age=20
    return render_template("voting.html",age=age)

app.run(debug=True)