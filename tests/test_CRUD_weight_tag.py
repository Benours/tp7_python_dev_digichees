import unittest
from src.CRUD_weight_tag import *
#La class permet de regrouper les tes à effectué
class testWeightTagCrud(unittest.TestCase):
    #Mais ne pas lancé le test testWeightTagCrud parce que
    #le lancement ce fait dans le désordre et ne créer pas
    #le PoidV avant de le supprimer ou le modifier.
    #Donc, il faut le lancer dans l'ordre la création d'abord
    #la suppression à la fin
    def testCreate(self):
        #la fonction createWeightTag retourne "successful creation"
        #si la method fonctionne correctement pour qu'on le voit sur swagger
        #que la création est affecué, donc on a juste à savoir si la création est un succés
        self.tagValues=2.0
        res= create_weight_tag(self.tagValues)
        self.assertEquals(res, "Successful Creation")

    def testGet(self):
        #si l'ordre est respecté par incrémentation nous devons retrouver à la dernière place
        #2.0
        res=get_weight_tag()
        self.id=list(res[len(res)-1])[0]
        #print(self.id)
        self.assertEquals(res[len(res)-1], (self.id,2.0))

    def testGetById(self):
        #si l'ordre est respecté par incrémentation nous devons retrouver à la dernière place
        #par id.
        res=get_weight_tag()
        self.id=list(res[len(res)-1])[0]
        #print(self.id)
        res2=get_weight_tag_by_id(self.id)
        self.assertEquals(res2, [(self.id,2.0)])

    def testUpdate(self):
        #donc parce que on a besoin de l'id du dernier emplacement
        #on récupère l'id de getWeightTag pour l'update
        res2=get_weight_tag()
        self.id = list(res2[len(res2) - 1])[0]
        res=update_weight_tag(self.id, 6.0)
        self.assertEquals(res, 'Successful Updated')
        res2 = get_weight_tag()
        res= res2[len(res2) - 1]
        self.assertEquals(res, (self.id, 6.0))

    def testDelete(self):
        #tout comme l'update, on a besoin de l'id du dernier emplacement pour supprimer
        #le PoidV test
        res2 = get_weight_tag()
        self.id = list(res2[len(res2) - 1])[0]
        res=delete_weight_tag(self.id)
        self.assertEquals(res, "Successful Deleted")
