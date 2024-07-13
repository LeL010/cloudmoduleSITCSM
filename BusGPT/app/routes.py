from flask import render_template, request, jsonify
from app import app
import pymysql

# RDS settings
RDS_HOST = "your-rds-endpoint"
RDS_USER = "admin"
RDS_PASSWORD = "P@ssword1234"
RDS_DB = "BusGPT_Db"

def get_db_connection():
    connection = pymysql.connect(
        host=RDS_HOST,
        user=RDS_USER,
        password=RDS_PASSWORD,
        database=RDS_DB,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.json
        name = data['name']
        email = data['email']
        message = data['message']

        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, email, message))
            connection.commit()

        connection.close()
        return jsonify({"message": "Contact information submitted successfully"}), 201
    
    return render_template('contact.html')