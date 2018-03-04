from kairos import *


print(kairos.engine.assetclassifier.test())

import pandas as pd
data = pd.DataFrame.from_csv('../samples/training_input.min.csv')
<<<<<<< HEAD
#data.head()
=======
data.head()
>>>>>>> a1673677c2df93f7e003fd73eee87752d7b28b34
indexes = data.index.tolist()
testrow = data.loc[indexes[0]]



object1 = kairos.classes.KairosDay(testrow, indexes[0])
<<<<<<< HEAD
object1.get_volatility()
=======
>>>>>>> a1673677c2df93f7e003fd73eee87752d7b28b34
