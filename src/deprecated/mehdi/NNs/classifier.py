import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
import keras

import re
import h5py
from keras.utils import to_categorical

path = 'data_with_vols.csv'

data = pd.read_csv(path,sep = ";")

data = data.fillna(data.median())
data = data.replace(np.inf,data.median())
y = (1*(data["TARGET"] <= 0.1)).values
y =  to_categorical(y)

del data['TARGET']

X = data.values

X_train,X_test,y_train,y_test = train_test_split(X,y)

model = Sequential()

model.add(Dense(1000,input_dim = X.shape[1],activation = 'sigmoid'))
model.add(Dense(300,activation = 'sigmoid'))
model.add(Dense(100,activation = 'sigmoid'))
model.add(Dense(10,activation = 'sigmoid'))
model.add(Dense(2,activation = 'softmax'))

model.compile(optimizer = "adam",loss =  keras.losses.binary_crossentropy,metrics = [keras.metrics.categorical_accuracy])

model.fit(X_train,y_train,validation_data = (X_test,y_test),verbose = True,epochs = 100,batch_size = 100)
