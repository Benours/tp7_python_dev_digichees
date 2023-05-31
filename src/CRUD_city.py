from fastapi import FastAPI

from src.Connect import conn

app = FastAPI()


@app.post("/post")
def createCity(zipCode: str, name: str, department: str):
    cursor = conn.cursor()
    cityInsert = """INSERT INTO t_city(
        zipCode,
        name,
        department)
        VALUES (%s,%s,%s)"""
    cursor.execute(cityInsert, (zipCode, name, department))
    conn.commit()
    return "Successful Creation"


@app.get('/get')
def getCity():
    cursor = conn.cursor()
    cityGet = """SELECT * FROM t_city"""
    cursor.execute(cityGet)
    city = cursor.fetchall()
    for c in city:
        print(c)
    return city


@app.put("/put")
def updateCity(id: int, zipCode: str, name: str, department: str):
    cursor = conn.cursor()
    cityUpdate = "UPDATE t_city SET zipCode=%s, name=%s, department=%s WHERE id=%s"
    cursor.execute(cityUpdate, (zipCode, name, department, id))
    conn.commit()
    return "Successful Updated"


@app.delete("/delete")
def deleteCity(id):
    cursor = conn.cursor()
    cityDelete = "DELETE FROM t_city WHERE id=%s"
    cursor.execute(cityDelete, tuple(id))
    conn.commit()
    return "Successful Deleted"


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='127.0.0.1', port=8282)
