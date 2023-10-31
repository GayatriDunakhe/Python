## Flask_WTF(L3)

---

**Question 1:** 
Create a Flask-WTF form named `RegistrationForm` with the following fields:

1. `username` - a text field with a label "Username".
2. `email` - an email field with a label "Email Address".
3. `password` - a password field with a label "Password".
4. `confirm_password` - a password field with a label "Confirm Password".

Add validators to ensure that:
- All fields are required.
- The `email` is a valid email address.
- The `password` and `confirm_password` fields match.

Ans- 
```python
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey' 

class MyForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = StringField('password', validators=[DataRequired()])
    confirm_password = StringField('confirm_password', validators=[DataRequired(), EqualTo('password', message = "Password should be match!")])

    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        flash(f'Hello, {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
```

---

**Question 2:** 
In Flask, what purpose does `form.hidden_tag()` serve when used within a form rendered in a Jinja2 template, and why is it essential when dealing with Flask-WTF forms?
- In Flask, when we use `form.hidden_tag()` within a form rendered in a Jinja2 template, it serves an essential purpose when dealing with Flask-WTF forms. 
- This function generates hidden input fields in the HTML form, and it's required for security reasons and for ensuring that CSRF (Cross-Site Request Forgery) protection works correctly. 
- To prevent CSRF attacks, Flask-WTF generates a unique token for each form and includes it as a hidden input field in the form. 
- This token is used to verify that the form submission is legitimate and not coming from an external or malicious source.
- The form.hidden_tag() function generates the necessary hidden input fields for the CSRF token. 
- These hidden fields include the CSRF token itself and a timestamp, which is used for additional security. 
- When the form is submitted, the CSRF token is checked to ensure it matches the token stored on the server, and the timestamp is used to prevent token replay attacks.

---

**Question 3:** 
Using Flask-WTF, how would you implement a CSRF protection token in your form? Explain both the backend changes (in the Flask app) and the frontend changes (in the HTML template).
- To implement CSRF protection in Flask-WTF form, we need to make changes in both the Flask app (backend) and the HTML template (frontend). Here's how to do it step by step:
    - Backend -
        1. Import the necessary modules in Flask app:
        ```python
        from flask import Flask, render_template, request, redirect, url_for
        from flask_wtf import FlaskForm
        from wtforms import StringField, SubmitField
        from wtforms.validators import DataRequired
        from flask_wtf.csrf import CSRFProtect
        ```
        
        2. Create an instance of your Flask application and configure it with a secret key:
        ```python
        app = Flask(__name__)
        app.config['SECRET_KEY'] = 'your_secret_key_here'
        ```

        3. Initialize CSRF protection for app:
        ```python
        csrf = CSRFProtect(app)
        ```

        4. Define your form class, including any fields and validators you need. Make sure to include the CSRF token in your form class.
        ```python
        class MyForm(FlaskForm):
        name = StringField('Name', validators=[DataRequired()])
        submit = SubmitField('Submit')
        ```

        5. Create a route to render the form and handle form submissions:
        ```python
        @app.route('/my_form', methods=['GET', 'POST'])
        def my_form():
            form = MyForm()

            if form.validate_on_submit():
                # Process the form data here
                name = form.name.data
                # ...

            return render_template('my_form.html', form=form)
        ```
    - Frontend -
        1. In your HTML template (e.g., my_form.html), include the CSRF token using form.hidden_tag() within your form:
        ```python
        <form method="POST">
            {{ form.hidden_tag() }}
            {{ form.name.label }} {{ form.name(size=20) }}
            {{ form.submit() }}
        </form>
        ```
        The {{ form.hidden_tag() }} line generates the hidden input fields for the CSRF token and additional security data.