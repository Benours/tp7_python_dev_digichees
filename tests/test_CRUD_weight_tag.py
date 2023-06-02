import unittest
from src.CRUD_weight_tag import *


# the class allow to regroup all the test. it is mandatory to do the test in the good order create first,
# then get and get id, then update , delete last.

# this test allow to see if the creation of weight's tag works
def test_Create():
    tagValues = 2.0
    res = create_weight_tag(tagValues)
    assert (res, "Successful Creation")


# this test allow to see all the weight's tag
def test_Get():
    res = get_all_weight_tag()
    id = list(res[len(res) - 1])[0]
    # print(id)
    assert (res[len(res) - 1], (id, 2.0))


# this test is to see the weight's tag associated to the id selected
def test_Get_By_Id():
    res = get_all_weight_tag()
    id = list(res[len(res) - 1])[0]
    # print(id)
    res2 = get_weight_tag_by_id(id)
    assert (res2, [(id, 2.0)])


# this test allow to see if the weight's tag can be modified in the database
def test_Update():
    res2 = get_all_weight_tag()
    id = list(res2[len(res2) - 1])[0]
    res = update_weight_tag(id, 6.0)
    assert (res, 'Successful Updated')
    res2 = get_all_weight_tag()
    res = res2[len(res2) - 1]
    assert (res, (id, 6.0))


# this test allow to see if the weight's tag to the id selected can be removed
def test_Delete():
    res2 = get_all_weight_tag()
    id = list(res2[len(res2) - 1])[0]
    res = delete_weight_tag(id)
    assert (res, "Successful Deleted")
