from fastapi import FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pony.orm import db_session
from pydantic import BaseModel
from db.pony_config import db as database
import db.pony_entitites
import bcrypt

app = FastAPI()

class ConnectionItem(BaseModel):
    email: str
    password: str

def getPasswordHash(password, salt):

    password = password.encode("utf-8")
    # Adding the salt to password
    #salt = bcrypt.gensalt()
    # Hashing the password
    hashed = bcrypt.hashpw(password,salt)
    return hashed

@db_session
def selectAllUsers():
    users = database.select("* FROM t_user")
    return users

@db_session
def selectUser(email):
    u = database.select(f"* FROM t_user WHERE email = '{email}'")
    return u


@app.post("/token")
def login(item: ConnectionItem):
    print("je suis ici")
    h = getPasswordHash(item.password)
    userList = selectUser(item.email)
    if len(userList) == 0:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    print("je suis la")
    h = getPasswordHash(item.password)
    print(h)
    if not h == userList[0].password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return  "{token='{0}'}".format(item.token)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8282)
