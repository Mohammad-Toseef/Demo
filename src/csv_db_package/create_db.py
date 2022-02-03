"""Script to create a database to the mysql server"""

from mysql.connector import connect, Error
import os

MYSQL_USER = os.getenv("USER")
MYSQL_PASSWORD = os.getenv('PASSWORD')
MYSQL_DB = "user_data"
MYSQL_HOST = os.getenv('HOST')

try:
    conn = connect(host=MYSQL_HOST, user=MYSQL_USER,
                   password=MYSQL_PASSWORD)
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE {MYSQL_DB}")
        print("Database is created")
except Error as e:
    print("Error while connecting to MySQL", e)
