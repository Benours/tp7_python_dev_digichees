from fastapi import APIRouter

from src.connect import conn

app = APIRouter()

# Create a new tag weight with tagvalues (weight)
@app.post("/post")
def create_weight_tag(tagValues: float)-> str:
    cursor = conn.cursor()
    weightTagInsert = """INSERT INTO t_weight_tag (tagValues) VALUES (%s)""" % tagValues
    cursor.execute(weightTagInsert)
    conn.commit()
    return "Successful Creation"

# Get all the tag weight
@app.get('/getall')
def get_weight_tag() -> list:
    cursor = conn.cursor()
    weightTagGet = """SELECT * FROM t_weight_tag"""
    cursor.execute(weightTagGet)
    city = cursor.fetchall()
    for c in city:
        print(c)
    return city

# Get a tag weight with id
@app.get('/getbyid')
def get_weight_tag_by_id(id: int) -> list:
    cursor = conn.cursor()
    weightTagGet = "SELECT * FROM t_weight_tag WHERE id=%s" % (id)
    cursor.execute(weightTagGet)
    weightTag = cursor.fetchall()
    return weightTag

# Modify a tag weight with tagvalues (weight) and id to access
@app.put("/put")
def update_weight_tag(id: int, tagValues: float)-> str:
    cursor = conn.cursor()
    weightTagUpdate = "UPDATE t_weight_tag SET tagValues=%s WHERE id=%s" % (tagValues, id)
    cursor.execute(weightTagUpdate)
    conn.commit()
    return "Successful Updated"

# Delete a tag weight
@app.delete("/delete")
def delete_weight_tag(id: int)-> str:
    cursor = conn.cursor()
    weightTagDelete = "DELETE FROM t_weight_tag WHERE id=%s" % (id)
    cursor.execute(weightTagDelete)
    conn.commit()
    return "Successful Deleted"
