from src.connect import conn
from fastapi import APIRouter, HTTPException
import secrets

router = APIRouter()


# Get all weights
@router.get("/all")
async def get_all_weights():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM t_weight")
    weights = cursor.fetchall()
    return weights


# Get weight by id
@router.get("/get/{id}")
async def get_weight_by_id(id: int):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM t_weight WHERE id = %s", (id,))
    weight = cursor.fetchone()
    if weight:
        return weight
    else:
        raise HTTPException(status_code=404, detail="Weight not found")

# Get weight by values
@router.get("/get/{w_val}")
async def get_weight_by_w_val(w_val: float):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM t_weight WHERE w_val = %s", (w_val,))
    weight = cursor.fetchone()
    if weight:
        return weight
    else:
        raise HTTPException(status_code=404, detail="Weight not found")


# Add weight
@router.post("/add")
async def add_weight(w_val: float):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO t_weight (w_val) VALUES (%s)", (w_val,))
    conn.commit()
    return {"message": "Weight add successfully"}


# Update weight
@router.put("/update/{id}")
async def update_weight(id: int, w_val: float):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE t_weight SET w_val = %s WHERE id = %s",
        (w_val, id)
    )
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Weight not found")
    conn.commit()
    return {"message": "Weight update successfully"}


# Delete weight
@router.delete("/del/{id}")
async def delete_weight(id: int):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM t_weight WHERE id = %s", (id,))
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Weight not found")
    conn.commit()
    return {"message": "Weight delete successfully"}
