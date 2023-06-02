import json

from src.CRUD_city import get_city
from src.CRUD_user import get_all_users
from src.CRUD_object import get_all_objects
from src.CRUD_weight import get_all_weights
from src.CRUD_conditioning import get_conditioning
from src.CRUD_weight_tag import get_weight_tag

from fastapi import APIRouter

app = APIRouter()

#pour impress, il faut que les données soit dans un fichier txt pour l'imprimer.
#pour différencier les fichier et ainsi avoir un historique, la date du jour est necessaire
#pour l'inserer dans le nom du fichier

#Impress_all permet de créer un fichier qui acceuille tout les get de chaque classe
@app.get("/impress_all")
async def impress_all(date: str):
    city = get_city()
    user = await get_all_users()
    objects = await get_all_objects()
    weight = await get_all_weights()
    conditioning = get_conditioning()
    weighttag = get_weight_tag()

    impress = str(city[:])+"\n"+ str(user)+"\n"+str( objects)+"\n"+ str(weight)+"\n"+ str(conditioning[:])+"\n"+ str(weighttag[:])

    file = open("../impress/impress_%s.txt" % date, "w")
    file.write(impress)
    file.close()
    return "Successful Impression"

#Impress_user permet de créer un fichier qui acceuille uniquement le get de user
@app.get("/impress_user")
async def impress_user(date: str):
    user = await get_all_users()

    impress =  str(user)

    file = open("../impress/impress_%s_user.txt" % date, "w")
    file.write(impress)
    file.close()
    return "Successful Impression"

#Impress_city permet de créer un fichier qui acceuille uniquement le get de city
@app.get("/impress_city")
def impress_city(date: str):
    city = get_city()

    impress =  str(city)

    file = open("../impress/impress_%s_city.txt" % date, "w")
    file.write(impress)
    file.close()
    return "Successful Impression"

#Impress_conditioning permet de créer un fichier qui acceuille uniquement le get de conditioning
@app.get("/impress_conditioning")
def impress_conditioning(date: str):
    conditioning = get_conditioning()

    impress =  str(conditioning)

    file = open("../impress/impress_%s_conditioning.txt" % date, "w")
    file.write(impress)
    file.close()
    return "Successful Impression"

#Impress_weight_tag permet de créer un fichier qui acceuille uniquement le get de weight_tag
@app.get("/impress_weight_tag")
def impress_weight_tag(date: str):
    weighttag = get_weight_tag()

    impress =  str(weighttag)

    file = open("../impress/impress_%s_weight_tag.txt" % date, "w")
    file.write(impress)
    file.close()
    return "Successful Impression"

#Impress_weights permet de créer un fichier qui acceuille uniquement le get de weights
@app.get("/impress_weights")
async def impress_weights(date: str):
    weight = await get_all_weights()

    impress =  str(weight)

    file = open("../impress/impress_%s_weight.txt" % date, "w")
    file.write(impress)
    file.close()
    return "Successful Impression"

#Impress_objects permet de créer un fichier qui acceuille uniquement le get de objects
@app.get("/impress_objects")
async def impress_objects(date: str):
    objects = await get_all_objects()

    impress =  str(objects)

    file = open("../impress/impress_%s_objects.txt" % date, "w")
    file.write(impress)
    file.close()
    return "Successful Impression"


