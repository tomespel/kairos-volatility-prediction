from kairos import *


print(kairos.engine.assetclassifier.test())

import pandas as pd
data = pd.DataFrame.from_csv('../samples/training_input.min.csv')
data.head()
indexes = data.index.tolist()
testrow = data.loc[indexes[0]]
import datetime
a = datetime.datetime.now()
objects = []
for i in range(len(indexes)):
    objects.append(kairos.classes.KairosDay(data.loc[indexes[i]], indexes[i]))
b = datetime.datetime.now()
print(len(objects))
print(b-a)

object1 = kairos.classes.KairosDay(testrow, indexes[0])
object1.get_volatility()


import pickle
a = datetime.datetime.now()
filehandler = open('../samples/saveddays.kairos', 'wb')
pickle.dump(objects, filehandler)
b = datetime.datetime.now()
print(b-a)
a = datetime.datetime.now()
filereader = open('../samples/saveddays.kairos', 'rb')
new_objects = pickle.load(filereader)
b = datetime.datetime.now()
print(b-a)
print(new_objects)
print(new_objects[-1].get_volatility()[4])
