from flask import Flask, jsonify, render_template, url_for, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
app = Flask(__name__)

def opendb():
    global mydb, mycursor
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='flaskdb'
    )
    mycursor = mydb.close()

def closedb():
    global mydb, mycursor
    mycursor.close()
    mydb.close()

@app.route('/')
def view():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)