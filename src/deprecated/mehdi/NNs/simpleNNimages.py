import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
import keras

import re
import h5py


path = '../OriginalData/training_input.csv'
path_output = '../OriginalData/training_output.csv'
path_testing = '../OriginalData/testing_input.csv'

path = 'preprocess.csv'
path_output = 'target_1.csv'

data = pd.read_csv(path,sep = ";")
output_train = pd.read_csv(path_output,sep = ";",header = None)


data = data.fillna(data.median())

X = data.values
y = output_train.values

X_train,X_test,y_train,y_test = train_test_split(X,y)

model = Sequential()

model.add(Dense(300,input_dim = X.shape[1],activation = 'relu'))
model.add(Dense(100,activation = 'relu'))
model.add(Dense(30,activation = 'relu'))
model.add(Dense(1,activation = 'softmax'))

model.compile(optimizer = "adam",loss = keras.losses.kullback_leibler_divergence,metrics = [keras.metrics.categorical_accuracy])

model.fit(X_train,y_train,validation_data = (X_test,y_test),verbose = True,epochs = 50,batch_size = 10)


predictions.to_csv('predictions_L_deep_with_test.csv',index = False)

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")
