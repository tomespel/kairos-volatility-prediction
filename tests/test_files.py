import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir+'/src')

import pytest
import kairos

@pytest.fixture
def data():
    return kairos.input.from_csv('testinput.csv')

def test_save_restore(data):
    kairos.output.freeze(data, 'test.krf')
    for i in range(len(data)):
        for j in range(data[i].get_daysNumber()):
            assert data[i][j].get_allFeatures() == kairos.input.release('test.krf')[i][j].get_allFeatures()
