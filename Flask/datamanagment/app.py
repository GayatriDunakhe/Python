from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__, static_url_path='/static')

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/insert', methods=['POST'])
def insert():
    user_id = request.form['id']
    user_name = request.form['username']
    user_emil = request.form['email']

    insert_data(user_id, user_name, user_emil)

    return render_template('add.html')

def insert_data(user_id, user_name, user_emil):
    conn=connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO emp(id,username,email) VALUES (?,?,?)",
    (user_id,user_name,user_emil))
    
    conn.commit()
    conn.close()

@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/remove', methods=['POST'])
def remove(id):
    user_id = request.form['id']
    user_id =id

    delete_data(user_id)

    return render_template('delete.html')


def delete_data(user_id):
    conn = connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM emp WHERE id=?",(user_id,))

    conn.commit()
    conn.close()

@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/updatedata', methods=['POST'])
def updatedata():
    user_id = request.form['id']
    user_name = request.form['username']
    user_emil = request.form['email']

    update_data(user_id, user_name, user_emil)

    return render_template('update.html')

def update_data(user_id,user_name,user_emil):
    conn = connection()
    cursor = conn.cursor()
    
    cursor.execute("UPDATE emp SET username=?, email=? WHERE id=?",(user_name,user_emil,user_id))
    
    conn.commit()
    conn.close()

@app.route('/display')
def display():
    data = show_data()
    return render_template('display.html', data=data)

def connection():
    conn=sqlite3.connect('infy.db')
    return conn

def create_table():
    conn=connection()
    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS emp(id INTEGER,username TEXT,email TEXT)
    """)

    conn.commit()
    conn.close()

def show_data():
    conn = sqlite3.connect('infy.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM emp")

    data = cursor.fetchall()

    conn.close()
    return data    

if __name__ == '__main__':
    connection()
    create_table()
    # insert_table()
    # update()
    app.run(debug=True)