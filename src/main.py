from fastapi import FastAPI
from src.CRUD_user import router as user_router
from src.CRUD_object import router as object_router
from src.authentification.authtentification import router as authentification_router
import uvicorn

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(object_router, prefix="/object", tags=["object"])
app.include_router(authentification_router, prefix="/authentification", tags=["authentification"])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    '''uvicorn.run(app, host="0.0.0.0", port=8000)'''
    uvicorn.run(app, host="127.0.0.1", port=8282)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
