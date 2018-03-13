import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir+'/src')

from kairos import *


data = kairos.input.from_csv('../samples/training_input.min.csv')  # When using for the first time, the delete
#data = kairos.input.release('../mehdi.min.krf')

# Do my stuff

kairos.output.freeze(data, '../samples/mehdi.min.krf')
