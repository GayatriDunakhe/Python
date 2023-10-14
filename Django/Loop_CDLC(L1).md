**Objective**
To create a loop in a Django HTML template to display numbers from 1 to 10, 
you can use the `{% for %}` template tag. 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Loop in Django HTML</title>
</head>
<body>
    <ul>
        {% for number in numbers %}
            <li>{{ number }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

In your Django view, you'll need to pass a list of numbers from 1 to 10 to the template context. Here's an example of how you can do this in a Django view:

```python
from django.shortcuts import render

def your_view(request):
    numbers = range(1, 11)
    return render(request, 'your_template.html', {'numbers': numbers})
```

In this code:

1. We define a list of numbers from 1 to 10 using the `range` function.
2. We pass this list to the template context as the variable `numbers`.
3. In the HTML template, we use the `{% for %}` template tag to loop through each number in the `numbers` list and display it as list items.
