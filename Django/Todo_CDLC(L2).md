# Delete feature to your Django to-do list web app

1. Update the `views.py` file in the `todo` app to include a delete view:

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem

def todo_list(request):
    items = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'items': items})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        TodoItem.objects.create(title=title)
    return redirect('todo_list')

def delete_todo(request, item_id):
    item = get_object_or_404(TodoItem, pk=item_id)
    if request.method == 'POST':
        item.delete()
    return redirect('todo_list')
```

2. Update the `urls.py` file in the `todo` app to include a URL pattern for the delete view:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add/', views.add_todo, name='add_todo'),
    path('delete/<int:item_id>/', views.delete_todo, name='delete_todo'),  # Add this line
]
```

3. Update the `todo_list.html` template to include a delete button next to each to-do item:

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
            <li>
                {{ item.title }}
                <form method="post" action="{% url 'delete_todo' item.id %}">
                    <!-- {% csrf_token %} -->
                    <button type="submit">Delete</button>
                </form>
            </li>
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

4. Now, when you visit the to-do list page (`http://localhost:8000/`), you will see a "Delete" button next to each item. Clicking the "Delete" button will remove the corresponding item from the to-do list.