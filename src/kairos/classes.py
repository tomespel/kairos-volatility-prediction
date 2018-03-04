# This file is part of the KAIROS package
# Developed in London by mehdithomas and tjespel

# classes.py
# This file contains the class definitions


# General elements
import time  # Generation of timestamps in classes
classesliststringdates = [time.strftime('%H:%M:%S', time.gmtime(34200 + i*300)) for i in range(53)]


# KairosDay includes the informations related to a day of volatility

class KairosDay:

    def __rawconversion(self, row):
        volatility = [row.loc['volatility ' + classesliststringdates[i]] for i in range(len(classesliststringdates))]
        returns = [row.loc['return ' + classesliststringdates[i]] for i in range(len(classesliststringdates))]
        returns =[]
        return (int(row['date']), int(row['product_id']), volatility, returns)

    def __init__(self, pandasrawline, targetid):
        self.__id = int(targetid)
        (self.__date, self.__asset, self.__volatility,
            self.__returns) = self.__rawconversion(pandasrawline)
        self.__isclassified = False
        self.__localaverageclassification = None
        self.__classificationdetails = None

    def get_volatility(self):
        return self.__volatility

    def get_returns(self):
        return self.__returns

    def get_classification(self):
        return self.__localaverageclassification

    def is_classified(self):
        return self.__isclassified

    def classify(self, classification, probabilitydictionary):
        self.__isclassified = True
        self.__localaverageclassification = classification
        self.__classificationdetails = probabilitydictionary

# KairosAsset handles the KairosDays


class KairosAsset:
    def __init__(self, listkairosdays=[]):
        self.__dayslist = listkairosdays


# A KairosBucket handles several days


class KairosBucket:
    def __init__(self, listkairosassets=[]):
        self.__assetslist = listkairosassets
