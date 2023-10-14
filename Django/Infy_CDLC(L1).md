1. **Create a Django App**:

   ```bash
   python manage.py startapp infy
   ```

2. **Define a View**: 
* Inside the `views.py` file of your "infy" app directory, create a simple "Hello, World!" view:
* infy/view

   ```python
   from django.http import HttpResponse

   def hello_world(request):
       return HttpResponse("Hello, World!")
   ```

3. **Create a URL Mapping**: In your "infy" app's `urls.py` file, define a URL pattern:
* infy/urls.py
* Create one file file is not there.

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('hello/', views.hello_world, name='hello_world'),
   ]
   ```

4. **Include the App URLs in the Project**: 
* In your project's `urls.py` file, include the app's URLs:

   ```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('infy.urls')),  # Include the app's URLs here
   ]
   ```

5. **Run the Development Server**:

   ```bash
   python manage.py runserver
   ```

6. **Access the "Hello, World!" View**: 
* Open a web browser and go to http://localhost:8000/hello/ (or the URL you defined in step 3). 
* You should see "Hello, World!" displayed in your browser.
* Now, your Django app named "infy" will display "Hello, World!" when you access the specified URL.