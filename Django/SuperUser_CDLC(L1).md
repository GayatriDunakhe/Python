
# How to create super user in Django?

* In Django, a superuser is a user with administrative privileges who has access to the Django admin interface and can perform tasks like managing other users, creating and editing database records, and more. To create a superuser in Django, you can follow these steps:

1. Create a Django project and navigate to its root directory in your terminal.

2. Run the following command to create a superuser:

```bash
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
```

3. You'll be prompted to enter the following information for the superuser:

   - Username: This will be the username for the superuser. You can choose any username you like.
   - Email address: Provide an email address for the superuser.
   - Password: Enter a secure password for the superuser. Django will prompt you to confirm the password by typing it again.

4. After entering the required information, the superuser will be created, and you will see a confirmation message similar to the following:

   ```
   Superuser created successfully.
   ```

Now, you can use the superuser credentials to log in to the Django admin interface and manage your Django application. To access the admin interface, follow these steps:

1. Start your Django development server if it's not already running:

```bash
python manage.py runserver
```

2. Open a web browser and navigate to the admin login page, typically located at `http://localhost:8000/admin/`.

3. Log in using the username and password you provided when creating the superuser.

Once logged in, you'll have access to the Django admin interface and can begin managing your application's data and users with administrative privileges.

Keep in mind that it's important to choose strong and secure passwords for superusers and other users with administrative access to your Django application to help protect your site from unauthorized access.