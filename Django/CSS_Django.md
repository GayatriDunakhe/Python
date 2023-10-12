1. Add this in settings.py

```
STATIC_URL = 'static/'
import os
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
```


2. Create a static folder and add css/styles.css

myproject/
├── manage.py
├── myproject/ (Django project settings and configurations)
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── myapp1/ (Django app 1)
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── ...
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── myapp2/ (Django app 2)
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── ...
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── static/ (Directory for static files)
│   ├── css/
│   │   └── style.css
│   ├── js/
│   └── images/
├── templates/ (Directory for HTML templates)
│   ├── myapp1/
│   │   ├── template1.html
│   │   └── template2.html
│   ├── myapp2/
│   │   ├── template3.html
│   │   └── template4.html
│   └── base.html
└── venv/ (Virtual environment for Python dependencies - optional)


3.
``` HTML
*{% load static %}*
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
    <link rel="stylesheet" type="text/css" href="{% static 'css/styles.css' %}">
</head>
<body>
    <h1>fsdkfhjds </h1>
</body>
</html>

```

4.
```css
h1{
    color:red;
}
```