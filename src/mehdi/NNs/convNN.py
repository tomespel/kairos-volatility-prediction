import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Activation, Flatten
from keras.utils import np_utils # utilities for one-hot encoding of ground truth values
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
import re


path = 'preprocess.csv'
path_output = 'target_1.csv'

data = pd.read_csv(path,sep = ";")
output_train = pd.read_csv(path_output,sep = ";",header = None)


data = data.fillna(data.median())

X = data.values
y = np.array(output_train.values)

X_train,X_test,Y_train,Y_test = train_test_split(X,y)

X_train = X_train.reshape((X_train.shape[0],159,108,1))

model = Sequential()
# input: 100x100 images with 3 channels -> (100, 100, 3) tensors.
# this applies 32 convolution filters of size 3x3 each.
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(X_train.shape[1], X_train.shape[2],1)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.1))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.1))

model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(1, activation='softmax'))

model.compile(optimizer = "adam",loss = keras.losses.binary_crossentropy,metrics = [keras.metrics.categorical_accuracy])


model.fit(X_train, Y_train,                # Train the model using the training set...
          batch_size=100, epochs=10,
          verbose=1, validation_split=0.1) # ...holding out 10% of the data for validation

X_test = X_test.reshape((X_test.shape[0],159,108,1))

print(model.predict(X_test))

print(Y_test)

model.evaluate(X_test, Y_test, verbose=1)  # Evaluate the trained model on the test set!
