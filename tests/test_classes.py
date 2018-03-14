import os
import sys
import inspect
import pytest
import kairos
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir+'/src')


@pytest.fixture
def data():
    return kairos.input.from_csv('testinput.csv')


# Features manipulation


def addFeature(data):
    for i in range(data.get_assetsNumber()):
        for j in range(data[i].get_daysNumber()):
            data[i][j].add_feature('testFeature', [1, 2, 3])
    return 0


def test_addFeature(data):
    addFeature(data)
    for i in range(data.get_assetsNumber()):
        for j in range(data[i].get_daysNumber()):
            assert data[i][j].get_feature('testFeature') == [1, 2, 3]


def test_addFeatureError(data):
    addFeature(data)
    for i in range(data.get_assetsNumber()):
        for j in range(data[i].get_daysNumber()):
            assert data[i][j].get_feature('testFeature') == [1, 2, 3]


def test_getFeatureError(data):
    addFeature(data)
    for i in range(data.get_assetsNumber()):
        for j in range(data[i].get_daysNumber()):
            with pytest.raises(Exception):
                data[i][j].get_feature('testFeature2')


def test_setFeature(data):
    addFeature(data)
    for i in range(data.get_assetsNumber()):
        for j in range(data[i].get_daysNumber()):
            data[i][j].set_feature('testFeature', [4, 5, 6])
    for i in range(data.get_assetsNumber()):
        for j in range(data[i].get_daysNumber()):
            assert data[i][j].get_feature('testFeature') == [4, 5, 6]


def test_setFeatureError(data):
    addFeature(data)
    for i in range(data.get_assetsNumber()):
        for j in range(data[i].get_daysNumber()):
            with pytest.raises(Exception):
                data[i][j].set_feature('testFeature', [7, 8, 9, 10])
    for i in range(data.get_assetsNumber()):
        for j in range(data[i].get_daysNumber()):
            assert data[i][j].get_feature('testFeature') == [1, 2, 3]
