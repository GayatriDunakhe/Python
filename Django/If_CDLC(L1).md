**Syntax:**
`{% if %}` template tag. 


**001_Example:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Voting Eligibility</title>
</head>
<body>
    {% if 19 > 18 %}
        <p>You are eligible to vote.</p>
    {% else %}
        <p>You are not eligible to vote.</p>
    {% endif %}
</body>
</html>
```

**002_Example:**
* app/templates/index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Voting Eligibility</title>
</head>
<body>
    <h1>Age: {{ age }}</h1>
    {% if age > 18 %}
        <p>You are eligible to vote.</p>
    {% else %}
        <p>You are not eligible to vote.</p>
    {% endif %}
</body>
</html>
```

* app_name/views.py

```python
from django.shortcuts import render
from .models import Infyx

def name_list(request):
    age = 21
    return render(request, 'index.html', {'age': age})
```