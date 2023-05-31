import unittest
from src.CRUD_Conditioning import *
from src.CRUD_WeightTag import *
#La class permet de regrouper les tes à effectué
class testConditioningCrud(unittest.TestCase):
    #Mais ne pas lancé le test testConditioningCrud parce que
    #le lancement ce fait dans le désordre et ne créer pas
    #le conditionnementavant de le supprimer ou le modifier.
    #Donc, il faut le lancer dans l'ordre la création d'abord
    #la suppression à la fin
    def testCreate(self):
        #la fonction createConditioning retourne "successful creation"
        #si la method fonctionne correctement pour qu'on le voit sur swagger
        #que la création est affecué, donc on a juste à savoir si la création est un succés
        self.tag="herta"
        self.weight=4.0
        self.price= 5.0
        res=createConditioning(self.tag, self.weight, self.price)
        self.assertEquals(res, "Successful Creation")

    def testGet(self):
        #si l'ordre est respecté par incrémentation nous devons retrouver à la dernière place
        #Herta
        res=getConditioning()
        self.id=list(res[len(res)-1])[0]
        print(self.id)
        res2 = getWeightTag()
        self.id2 = list(res2[len(res2) - 1])[0]
        print(self.id2)
        self.assertEquals(res[len(res)-1], (self.id,"herta", self.id2, 5.0))

    def testUpdate(self):
        #donc parce que on a besoin de l'id du dernier emplacement
        #on récupère l'id de getConditioning pour l'update
        res2=getConditioning()
        self.id = list(res2[len(res2) - 1])[0]
        res=updateConditioning(self.id, "jambon", 1.0,1.0)
        self.assertEquals(res, 'Successful Updated')
        #on recupère l'id de weightTag parce que les tables sont liés
        res2 = getConditioning()
        res= res2[len(res2) - 1]
        res3 = getWeightTag()
        self.id2 = list(res3[len(res3) - 1])[0]
        print(self.id)
        self.assertEquals(res, (self.id, "jambon", self.id2,1.0))

    def testDelete(self):
        #tout comme l'update, on a besoin de l'id du dernier emplacement pour supprimer
        #le tag test
        res2 = getConditioning()
        self.id = list(res2[len(res2) - 1])[0]
        res=deleteConditioning(self.id)
        self.assertEquals(res, "Successful Deleted")