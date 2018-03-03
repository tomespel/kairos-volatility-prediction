import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense,Dropout
import keras
from keras.callbacks import EarlyStopping

import re
import h5py


path = 'feature_engineered_50.csv'

data = pd.read_csv(path,sep = ";")

#data = data.loc[data['TARGET'] >= 0.05]

y = data['TARGET'].values

del data['TARGET']

data = data.fillna(data.median())
data =data.replace(np.inf,100.0)
data =data.replace(-np.inf,-100.0)


X = data.values

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 1)

model = Sequential()

model.add(Dense(1000,input_dim = X.shape[1],activation = 'elu'))
model.add(Dense(300,input_dim = X.shape[1],activation = 'elu'))
model.add(Dense(100,activation = 'elu'))
model.add(Dense(30,activation = 'elu'))
model.add(Dense(10,activation = 'elu'))
model.add(Dense(1,activation = 'elu'))

model.compile(optimizer = "adam",loss = keras.losses.mean_absolute_percentage_error)

class LossHistory(keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.losses = []

    def on_batch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))

history = LossHistory()

early_stopping = EarlyStopping(monitor='val_loss', patience=1000)

model.fit(X_train,y_train,validation_data = (X_test,y_test),verbose = True,epochs = 2000,batch_size = 100,callbacks=[history,early_stopping])

pd.DataFrame(history.losses).to_csv('losses_smaller_batches_50.csv',index = False,sep = ';')

predictions = model.predict(X)

pd.DataFrame(predictions).to_csv('PREDICTIONS.csv',index = False, sep = ';')

# serialize model to JSON
model_json = model.to_json()
with open("model_small_batches_50.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model_smaller_batches_50.h5")
print("Saved model to disk")
