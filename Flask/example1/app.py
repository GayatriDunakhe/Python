from flask import Flask, render_template, request
import sqlite3data = show_data()

app = Flask(__name__, static_url_path='/static')

@app.route('/home')
def home():
    create_table()
    # delete_data(102)
    # update_data(102)

    data = show_data()

    cname = "GD"
    return render_template('home.html', cname=cname , data=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/insert', methods=['POST'])
def insert():
    user_id = request.form['id']
    user_name = request.form['username']
    user_emil = request.form['email']
    insert_data(user_id, user_name, user_emil)
    return "Data Added!"


def create_table():
    conn = sqlite3.connect('infy.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emp(
                   id INTEGER,
                   username TEXT,
                   email TEXT

        )
    """)
    conn.commit()
    conn.close()


def insert_data(user_id, user_name, user_emil):
    conn = sqlite3.connect('infy.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO emp(id,username,email) VALUES (?,?,?)",
    (user_id, user_name, user_emil))
    
    conn.commit()
    conn.close()

def delete_data(empid):
    conn = sqlite3.connect('infy.db')
    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM emp WHERE id ={empid}")

    conn.commit()
    conn.close()

def update_data(empid):
    conn = sqlite3.connect('infy.db')
    cursor = conn.cursor()

    user_name = "Rohan"

    cursor.execute(f"UPDATE emp SET username = '{user_name}' WHERE id = {empid}")

    conn.commit()
    conn.close()

def show_data():
    conn = sqlite3.connect('infy.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM emp")

    data = cursor.fetchall()

    conn.close()
    return data    

app.run(debug=True, port=6001)