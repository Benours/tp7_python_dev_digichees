import unittest
from src.CRUD_city import *


# the class allow to regroup all the test. it is mandatory to do the test in the good order create first,
# then get and get id, then update , delete last.


# this test allow to see if the creation of city works
def test_Create():
    zipCode = '46800'
    name = 'Montcuq'
    department = 'Lot'
    res = create_city(zipCode, name, department)
    assert res == "Successful Creation"

# this test allow to see all the city registered
def test_Get():
    res = get_all_city()
    id = list(res[len(res) - 1])[0]
    print(id)
    assert res[len(res) - 1] == (id, '46800', 'Montcuq', 'Lot')

# this test is to see the city associated to the id selected
def test_Get_By_Id():
    res = get_all_city()
    id = list(res[len(res) - 1])[0]
    res2 = get_city_by_id(id)
    assert res2 ==  [(id, '46800', 'Montcuq', 'Lot')]

# this test allow to see if the city can be modified in the database
def test_Update():
    res2 = get_all_city()
    id = list(res2[len(res2) - 1])[0]
    res = update_city(id, '46042', 'Cahors', 'Lot')
    assert res ==  'Successful Updated'
    res2 = get_all_city()
    res = res2[len(res2) - 1]
    assert res == (id, '46042', 'Cahors', 'Lot')

# this test allow to see if the city to the id selected can be removed
def test_Delete():
    res2 = get_all_city()
    id = list(res2[len(res2) - 1])[0]
    res = delete_city(str(id))
    assert  res == "Successful Deleted"
