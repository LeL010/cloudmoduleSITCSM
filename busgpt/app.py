from flask import Flask, render_template, request, redirect
import pymysql
from config import DB_CONFIG

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=DB_CONFIG['host'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        database=DB_CONFIG['database'],
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, email, message))
        connection.commit()
        connection.close()

        return redirect('/')

    return render_template('contact_us.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
