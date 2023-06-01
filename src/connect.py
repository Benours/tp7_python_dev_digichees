import mysql.connector

# Connect to database
conn = mysql.connector.connect(
    host="localhost",
    port=8889,
    user="root",
    password="root",
    database="digichees"
)
