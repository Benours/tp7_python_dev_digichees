from fastapi import FastAPI
from src.CRUD_user import router as user_router
from src.CRUD_object import router as object_router
from src.CRUD_weight import router as weight_router
from src.CRUD_weight_tag import app as weight_tag_router
from src.CRUD_city import app as city_router
from src.CRUD_conditioning import app as conditioning_router
from src.authentification.authtentification import router as authentification_router
import uvicorn

# Create the swagger
app = FastAPI()

# Include all routers in app
app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(object_router, prefix="/object", tags=["object"])
app.include_router(weight_router, prefix="/weight", tags=["weight"])
app.include_router(weight_tag_router, prefix="/weightTag", tags=["weightTag"])
app.include_router(city_router, prefix="/city", tags=["city"])
app.include_router(conditioning_router, prefix="/conditioning", tags=["conditioning"])
app.include_router(authentification_router, prefix="/authentification", tags=["authentification"])

# Launch uvicorn and access to swagger
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
from src.Impress import app as impress_router
app.include_router(impress_router, prefix="/impress", tags=["impress"])