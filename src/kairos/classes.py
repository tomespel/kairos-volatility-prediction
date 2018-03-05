# This file is part of the KAIROS package
# Developed in London by mehdithomas and tjespel

# classes.py
# This file contains the class definitions


# General elements
import time  # Generation of timestamps in classes
classesListStringDates = [time.strftime('%H:%M:%S', time.gmtime(34200 + i*300)) for i in range(53)]


# KairosDay includes the informations related to a day of volatility

class KairosDay:

    def __string_to_float(self, value):
        return float(value) if value != '' else None

    def __raw_conversion(self, row):
        volatility = [self.__string_to_float(row['volatility ' + classesListStringDates[i]]) for i in range(len(classesListStringDates))]
        returns = [self.__string_to_float(row['return ' + classesListStringDates[i]]) for i in range(len(classesListStringDates))]
        return (int(row['date']), int(row['product_id']), volatility, returns)

    def __init__(self, pandasrawline, targetid):
        self.__id = int(targetid)
        (self.__date, self.__asset, self.__volatility,
            self.__returns) = self.__raw_conversion(pandasrawline)
        self.__isClassified = False
        self.__localClassification = None
        self.__classificationDetails = dict()
        self.__features = dict()

    def get_date(self):
        return self.__date

    def get_id(self):
        return self.__id

    def get_asset(self):
        return self.__asset

    def get_volatility(self):
        return self.__volatility

    def get_returns(self):
        return self.__returns

    def get_classification(self):
        return self.__localClassification

    def is_classified(self):
        return self.__isClassified

    def set_classification(self, classification, probabilityDictionary):
        self.__isClassified = True
        self.__localClassification = classification
        self.__classificationDetails = probabilityDictionary

    def add_features(self, featuresnames, featuresList):
        self.__features[featuresnames] = featuresList

# KairosAsset handles the KairosDays


class KairosAsset:
    def __init__(self, listKairosDays=[]):
        self.__daysList = sorted(listKairosDays, key=KairosDay.get_date)
        self.__isClassified = False
        self.__averageClassification = None
        self.__classificationDetails = None

    def set_classification(self, classification, probabilityDictionary):
        self.__isClassified = True
        self.__averageClassification = classification
        self.__classificationDetails = probabilityDictionary

    def __getitem__(self, day):
        return self.__daysList[day]

# A KairosBucket handles several days


class KairosBucket:
    def __init__(self, listkairosassets=[]):
        self.__assetslist = listkairosassets
