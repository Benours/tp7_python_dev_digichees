import unittest
from src.CRUD_city import *

class testCityCrud(unittest.TestCase):

    def testCreate(self):
        self.zipCode = '46800'
        self.name = 'Montcuq'
        self.department = 'Lot'
        res=createCity(self.zipCode, self.name, self.department)
        self.assertEquals(res, "Successful Creation")

    def testGet(self):
        res=getCity()
        self.id=res[0][0]
        self.assertEquals(res[0], (id,'46800','Montcuq','Lot'))

    def testUpdate(self):
        res=updateCity(self.id, '46042', 'Cahors', 'Lot')
        res2=getCity()
        self.assertEquals(res, 'Successful Updated')
        self.assertEquals(res2[0], (self.id, '46042', 'Cahors', 'Lot'))

    def testDelete(self):
        res=deleteCity(str(self.id))
        self.assertEquals(res, "Successful Deleted")
