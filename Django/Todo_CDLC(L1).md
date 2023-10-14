**Exercise: Building a Basic To-Do List Web App**

In this exercise, you will create a simple web application using Django that allows users to create and manage a to-do list.

1. First, make sure you have Django installed. If not, you can install it using pip:

```
pip install Django
```

2. Create a new Django project and app:

```
django-admin startproject todo_project
cd todo_project
python manage.py startapp todo
```

3. In the `todo` app directory, create a model for the to-do items. Edit the `models.py` file in the `todo` app as follows:

```python
from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

4. Create a migration for the model and apply it to the database:

```
python manage.py makemigrations
python manage.py migrate
```

5. Create a view, `views.py`, to display the to-do list and allow users to add new items:

```python
from django.shortcuts import render, redirect
from .models import TodoItem

def todo_list(request):
    items = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'items': items})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        TodoItem.objects.create(title=title)
    return redirect('todo_list')
```

6. Create two HTML templates. In the `todo` directory, create a `templates` folder if it doesn't exist already. Inside the `templates` folder, create two files:

`todo_list.html` (for displaying the to-do list):

```html
<!DOCTYPE html>
<html>
<head>
    <title>To-Do List</title>
</head>
<body>
    <h1>To-Do List</h1>
    <ul>
        {% for item in items %}
            <li>{{ item.title }}</li>
        {% endfor %}
    </ul>
    <form method="post" action="{% url 'add_todo' %}">
        {% csrf_token %}
        <label for="title">New Item:</label>
        <input type="text" id="title" name="title" required>
        <button type="submit">Add</button>
    </form>
</body>
</html>
```

7. Configure the URLs in the `todo` app. In the `urls.py` file of the `todo` app:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add/', views.add_todo, name='add_todo'),
]
```

8. Configure the project-level URLs. In the `urls.py` file of the project (`todo_project/urls.py`), add the app's URLs:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
]
```

9. Run the development server:

```
python manage.py runserver
```

10. Visit `http://localhost:8000/` in your web browser to use the to-do list application. You can add new to-do items and see them displayed on the list.

**Conclusion**
* This exercise helps you create a simple web application with Django, demonstrating basic CRUD (Create, Read, Update, Delete) operations for a to-do list.