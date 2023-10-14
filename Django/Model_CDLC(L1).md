# Model

Create a  model for storing first names and last names and then add the ability to register them to an admin. 

1. Define the Model:
   In your newly created app's models.py file (infy/models.py), define the model for storing first names and last names:

   ```python
   from django.db import models

   class Infyx(models.Model):
       first_name = models.CharField(max_length=50)
       last_name = models.CharField(max_length=50)

       def __str__(self):
           return f"{self.first_name} {self.last_name}"
   ```

2. Register the Model in the Admin Panel:
   In your app's admin.py file (infy/admin.py), register the Name model to make it accessible in the Django admin panel:

   ```python
   from django.contrib import admin
   from .models import Infyx

   admin.site.register(Infyx)
   ```

3. Create and Apply Migrations:
   Create and apply migrations to update the database schema with the new Name model:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create a Superuser:
   To access the admin panel, create a superuser account using the following command:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create a username, email, and password for the admin user.

5. Run the Development Server:
   Start the development server:

   ```bash
   python manage.py runserver
   ```

   You can now access the Django admin panel by going to http://localhost:8000/admin and logging in with the superuser credentials.
