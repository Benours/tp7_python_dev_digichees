import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=8889,
    user="root",
    password="root",
    database="digichees"
)
