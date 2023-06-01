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
        res = create_city(self.zipCode, self.name, self.department)
        self.assertEquals(res, "Successful Creation")

    def testGet(self):
        # si l'ordre est respecté par incrémentation nous devons retrouver à la dernière place
        # Montcuq
        res = get_city()
        self.id = list(res[len(res) - 1])[0]
        print(self.id)
        self.assertEquals(res[len(res) - 1], (self.id, '46042', 'Cahors', 'Lot'))

    def testGetById(self):
        # si l'ordre est respecté par incrémentation nous devons retrouver à la dernière place
        # par id.
        res = get_city()
        self.id = list(res[len(res) - 1])[0]
        res2 = get_city_by_id(self.id)
        self.assertEquals(res2, [(self.id, '46042', 'Cahors', 'Lot')])

    def testUpdate(self):
        # donc parce que on a besoin de l'id du dernier emplacement
        # on récupère l'id de getcity pour l'update
        res2 = get_city()
        self.id = list(res2[len(res2) - 1])[0]
        res = update_city(self.id, '46042', 'Cahors', 'Lot')
        self.assertEquals(res, 'Successful Updated')
        res2 = get_city()
        res = res2[len(res2) - 1]
        self.assertEquals(res, (self.id, '46042', 'Cahors', 'Lot'))

    def testDelete(self):
        # tout comme l'update, on a besoin de l'id du dernier emplacement pour supprimer
        # la ville teste
        res2 = get_city()
        self.id = list(res2[len(res2) - 1])[0]
        res = delete_city(str(self.id))
        self.assertEquals(res, "Successful Deleted")
