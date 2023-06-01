from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
import bcrypt

from src.CRUD_user import add_user, get_user_by_email, delete_user

# Router creation to be able to add more route to the app.
router = APIRouter()

user_connected = []


# Class representing a connection formular recieved from the client. It contain an email, and a password.
class ConnectionItem(BaseModel):
    email: str
    password: str


# Class representing an action formular recieved from the client. It contain an token.
class TokenItem(BaseModel):
    token: str


# Class representing a register formular recieved from the client. It contain an email, a password, a lastname, and a firstname.
class RegisterItem(BaseModel):
    email: str
    password: str
    last_name: str
    first_name: str


# Return the hash of the given password and the given salt. The salt is encoded in binary if it's a string. The result hash is in binary format.
def get_password_hash(password, salt):
    p_encode = password.encode("utf-8")
    s_encode = ""
    if type(salt) == str:
        s_encode = salt.encode("utf-8")
    else:
        s_encode = salt

    # Hashing le motde passe
    hashed = bcrypt.hashpw(p_encode, s_encode)
    return hashed


# Route (POST) used to register a new user. A register formular must be given trought POST method.
# If a user with the chosen email already exist in base, then raise a 400 exception. Else the new user is added into the base.
@router.post("/register")
async def register(item: RegisterItem):
    try:
        user = await get_user_by_email(item.email)
    except Exception as error:
        salt = bcrypt.gensalt()
        await add_user(item.email, get_password_hash(item.password, salt), salt, item.first_name, item.last_name)

    else:
        raise HTTPException(status_code=400, detail="This email is already taken")



# Route (POST) used to unregister a new user. A token formular must be given trought POST method.
# If the token exist, and the user is connected, the user will be deleted from the base and from the connected users. Else raise a 400 exception.
@router.post("/unregister")
async def unregister(item: TokenItem):
    try:
        find = False
        for u in user_connected:
            if u[6] == item.token:
                find = True
                await delete_user(u[0])
                user_connected.remove(u)
                break
        if not find:
            raise HTTPException(status_code=400, detail="This token is invalid. Please login again")
    except Exception as error:
        raise HTTPException(status_code=400, detail="This token is invalid. Please login again")


# Route (POST) used to logout from the app. A token formular must be given trought POST method. If the token exist,
# and the user is connected, the user will be deleted from the connected users. Else raise a 400 exception.
@router.post("/logout")
async def logout(item: TokenItem):
    find = False
    for u in user_connected:
        if u[6] == item.token:
            find = True
            user_connected.remove(u)
            break
    if not find:
        raise HTTPException(status_code=400, detail="This token is invalid. Please login again")


# Route (POST) used to login to the app. A connection formular must be given trought POST method. If the user exist
# and the credentials are correct, and the user is not already connected, the user will be added to the list of
# connected users. A token will be returned. Else raise a 400 exception.

@router.post("/login")
async def login(item: ConnectionItem):
    try:
        user = await get_user_by_email(item.email)

        h = get_password_hash(item.password, user[3])
        if not h == user[2].encode("utf-8"):
            raise HTTPException(status_code=400, detail="Incorrect email or password")

    except Exception as error:
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    user_connected.append(user)
    return {'token': str(user[6])}
