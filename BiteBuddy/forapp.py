from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    stud=["Alex","Ram","Krish"]
    return render_template("for.html",stud=stud)

app.run(debug=True)