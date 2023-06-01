from fastapi import APIRouter

from src.connect import conn

app = APIRouter()

@app.post("/post")
def createWeightTag(tagValues: float):
    #on doit créer un nouvelle ville pour cela on a un l'id qui est auto incrémentable
    #nous avons plus qu'a créer un cursor pour mettre une requete sql pour inserer les données
    cursor = conn.cursor()
    weightTagInsert = """INSERT INTO t_weight_tag (tagValues) VALUES (%s)""" % tagValues
    cursor.execute(weightTagInsert)
    conn.commit()
    return "Successful Creation"


@app.get('/getall')
def getWeightTag():
    #pour le get le cursor aura pour requete sql un select * pour tout avoir dans la table t_weight_tag
    cursor = conn.cursor()
    weightTagGet = """SELECT * FROM t_weight_tag"""
    cursor.execute(weightTagGet)
    city = cursor.fetchall()
    for c in city:
        print(c)
    return city

@app.get('/getbyid')
def getWeightTagById(id: int):
    #pour le get le cursor aura pour requete sql un select * pour tout avoir dans la table t_weight_tag
    cursor = conn.cursor()
    weightTagGet = "SELECT * FROM t_weight_tag WHERE id=%s" % (id)
    cursor.execute(weightTagGet)
    weightTag = cursor.fetchall()
    for w in weightTag:
        print(w)
    return weightTag

@app.put("/put")
def updateWeightTag(id: int, tagValues: float):
    #pour le update, nous allons modifier le parametre: valeur(tagValues). mais pour cela il faut
    #renseigner l'id qui est unique puisque qu'il va être liée au client
    cursor = conn.cursor()
    weightTagUpdate = "UPDATE t_weight_tag SET tagValues=%s WHERE id=%s" % (tagValues, id)
    cursor.execute(weightTagUpdate)
    conn.commit()
    return "Successful Updated"


@app.delete("/delete")
def deleteWeightTag(id: int):
    #pour le delete, le cursor va avoir la requete sql pour supprimer la donnée
    #lié à l'id associé
    cursor = conn.cursor()
    weightTagDelete = "DELETE FROM t_weight_tag WHERE id=%s" % (id)
    cursor.execute(weightTagDelete)
    conn.commit()
    return "Successful Deleted"
