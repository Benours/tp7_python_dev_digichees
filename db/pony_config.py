from pony.orm import *

# Define your database
db = Database()
# Connect to the database
db.bind(provider='mysql', host='localhost', user='root', passwd='root', port=3306, db='digichees')