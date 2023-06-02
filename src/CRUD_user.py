from src.connect import conn
from fastapi import APIRouter, HTTPException
import secrets

router = APIRouter()


# Get all users
@router.get("/all")
async def get_all_users() -> list:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM t_user")
    users = cursor.fetchall()
    cursor.close()
    return users


# Get user with id
@router.get("/get/{id}")
async def get_user_by_id(id: int) -> list:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM t_user WHERE id = %s", (id,))
    user = cursor.fetchone()
    cursor.close()
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")

@router.get("/get/{email}")
async def get_user_by_email(email: str) -> list:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM t_user WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


# Add user
@router.post("/add")
async def add_user(email: str, password: str, salt: str, firstname: str = "", lastname: str = "") -> dict:
    cursor = conn.cursor()
    token = secrets.token_urlsafe(16)
    cursor.execute(
        "INSERT INTO t_user (email, password, salt, firstname, lastname, token) VALUES (%s, %s, %s, %s, %s, %s)",
        (email, password, salt, firstname, lastname, token)
    )
    conn.commit()
    cursor.close()
    return {"message": "User add successfully"}


# Update user with email, password and optional firstname and lastname and id to access
# Update user
@router.put("/update/{id}")
async def update_user(id: int, email: str, password: str, firstname: str = "", lastname: str = "") -> dict:
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE t_user SET email = %s, password = %s, firstname = %s, lastname = %s WHERE id = %s",
        (email, password, firstname, lastname, id)
    )
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="User not found")
    conn.commit()
    cursor.close()
    return {"message": "User update successfully"}


# Delete user
@router.delete("/del/{id}")
async def delete_user(id: int) -> dict:
    cursor = conn.cursor()
    cursor.execute("DELETE FROM t_user WHERE id = %s", (id,))
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="User not found")
    conn.commit()
    cursor.close()
    return {"message": "User delete successfully"}