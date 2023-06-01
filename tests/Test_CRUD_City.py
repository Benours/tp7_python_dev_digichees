import unittest
from src.CRUD_city import *


# La class permet de regrouper les tes à effectué
class testCityCrud(unittest.TestCase):
    # Mais ne pas lancé le test testCityCrud parce que
    # le lancement ce fait dans le désordre et ne créer pas
    # la ville avant de le supprimer ou le modifier.
    # Donc, il faut le lancer dans l'ordre la création d'abord
    # la suppression à la fin
    def testCreate(self):
        # la fonction createCity retourne "successful creation"
        # si la method fonctionne correctement pour qu'on le voit sur swagger
        # que la création est affecué, donc on a juste à savoir si la création est un succés
        self.zipCode = '46800'
        self.name = 'Montcuq'
        self.department = 'Lot'
        res = createCity(self.zipCode, self.name, self.department)
        self.assertEquals(res, "Successful Creation")

    def testGet(self):
        # si l'ordre est respecté par incrémentation nous devons retrouver à la dernière place
        # Montcuq
        res = getCity()
        self.id = list(res[len(res) - 1])[0]
        print(self.id)
        self.assertEquals(res[len(res) - 1], (self.id, '46800', 'Montcuq', 'Lot'))

    def testGetById(self):
        # si l'ordre est respecté par incrémentation nous devons retrouver à la dernière place
        # par id.
        res = getCity()
        self.id = list(res[len(res) - 1])[0]
        res2 = getCityById(self.id)
        self.assertEquals(res2, [(self.id, '46800', 'Montcuq', 'Lot')])

    def testUpdate(self):
        # donc parce que on a besoin de l'id du dernier emplacement
        # on récupère l'id de getcity pour l'update
        res2 = getCity()
        self.id = list(res2[len(res2) - 1])[0]
        res = updateCity(self.id, '46042', 'Cahors', 'Lot')
        self.assertEquals(res, 'Successful Updated')
        res2 = getCity()
        res = res2[len(res2) - 1]
        self.assertEquals(res, (self.id, '46042', 'Cahors', 'Lot'))

    def testDelete(self):
        # tout comme l'update, on a besoin de l'id du dernier emplacement pour supprimer
        # la ville teste
        res2 = getCity()
        self.id = list(res2[len(res2) - 1])[0]
        res = deleteCity(str(self.id))
        self.assertEquals(res, "Successful Deleted")
