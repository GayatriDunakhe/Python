## Microservices(L5)

1. Write a basic Flask application that returns "Hello, World!" on the root route.
```python
from flask import Flask

app = Flask(__name)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()

```
  
2. Add a route `/greet/<name>` to greet a user by their name.
```python
@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return f"Hello, {name}!"
```

3. Write a Flask route that accepts a query parameter `age` and returns whether the user is an adult or minor.
```python
@app.route('/checkage/<int:age>', methods=['GET'])
def checkAge(age):
    if age > 18:
        return "adult"
    else:
        return "minor"
```

4. Create a Flask route that accepts POST requests and returns the JSON data received.
```python
@app.route('/jsondata', methods=['POST'])
def jsdondata():
    data = request.get_json()
    return jsonify(data)
```

5. How would you implement basic authentication for a Flask route?
```python
# pip install Flask-BasicAuth

from flask_basicauth import BasicAuth

app.config['BASIC_AUTH_USERNAME'] = 'gd'
app.config['BASIC_AUTH_PASSWORD'] = '12345'

basic_auth = BasicAuth(app)

@app.route('/protected')
@basic_auth.required
def protected_route():
    return "This route is protected with basic authentication."
```

6. Write a route that returns the user agent of the request.
```python
@app.route('/useragent')
def get_user_agent():
    user_agent = request.headers.get('User-Agent')
    return f'User Agent: {user_agent}'
```

7. Implement a route `/add` that takes two query parameters, `a` and `b`, and returns their sum.
```python
@app.route('/add')
def adding():
    a = int(request.args.get('a', 2))
    b = int(request.args.get('b', 4))
    return str(a + b)
```

8. Use Flask's `Blueprint` to organize routes related to `products`.
```python
categories = Blueprint('categories', __name__)

@categories.route('/')
def category_list():
    return "List of categories"

app.register_blueprint(categories, url_prefix='/categories')
```

9. Create a simple REST API for CRUD operations on a `Todo` entity.
```python
notes = []

@app.route('/notes', methods=['GET', 'POST'])
def manage_notes():
    if request.method == 'GET':
        return jsonify(notes)
    else:
        notes.append(request.json)
        return "Note added!", 201
```

10. Write middleware in Flask that logs each request's method and path.
```python
@app.before_request
def log_user_agent():
    print(f"{request.method} {request.path} - User Agent: {request.headers.get('User-Agent')}")
```