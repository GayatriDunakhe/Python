from flask import Flask, request, jsonify, Blueprint, make_response
from flask_basicauth import BasicAuth
import os
from flask_limiter import Limiter
import datetime

app = Flask(__name__)

# Simple in-memory store for tasks
tasks = []

app.config['BASIC_AUTH_USERNAME'] = 'gd'
app.config['BASIC_AUTH_PASSWORD'] = '12345'

basic_auth = BasicAuth(app)

@app.route('/protected')
@basic_auth.required
def protected_route():
    return "This route is protected with basic authentication."

@app.route('/')
def hello_world():
    log_user_agent()
    return 'Hello, World!'

@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return f"Hello, {name}!"

@app.route('/checkage/<int:age>', methods=['GET'])
def checkAge(age):
    if age > 18:
        return "adult"
    else:
        return "minor"

@app.route('/jsondata', methods=['POST'])
def jsdondata():
    data = request.get_json()
    return jsonify(data)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json.get('task')
    if not task:
        return jsonify({"error": "Task not provided"}), 400

    tasks.append(task)
    return jsonify({"message": "Task added!"}), 201

@app.route('/useragent')
def get_user_agent():
    user_agent = request.headers.get('User-Agent')
    return f'User Agent: {user_agent}'

@app.route('/add')
def adding():
    a = int(request.args.get('a', 2))
    b = int(request.args.get('b', 4))
    return str(a + b)

categories = Blueprint('categories', __name__)

@categories.route('/')
def category_list():
    return "List of categories"

app.register_blueprint(categories, url_prefix='/categories')

notes = []

@app.route('/notes', methods=['GET', 'POST'])
def manage_notes():
    if request.method == 'GET':
        return jsonify(notes)
    else:
        notes.append(request.json)
        return "Note added!", 201

@app.before_request
def log_user_agent():
    print(f"{request.method} {request.path} - User Agent: {request.headers.get('User-Agent')}")

@app.route('/set-cookie/<user_id>')
def set_cookie(user_id):
    resp = make_response("Cookie Set")
    resp.set_cookie('user_id', user_id)
    return resp

@app.route('/read-cookie')
def read_cookie():
    session_id = request.cookies.get('session_id')
    return f"Session ID: {session_id}"

@app.errorhandler(404)
def not_found(error):
    return jsonify(error="Not Found", message="The resource was not found"), 404

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

users = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]

@app.route('/users')
def get_users():
    return jsonify(users)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-secret-key')

@app.route('/env')
def hello():
    return "Hello, World!"

# limiter = Limiter(app, key_func=get_remote_address)

# @app.route('/limited', methods=["GET"])
# @limiter.limit("5 per minute")
# def limited():
#     return jsonify(success=True), 200


@app.route('/reverse')
def reverse_string():
    original = request.args.get('string', '')
    reversed_str = original[::-1]
    return reversed_str

@app.route('/time')
def get_time():
    current_time = datetime.datetime.now().isoformat()
    return jsonify(time=current_time)

@app.route('/static-page')
def static_page():
    return app.send_static_file('page.html')

if __name__ == '__main__':
    app.run(port=5000)
