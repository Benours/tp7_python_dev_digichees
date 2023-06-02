import unittest
from src.CRUD_city import *


# the class allow to regroup all the test. it is mandatory to do the test in the good order create first,
# then get and get id, then update , delete last.
class TestCityCrud(unittest.TestCase):

    # this test allow to see if the creation of city works
    def test_Create(self):
        self.zipCode = '46800'
        self.name = 'Montcuq'
        self.department = 'Lot'
        res = create_city(self.zipCode, self.name, self.department)
        self.assertEquals(res, "Successful Creation")

    # this test allow to see all the city registered
    def test_Get(self):
        res = get_city()
        self.id = list(res[len(res) - 1])[0]
        print(self.id)
        self.assertEquals(res[len(res) - 1], (self.id, '46042', 'Montcuq', 'Lot'))

    # this test is to see the city associated to the id selected
    def test_Get_By_Id(self):
        res = get_city()
        self.id = list(res[len(res) - 1])[0]
        res2 = get_city_by_id(self.id)
        self.assertEquals(res2, [(self.id, '46042', 'Montcuq', 'Lot')])

    # this test allow to see if the city can be modified in the database
    def test_Update(self):
        res2 = get_city()
        self.id = list(res2[len(res2) - 1])[0]
        res = update_city(self.id, '46042', 'Cahors', 'Lot')
        self.assertEquals(res, 'Successful Updated')
        res2 = get_city()
        res = res2[len(res2) - 1]
        self.assertEquals(res, (self.id, '46042', 'Cahors', 'Lot'))

    # this test allow to see if the city to the id selected can be removed
    def test_Delete(self):
        res2 = get_city()
        self.id = list(res2[len(res2) - 1])[0]
        res = delete_city(str(self.id))
        self.assertEquals(res, "Successful Deleted")
