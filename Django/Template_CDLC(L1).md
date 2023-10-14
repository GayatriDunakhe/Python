# "Hello, World!" using a single HTML template, 

* You can modify the view to render an HTML template that contains the message. Here's the updated code:

1. Create a Django App:
   - Run the command to create a new Django app named "infy":

   ```bash
   python manage.py startapp infy
   ```

2. Define a View and Create an HTML Template:
   - Inside the `views.py` file of your "infy" app directory, create a view that renders an HTML template:

   ```python
   # infy/views.py
   from django.shortcuts import render

   def hello_world(request):
       return render(request, 'infy/hello.html')
   ```

3. Create an HTML Template:
   - Create a new directory named "templates" inside your "infy" app directory if it doesn't already exist.
   - Inside the "templates" directory, create an HTML file named "hello.html" with the following content:

   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>Hello, World!</title>
   </head>
   <body>
       <h1>Hello, World!</h1>
   </body>
   </html>
   ```

4. Create a URL Mapping:
   - In your "infy" app's `urls.py` file, define a URL pattern:

   ```python
   # infy/urls.py
   from django.urls import path
   from . import views

   urlpatterns = [
       path('hello/', views.hello_world, name='hello_world'),
   ]
   ```

5. Include the App URLs in the Project:
   - In your project's `urls.py` file, include the app's URLs:

   ```python
   # project/urls.py
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('infy.urls')),  # Include the app's URLs here
   ]
   ```

6. Run the Development Server:
   - Start the Django development server using the following command:

   ```bash
   python manage.py runserver
   ```

7. Access the "Hello, World!" View:
   - Open a web browser and go to http://localhost:8000/hello/ (or the URL you defined in step 4). You should see the "Hello, World!" message displayed in your browser using the HTML template.
