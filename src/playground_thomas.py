from kairos import *
import datetime
a = datetime.datetime.now()
test = kairos.input.from_csv('../samples/training_input.min.csv')
b = datetime.datetime.now()
print(b-a)

len(test)

import pandas as pd

a = datetime.datetime.now()
data = pd.DataFrame.from_csv('../samples/training_input.min.csv')
b = datetime.datetime.now()
print(len(data))
print(b-a)


a = datetime.datetime.now()
kairos.output.freeze(test, '../samples/training_input.min.krf')
b = datetime.datetime.now()
print(b-a)
a = datetime.datetime.now()
retrieve = kairos.input.release('../samples/training_input.min.krf')
b = datetime.datetime.now()
print(b-a)
