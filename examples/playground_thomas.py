import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir+'/src')

from kairos import *
import matplotlib.pyplot as plt
#import datetime

#data = kairos.input.from_csv('../samples/training_input.min.csv')

data = kairos.input.release('../samples/thomas.min.krf')

# Do my stuff
data[0][0]

for day in data[0]:
    plt.plot(day.get_volatility())
plt.show()

for day in data[0]:
    plt.plot(day.get_returns())
plt.show()

kairos.output.freeze(data, '../samples/thomas.min.krf')