from kairos import *


data = kairos.input.from_csv('../samples/training_input.min.csv')  # When using for the first time, the delete
#data = kairos.input.release('../mehdi.min.krf')

# Do my stuff

kairos.input.freeze(data, '../samples/mehdi.min.krf')
