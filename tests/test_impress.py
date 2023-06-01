import unittest
from src.Impress import *
class test_impress(unittest.TestCase):
    async def test_impress_all(self):
        res=await impress_all('01062023')
        self.assertEquals(res, 'Successful Impression')

    async def test_impress_user(self):
        res=await impress_user('01062023')
        self.assertEquals(res, 'Successful Impression')

    def test_impress_city(self):
        res= impress_city('01062023')
        self.assertEquals(res, 'Successful Impression')

    def test_impress_conditioning(self):
        res= impress_conditioning('01062023')
        self.assertEquals(res, 'Successful Impression')

    async def test_impress_weight(self):
        res=await impress_weights('01062023')
        self.assertEquals(res, 'Successful Impression')

    def test_impress_weight_tag(self):
        res= impress_weight_tag('01062023')
        self.assertEquals(res, 'Successful Impression')

    async def test_impress_object(self):
        res=await impress_objects('01062023')
        self.assertEquals(res, 'Successful Impression')