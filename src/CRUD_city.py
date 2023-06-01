from fastapi import APIRouter

from src.connect import conn

app = APIRouter()

#on import fastapi pour swagger et conn qui est dans connect.py qui
#permet la connection avec la base de donnée

# Create a new city with ZIPCode, name and department
@app.post("/post")
def create_city(zipCode: str, name: str, department: str):
    #on doit créer un nouvelle ville pour cela on a un l'id qui est auto incrémentable
    #nous avons plus qu'a créer un cursor pour mettre une requete sql pour inserer les données
    cursor = conn.cursor()
    cityInsert = """INSERT INTO t_city(
        zipCode,
        name,
        department)
        VALUES (%s,%s,%s)"""
    cursor.execute(cityInsert, (zipCode, name, department))
    conn.commit()
    return "Successful Creation"

# Get all the cities
@app.get('/getall')
def get_city():
    #pour le get le cursor aura pour requete sql un select * pour tout avoir dans la table t_city
    cursor = conn.cursor()
    cityGet = """SELECT * FROM t_city"""
    cursor.execute(cityGet)
    city = cursor.fetchall()
    for c in city:
        print(c)
    return city

# Return one city with id
@app.get('/getbyid')
def get_city_by_id(id: int):
    #pour le get le cursor aura pour requete sql un select * pour tout avoir dans la table t_city
    cursor = conn.cursor()
    cityGet = "SELECT * FROM t_city WHERE id=%s" % (id)
    cursor.execute(cityGet)
    city = cursor.fetchall()
    return city

# Modify city information with this ZIPCode, name and department and id to access
@app.put("/put")
def update_city(id: int, zipCode: str, name: str, department: str):
    #pour le update, nous allons modifier les 3 parametres: code postal(zipCode),
    #la ville(name), et le departement(department). mais pour cela il faut
    #renseigner l'id qui est unique puisque qu'il va être liée au client
    cursor = conn.cursor()
    cityUpdate = "UPDATE t_city SET zipCode=%s, name=%s, department=%s WHERE id=%s"
    cursor.execute(cityUpdate, (zipCode, name, department, id))
    conn.commit()
    return "Successful Updated"

# Delete a city with id
@app.delete("/delete")
def delete_city(id: int):
    #pour le delete, le cursor va avoir la requete sql pour supprimer la donnée
    #lié à l'id associé
    cursor = conn.cursor()
    cityDelete = "DELETE FROM t_city WHERE id=%s" % (id)
    cursor.execute(cityDelete)
    conn.commit()
    return "Successful Deleted"


