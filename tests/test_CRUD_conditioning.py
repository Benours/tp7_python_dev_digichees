import unittest
from src.CRUD_conditioning import *
from src.CRUD_weight_tag import *


# La class permet de regrouper les tests à effectué
class TestConditioningCrud(unittest.TestCase):
    # Mais ne pas lancé le test testConditioningCrud parce que
    # le lancement ce fait dans le désordre et ne créer pas
    # le conditionnement avant de le supprimer ou le modifier.
    # Donc, il faut le lancer dans l'ordre la création d'abord
    # la suppression à la fin

    # test de la création de l'objet conditionné
    def test_Create(self):
        # la fonction createConditioning retourne "successful creation"
        # si la method fonctionne correctement pour qu'on le voit sur swagger
        # que la création est affecué, donc on a juste à savoir si la création est un succés
        self.tag = "herta"
        self.weight = 4.0
        self.price = 5.0
        res = create_conditioning(self.tag, self.weight, self.price)
        self.assertEquals(res, "Successful Creation")

    # test pour avoir toutes les objets conditionnés
    def test_Get(self):
        # si l'ordre est respecté par incrémentation nous devons retrouver à la dernière place
        # Herta
        res = get_conditioning()
        self.id = list(res[len(res) - 1])[0]
        print(self.id)
        res2 = get_weight_tag()
        self.id2 = list(res2[len(res2) - 1])[0]
        print(self.id2)
        self.assertEquals(res[len(res) - 1], (self.id, "herta", self.id2, 5.0))

    # test pour avoir l'objets conditionné associé à l'id inscrit
    def test_Get_By_Id(self):
        # si l'ordre est respecté par incrémentation nous devons retrouver à la dernière place
        # par id.
        res = get_conditioning()
        self.id = list(res[len(res) - 1])[0]
        # print(self.id)
        res2 = get_weight_tag()
        self.id2 = list(res2[len(res2) - 1])[0]
        res3 = get_conditioning_by_id(self.id)
        self.assertEquals(res3, [(self.id, "herta", self.id2, 5.0)])

    # test pour modifier les informations associé à l'id
    def test_Update(self):
        # donc parce que on a besoin de l'id du dernier emplacement
        # on récupère l'id de getConditioning pour l'update
        res2 = get_conditioning()
        self.id = list(res2[len(res2) - 1])[0]
        res = update_conditioning(self.id, "jambon", 1.0, 1.0)
        self.assertEquals(res, 'Successful Updated')
        # on recupère l'id de weightTag parce que les tables sont liés
        res2 = get_conditioning()
        res = res2[len(res2) - 1]
        res3 = get_weight_tag()
        self.id2 = list(res3[len(res3) - 1])[0]
        # print(self.id)
        self.assertEquals(res, (self.id, "jambon", self.id2, 1.0))

    # test de suppression de l'id avec son contenu
    def test_Delete(self):
        # tout comme l'update, on a besoin de l'id du dernier emplacement pour supprimer
        # le tag test
        res2 = get_conditioning()
        self.id = list(res2[len(res2) - 1])[0]
        res = delete_conditioning(self.id)
        self.assertEquals(res, "Successful Deleted")
