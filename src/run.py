from kairos import *


print(kairos.engine.assetclassifier.test())

import pandas as pd
data = pd.DataFrame.from_csv('../samples/training_input.min.csv')
#data.head()
indexes = data.index.tolist()
testrow = data.loc[indexes[0]]



object1 = kairos.classes.KairosDay(testrow, indexes[0])
object1.get_volatility()
