import unittest
from src.CRUD_conditioning import *
from src.CRUD_weight_tag import *


# the class allow to regroup all the test. it is mandatory to do the test in the good order create first,
# then get and get id, then update , delete last.
class TestConditioningCrud(unittest.TestCase):

    # this test allow to see if the creation of conditioned object works
    def test_Create(self):
        self.tag = "herta"
        self.weight = 4.0
        self.price = 5.0
        res = create_conditioning(self.tag, self.weight, self.price)
        self.assertEquals(res, "Successful Creation")

    # this test allow to see all the conditioned object
    def test_Get(self):
        res = get_conditioning()
        self.id = list(res[len(res) - 1])[0]
        print(self.id)
        res2 = get_weight_tag()
        self.id2 = list(res2[len(res2) - 1])[0]
        print(self.id2)
        self.assertEquals(res[len(res) - 1], (self.id, "herta", self.id2, 5.0))

    # this test is to see the conditioned object associated to the id selected
    def test_Get_By_Id(self):
        res = get_conditioning()
        self.id = list(res[len(res) - 1])[0]
        # print(self.id)
        res2 = get_weight_tag()
        self.id2 = list(res2[len(res2) - 1])[0]
        res3 = get_conditioning_by_id(self.id)
        self.assertEquals(res3, [(self.id, "herta", self.id2, 5.0)])

    # this test allow to see if the conditioned object can be modified in the database
    def test_Update(self):
        res2 = get_conditioning()
        self.id = list(res2[len(res2) - 1])[0]
        res = update_conditioning(self.id, "jambon", 1.0, 1.0)
        self.assertEquals(res, 'Successful Updated')
        res2 = get_conditioning()
        res = res2[len(res2) - 1]
        res3 = get_weight_tag()
        self.id2 = list(res3[len(res3) - 1])[0]
        # print(self.id)
        self.assertEquals(res, (self.id, "jambon", self.id2, 1.0))

    # this test allow to see if the conditioned object to the id selected can be removed
    def test_Delete(self):
        res2 = get_conditioning()
        self.id = list(res2[len(res2) - 1])[0]
        res = delete_conditioning(self.id)
        self.assertEquals(res, "Successful Deleted")
