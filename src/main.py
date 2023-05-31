from fastapi import FastAPI
from src.CRUD_user import router as user_router
from src.CRUD_object import router as object_router
import uvicorn

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(object_router, prefix="/object", tags=["object"])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
