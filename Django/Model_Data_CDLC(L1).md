# Display the data from your Django model in an HTML template, 

**1. Create a View:**

In your Django app, create a view function that retrieves the data from the Name model and passes it to an HTML template. In your app's views.py file (names/views.py), add the following code:

```python
from django.shortcuts import render
from .models import Infyx

def name_list(request):
    names = Name.objects.all()
    return render(request, 'names/name_list.html', {'names': names})
```

**2. Create an HTML Template:**

Create an HTML template to display the data. In your app's templates/names directory, create a new file named "name_list.html" with the following code:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Name List</title>
</head>
<body>
    <h1>Name List</h1>
    <ul>
        {% for name in names %}
            <li>{{ name.first_name }} {{ name.last_name }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```


**3. Access the Data in the Browser:**

Start the development server:

```bash
python manage.py runserver
```

You can now access the list of names in your browser by navigating to http://localhost:8000/names/. This URL should display the names stored in your database using the HTML template.

