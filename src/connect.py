import mysql.connector

# Connect to database
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="digichees"
)
