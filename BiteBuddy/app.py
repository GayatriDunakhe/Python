from flask import Flask,render_template

app = Flask(__name__)

@app.route('/homepage')
def homepage():
    head="Swiggy"
    tagline= "From India"
    return render_template("homepage.html",head=head,tagline=tagline)

app.run(debug=True)