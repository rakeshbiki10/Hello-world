from flask import Flask, request, render_template
import psycopg2
import os

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        host='postgres',
        database='postgres',
        user='postgres',
        password='mysecretpassword')
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    zip_code = request.form['zipcode']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name, email, phone, zipcode) VALUES (%s, %s, %s, %s)',
                (name, email, phone, zip_code))
    conn.commit()
    cur.close()
    conn.close()

    return 'Success'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

