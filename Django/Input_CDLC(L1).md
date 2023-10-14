# InputApp

1. First, make sure you have Django installed. If not, you can install it using pip:

```
pip install Django
```

2. Create a new Django project and app:

```
django-admin startproject age_checker_project
cd age_checker_project
python manage.py startapp age_checker
```

3. In the `age_checker` app directory, create a view, `views.py`, with the logic to check the age:

```python
from django.shortcuts import render

def check_age(request):
    if request.method == 'POST':
        age = int(request.POST['age'])
        if age >= 18:
            message = "You are eligible to vote!"
        else:
            message = "You are not eligible to vote."
        return render(request, 'age_checker/result.html', {'message': message})
    return render(request, 'age_checker/check_age.html')
```

4. Create two HTML templates. In the `age_checker` directory, create a `templates` folder if it doesn't exist already. Inside the `templates` folder, create two files:

`check_age.html` (for the input form):

```html
<!DOCTYPE html>
<html>
<head>
    <title>Age Checker</title>
</head>
<body>
    <h1>Age Checker</h1>
    <form method="post">
        {% csrf_token %}
        <label for="age">Enter your age:</label>
        <input type="number" id="age" name="age" required>
        <button type="submit">Check</button>
    </form>
</body>
</html>
```

`result.html` (for displaying the result):

```html
<!DOCTYPE html>
<html>
<head>
    <title>Age Checker - Result</title>
</head>
<body>
    <h1>Age Checker - Result</h1>
    <p>{{ message }}</p>
    <a href="{% url 'check_age' %}">Check another age</a>
</body>
</html>
```

5. Configure the URLs in the `age_checker` app. In the `urls.py` file of the `age_checker` app:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.check_age, name='check_age'),
]
```

6. Configure the project-level URLs. In the `urls.py` file of the project (`age_checker_project/urls.py`), add the app's URLs:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('age_checker.urls')),
]
```

7. Run the development server:

```
python manage.py runserver
```

8. Visit `http://localhost:8000/` in your web browser to use the age checker.
