from kairos import *
import datetime
a = datetime.datetime.now()
test = kairos.input.from_csv('../samples/training_input.min.csv')
b = datetime.datetime.now()
print(b-a)

len(test)

test[0].get_date()
test2=sorted(test, key=kairos.classes.KairosDay.get_date)
test3 =  kairos.classes.KairosAsset(test)

print(kairos.engine.assetclassifier.test())

import pandas as pd

a = datetime.datetime.now()
data = pd.DataFrame.from_csv('../samples/training_input.min.csv')
b = datetime.datetime.now()
print(len(data))
print(b-a)

test[0].get_returns()

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
