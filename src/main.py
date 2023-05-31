from fastapi import FastAPI
from src.CRUD_user import router as user_router
import uvicorn

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["user"])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
