from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def score():
    score=50
    return render_template("score.html",score=score)

app.run(debug=True)