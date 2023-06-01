from src.connect import conn
from fastapi import APIRouter, HTTPException
from src.CRUD_weight import add_weight, get_weight_by_w_val

router = APIRouter()


# Get all object
@router.get("/all")
async def get_all_objects():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM t_object")
    objects = cursor.fetchall()
    cursor.close()
    return objects


# Get object with id
@router.get("/get/{id}")
async def get_object_by_id(id: int):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM t_object WHERE id = %s", (id,))
    object = cursor.fetchone()
    cursor.close()
    if object:
        return object
    else:
        raise HTTPException(status_code=404, detail="Object not found")


# Add object with name, height, w_val (weight), description, price, stockline, shop and conditioning
# Add object
@router.post("/add")
async def add_object(name: str, height: int, w_val: float, description: str, price: int, stockline: int, shop: int, conditioning: int):
    cursor = conn.cursor()
    await add_weight(w_val)
    weight = await get_weight_by_w_val(w_val)
    cursor.execute(
        "INSERT INTO t_object (name, height, weight, description, price, stockline, shop, conditioning) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (name, height, weight[0], description, price, stockline, shop, conditioning)
    )
    conn.commit()
    cursor.close()
    return {"message": "Object add successfully"}


# Update object with name, height, w_val (weight), description, price, stockline, shop and conditioning and id to access
# Update object
@router.put("/update/{id}")
async def update_object(id: int, name: str, height: int, w_val: int, description: str, price: int, stockline: int, shop: int, conditioning: int):
    cursor = conn.cursor()
    await add_weight(w_val)
    weight = await get_weight_by_w_val(w_val)
    cursor.execute(
        "UPDATE t_object SET name = %s, height = %s, weight = %s, description = %s, price = %s, stockline = %s, shop = %s, conditioning = %s WHERE id = %s",
        (name, height, weight, description, price, stockline, shop, conditioning, id)
    )
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Object not found")
    conn.commit()
    cursor.close()
    return {"message": "Object update successfully"}


# Delete object
@router.delete("/del/{id}")
async def delete_object(id: int):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM t_object WHERE id = %s", (id,))
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Object not found")
    conn.commit()
    cursor.close()
    return {"message": "Object delete successfully"}