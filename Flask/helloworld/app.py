from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/home')
def hello_world():
    # return 'Hello, World!'
    return render_template("hello.html")

@app.route('/footer')
def footer():
    return render_template("footer.html")

app.run(debug = True)
