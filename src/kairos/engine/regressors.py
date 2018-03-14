# This file is part of the KAIROS package
# Developed in London by mehdithomas and tjespel

# engine/utilityregressors.py
# This file contains the functions used to interact with regressors

from keras.layers import Input, Dense
from keras.models import Model
from keras.optimizers import SGD


class linearRegressor:

    def __init__(self, optimizer='sgd'):
        inputs = Input(shape=(1,))
        predictions = Dense(1, activation='linear')(inputs)
        model = Model(inputs=inputs, outputs=predictions)
        self.__model = Model(inputs=inputs, outputs=predictions)
        sgd = SGD()
        self.__model.compile(optimizer=sgd, loss='mse', metrics=['mse'])

    def fit(self, modelInput, modelOutput, shuffling=False):
        self.__model.fit(modelInput, modelOutput, batch_size=1, epochs=30, shuffle=shuffling)
        return 0

    def predict(self, data):
        return self.__model.predict(data)

    def freeze(self):
        return self.__model.to_json()
