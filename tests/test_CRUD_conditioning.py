import unittest
from src.CRUD_conditioning import *
from src.CRUD_weight_tag import *


# the class allow to regroup all the test. it is mandatory to do the test in the good order create first,
# then get and get id, then update , delete last.

# this test allow to see if the creation of conditioned object works
def test_Create():
    tag = "herta"
    weight = 4.0
    price = 5.0
    res = create_conditioning(tag, weight, price)
    assert (res, "Successful Creation")


# this test allow to see all the conditioned object
def test_Get():
    res = get_all_conditioning()
    id = list(res[len(res) - 1])[0]
    print(id)
    res2 = get_all_weight_tag()
    id2 = list(res2[len(res2) - 1])[0]
    print(id2)
    assert (res[len(res) - 1], (id, "herta", id2, 5.0))


# this test is to see the conditioned object associated to the id selected
def test_Get_By_Id():
    res = get_all_conditioning()
    id = list(res[len(res) - 1])[0]
    # print(id)
    res2 = get_all_weight_tag()
    id2 = list(res2[len(res2) - 1])[0]
    res3 = get_conditioning_by_id(id)
    assert (res3, [(id, "herta", id2, 5.0)])


# this test allow to see if the conditioned object can be modified in the database
def test_Update():
    res2 = get_all_conditioning()
    id = list(res2[len(res2) - 1])[0]
    res = update_conditioning(id, "jambon", 1.0, 1.0)
    assert (res, 'Successful Updated')
    res2 = get_all_conditioning()
    res = res2[len(res2) - 1]
    res3 = get_all_weight_tag()
    id2 = list(res3[len(res3) - 1])[0]
    # print(id)
    assert (res, (id, "jambon", id2, 1.0))


# this test allow to see if the conditioned object to the id selected can be removed
def test_Delete():
    res2 = get_all_conditioning()
    id = list(res2[len(res2) - 1])[0]
    res = delete_conditioning(id)
    assert (res, "Successful Deleted")
