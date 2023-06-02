import unittest
from src.Impress import *


# Test to see if you can impress all the database with the chosen date
def test_impress_all():
    res = impress_all('01062023')
    assert (res, 'Successful Impression')


# Test to see if you can impress all the users with the chosen date
def test_impress_user():
    res = impress_user('01062023')
    assert (res, 'Successful Impression')


# Test to see if you can impress all the cities with the chosen date
def test_impress_city():
    res = impress_city('01062023')
    assert (res, 'Successful Impression')


# Test to see if you can impress all the conditioned objects with the chosen date
def test_impress_conditioning():
    res = impress_conditioning('01062023')
    assert (res, 'Successful Impression')


def test_impress_weight():
    res = impress_weights('01062023')
    assert (res, 'Successful Impression')


def test_impress_weight_tag():
    res = impress_weight_tag('01062023')
    assert (res, 'Successful Impression')


def test_impress_object():
    res = impress_objects('01062023')
    assert (res, 'Successful Impression')
