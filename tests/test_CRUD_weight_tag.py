import unittest
from src.CRUD_weight_tag import *


# the class allow to regroup all the test. it is mandatory to do the test in the good order create first,
# then get and get id, then update , delete last.
class TestWeightTagCrud(unittest.TestCase):

    # this test allow to see if the creation of weight's tag works
    def test_Create(self):
        self.tagValues = 2.0
        res = create_weight_tag(self.tagValues)
        self.assertEquals(res, "Successful Creation")

    # this test allow to see all the weight's tag
    def test_Get(self):
        res = get_weight_tag()
        self.id = list(res[len(res) - 1])[0]
        # print(self.id)
        self.assertEquals(res[len(res) - 1], (self.id, 2.0))

    # this test is to see the weight's tag associated to the id selected
    def test_Get_By_Id(self):
        res = get_weight_tag()
        self.id = list(res[len(res) - 1])[0]
        # print(self.id)
        res2 = get_weight_tag_by_id(self.id)
        self.assertEquals(res2, [(self.id, 2.0)])

    # this test allow to see if the weight's tag can be modified in the database
    def test_Update(self):
        res2 = get_weight_tag()
        self.id = list(res2[len(res2) - 1])[0]
        res = update_weight_tag(self.id, 6.0)
        self.assertEquals(res, 'Successful Updated')
        res2 = get_weight_tag()
        res = res2[len(res2) - 1]
        self.assertEquals(res, (self.id, 6.0))

    # this test allow to see if the weight's tag to the id selected can be removed
    def test_Delete(self):
        res2 = get_weight_tag()
        self.id = list(res2[len(res2) - 1])[0]
        res = delete_weight_tag(self.id)
        self.assertEquals(res, "Successful Deleted")
