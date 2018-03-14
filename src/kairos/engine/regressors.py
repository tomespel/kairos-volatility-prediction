# This file is part of the KAIROS package
# Developed in London by mehdithomas and tjespel

# engine/utilityregressors.py
# This file contains the functions used to interact with regressors

from keras.layers import Input, Dense
from keras.models import Model
from keras.optimizers import SGD
from keras.models import model_from_yaml


#This model only takes one input
class linearRegressorSingle:

    def __init__(self, optimizer='sgd'):
        inputs = Input(shape=(1,))
        predictions = Dense(1, activation='linear')(inputs)
        self.__model = Model(inputs=inputs, outputs=predictions)
        sgd = SGD()
        self.__model.compile(optimizer=sgd, loss='mse', metrics=['mse'])

    def fit(self, inputDay, shuffling=False):
        if inputDay.get_targetValue() is None:
            raise Exception("Day has no target value")
            return 1
        self.__model.fit(inputDay.get_allFeatures(), [inputDay.get_targetValue()[0]], shuffle=shuffling)
        return 0

    def fitForce(self, inputValues, outputValues, shuffling=False):
        self.__model.fit(inputValues, outputValues, shuffle=shuffling)
        return 0

    def predict(self, data):
        predictions = self.__model.predict(data).tolist()
        return predictions

    def freeze(self):
        return self.__model.to_json()

    def loadModel(self, modelData):
        self.__model = model_from_yaml(modelData)
        return 0
