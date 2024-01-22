# model/db.py
import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "web2_demo1",
    "port": 3307,
}

def get_db():
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()
    try:
        yield cursor
    finally:
        cursor.close()
        db.close()
