from fastapi import APIRouter
from src.CRUD_weight_tag import create_weight_tag, get_weight_tag, update_weight_tag, delete_weight_tag
from src.connect import conn

app = APIRouter()


# Create a new conditioning with tag, weight and price
@app.post("/post")
def create_conditioning(tag: str, weight: float, price: float)-> str:
    cursor = conn.cursor()
    create_weight_tag(weight)
    weightTag = get_weight_tag()
    weight = list(weightTag[len(weightTag) - 1])[0]
    conditioningInsert = """INSERT INTO t_conditioning(
        tag,
        weightTag,
        price)
        VALUES (%s,%s,%s)"""
    cursor.execute(conditioningInsert, (tag, weight, price))
    conn.commit()
    return "Successful Creation"


# Get all the conditioning
@app.get('/getall')
def get_conditioning() -> list:
    cursor = conn.cursor()
    conditioningGet = """SELECT * FROM t_conditioning"""
    cursor.execute(conditioningGet)
    conditioning = cursor.fetchall()
    for c in conditioning:
        print(c)
    return conditioning

# Get one conditioning with id
@app.get('/getbyid')
def get_conditioning_by_id(id: int) -> list:
    cursor = conn.cursor()
    conditioningGet = "SELECT * FROM t_conditioning WHERE id=%s" % (id)
    cursor.execute(conditioningGet)
    conditioning = cursor.fetchall()
    return conditioning

# Modify conditioning information with tag, weight and price with id to access
@app.put("/put")
def update_conditioning(id: int, tag: str, weight: float, price: float)-> str:
    cursor = conn.cursor()
    condition=get_conditioning().copy()
    conditId= list(condition)[:][0].index(id)
    weightId=list(condition)[conditId][2]
    # print(weightId)
    update_weight_tag(weightId, weight)
    conditioningUpdate = "UPDATE t_conditioning SET tag=%s, price=%s WHERE id=%s"
    cursor.execute(conditioningUpdate, (tag, price, id))
    conn.commit()
    return "Successful Updated"

# Delete a conditioning
@app.delete("/delete")
def delete_conditioning(id: int)-> str:
    cursor = conn.cursor()
    condition = get_conditioning().copy()
    conditId = list(condition)[:][0].index(id)
    # print(conditId)
    weightId = list(condition)[conditId][2]
    # print(weightId)
    delete_weight_tag(weightId)
    conditioningDelete = "DELETE FROM t_conditioning WHERE id=%s" % (id)
    cursor.execute(conditioningDelete)
    conn.commit()
    return "Successful Deleted"


