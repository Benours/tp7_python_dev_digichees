import json

from src.CRUD_city import get_all_city
from src.CRUD_user import get_all_users
from src.CRUD_object import get_all_objects
from src.CRUD_weight import get_all_weights
from src.CRUD_conditioning import get_all_conditioning
from src.CRUD_weight_tag import get_all_weight_tag

from fastapi import APIRouter

app = APIRouter()


# To impress, the date needs to be place in a txt file.
# To differenciate files, and historize them, the date is necessary to insert it inside the file name.

# Impress_all allow to create a file hosting all the get_all methods of each class
@app.get("/impress_all")
async def impress_all(date: str):
    city = get_all_city()
    user = await get_all_users()
    objects = await get_all_objects()
    weight = await get_all_weights()
    conditioning = get_all_conditioning()
    weighttag = get_all_weight_tag()

    impress = str(city[:]) + "\n" + str(user) + "\n" + str(objects) + "\n" + str(weight) + "\n" + str(
        conditioning[:]) + "\n" + str(weighttag[:])

    file = open("../impress/impress_%s.txt" % date, "w")
    file.write(impress)
    file.close()
    return "Successful Impression"


# Impress_all allow to create a file hosting all the users in the database
@app.get("/impress_user")
async def impress_user(date: str):
    user = await get_all_users()

    impress = str(user)

    file = open("../impress/impress_%s_user.txt" % date, "w")
    file.write(impress)
    file.close()
    return "Successful Impression"


# Impress_all allow to create a file hosting all the cities in the database
@app.get("/impress_city")
def impress_city(date: str):
    city = get_all_city()

    impress = str(city)

    file = open("../impress/impress_%s_city.txt" % date, "w")
    file.write(impress)
    file.close()
    return "Successful Impression"


# Impress_all allow to create a file hosting all the conditioned object in the database
@app.get("/impress_conditioning")
def impress_conditioning(date: str):
    conditioning = get_all_conditioning()

    impress = str(conditioning)

    file = open("../impress/impress_%s_conditioning.txt" % date, "w")
    file.write(impress)
    file.close()
    return "Successful Impression"


# Impress_all allow to create a file hosting all the weight's tags in the database
@app.get("/impress_weight_tag")
def impress_weight_tag(date: str):
    weighttag = get_all_weight_tag()

    impress = str(weighttag)

    file = open("../impress/impress_%s_weight_tag.txt" % date, "w")
    file.write(impress)
    file.close()
    return "Successful Impression"


# Impress_all allow to create a file hosting all the weights in the database
@app.get("/impress_weights")
async def impress_weights(date: str):
    weight = await get_all_weights()

    impress = str(weight)

    file = open("../impress/impress_%s_weight.txt" % date, "w")
    file.write(impress)
    file.close()
    return "Successful Impression"


# Impress_all allow to create a file hosting all the objects in the database
@app.get("/impress_objects")
async def impress_objects(date: str):
    objects = await get_all_objects()

    impress = str(objects)

    file = open("../impress/impress_%s_objects.txt" % date, "w")
    file.write(impress)
    file.close()
    return "Successful Impression"
