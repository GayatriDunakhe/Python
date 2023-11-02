## Microservices(L6)

11. Create a Flask route that sets a cookie named `user_id`.
```python
@app.route('/set-cookie/<user_id>')
def set_cookie(user_id):
    resp = make_response("Cookie Set")
    resp.set_cookie('user_id', user_id)
    return resp
```

12. Write a Flask route that reads a cookie named `session_id`.
```python
@app.route('/read-cookie')
def read_cookie():
    session_id = request.cookies.get('session_id')
    return f"Session ID: {session_id}"
```

13. How would you handle errors in Flask and return a custom error JSON response?
```python
@app.errorhandler(404)
def not_found(error):
    return jsonify(error="Not Found", message="The resource was not found"), 404
```

14. Create a route that accepts a file upload and saves it to the server.
```python
from flask import request, redirect, url_for
import os

UPLOAD_FOLDER = '/path/to/upload/folder'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file', filename=filename))
    return '''
    <!doctype html>
    <title>Upload a File</title>
    <h1>Upload File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
```

15. Implement a route that returns a JSON list of users from an in-memory list.
```python
users = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]

@app.route('/users')
def get_users():
    return jsonify(users)
```

16. Write a Flask application that uses environment variables for configuration.
```python
import os
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-secret-key')

@app.route('/')
def hello():
    return "Hello, World!"
```

17. Create a rate-limited route that allows only 5 requests per minute.
```python
from flask import Flask, request, jsonify
from flask_limiter import Limiter

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)

@app.route('/limited', methods=["GET"])
@limiter.limit("5 per minute")
def limited():
    return jsonify(success=True), 200
```

18. Implement a route `/reverse` that reverses the given string query parameter.
```python
@app.route('/reverse')
def reverse_string():
    original = request.args.get('string', '')
    reversed_str = original[::-1]
    return reversed_str
```

19. Write a route that returns the current server time in a JSON response.
```python
import datetime

@app.route('/time')
def get_time():
    current_time = datetime.datetime.now().isoformat()
    return jsonify(time=current_time)
```

20. Create a route that returns a static HTML file.
```python
@app.route('/static-page')
def static_page():
    return app.send_static_file('page.html')
```