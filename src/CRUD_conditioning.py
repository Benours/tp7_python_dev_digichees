from fastapi import APIRouter
from src.CRUD_weight_tag import createWeightTag, getWeightTag, updateWeightTag, deleteWeightTag
from src.connect import conn

app = APIRouter()


# on import fastapi pour swagger et conn qui est dans connect.py qui
# permet la connection avec la base de donnée

@app.post("/post")
def createConditioning(tag: str, weight: float, price: float):
    # on doit créer un nouvelle ville pour cela on a un l'id qui est auto incrémentable
    # nous avons plus qu'a créer un cursor pour mettre une requete sql pour inserer les données
    cursor = conn.cursor()
    createWeightTag(weight)
    weightTag = getWeightTag()
    weight = list(weightTag[len(weightTag) - 1])[0]
    conditioningInsert = """INSERT INTO t_conditioning(
        tag,
        weight,
        price)
        VALUES (%s,%s,%s)"""
    cursor.execute(conditioningInsert, (tag, weight, price))
    conn.commit()
    return "Successful Creation"


@app.get('/getall')
def getConditioning():
    # pour le get le cursor aura pour requete sql un select * pour tout avoir dans la table t_conditioning
    cursor = conn.cursor()
    conditioningGet = """SELECT * FROM t_conditioning"""
    cursor.execute(conditioningGet)
    conditioning = cursor.fetchall()
    for c in conditioning:
        print(c)
    return conditioning

@app.get('/getbyid')
def getConditioningById(id: int):
    # pour le get le cursor aura pour requete sql un select * pour tout avoir dans la table t_conditioning
    cursor = conn.cursor()
    conditioningGet = "SELECT * FROM t_conditioning WHERE id=%s" % (id)
    cursor.execute(conditioningGet)
    conditioning = cursor.fetchall()
    return conditioning

@app.put("/put")
def updateConditioning(id: int, tag: str, weight: float, price: float):
    # pour le update, nous allons modifier les parametres. mais pour cela il faut
    # renseigner l'id qui est unique puisque qu'il va être liée au client
    cursor = conn.cursor()
    condition=getConditioning().copy()
    conditId= list(condition)[:][0].index(id)
    weightId=list(condition)[conditId][2]
    # print(weightId)
    updateWeightTag(weightId, weight)
    conditioningUpdate = "UPDATE t_conditioning SET tag=%s, price=%s WHERE id=%s"
    cursor.execute(conditioningUpdate, (tag, price, id))
    conn.commit()
    return "Successful Updated"


@app.delete("/delete")
def deleteConditioning(id: int):
    # pour le delete, le cursor va avoir la requete sql pour supprimer la donnée
    # lié à l'id associé
    cursor = conn.cursor()
    condition = getConditioning().copy()
    conditId = list(condition)[:][0].index(id)
    # print(conditId)
    weightId = list(condition)[conditId][2]
    # print(weightId)
    deleteWeightTag(weightId)
    conditioningDelete = "DELETE FROM t_conditioning WHERE id=%s" % (id)
    cursor.execute(conditioningDelete)
    conn.commit()
    return "Successful Deleted"


