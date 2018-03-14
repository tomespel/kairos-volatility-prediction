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
        return (int(row['product_id']), int(row['date']), volatility + returns)

    def __init__(self, pandasrawline, targetid, targetValue=None):
        self.__id = int(targetid)
        (self.__asset, self.__date, self.__features) = self.__raw_conversion(pandasrawline)
        self.__featuresIndex = dict([('volatility',(0, 53)),('returns', (53, 53))])
        self.__localClassification = None
        self.__classificationDetails = dict()
        self.__targetValue = targetValue

    def get_date(self):
        return self.__date

    def get_id(self):
        return self.__id

    def get_asset(self):
        return self.__asset

    def get_targetValue(self):
        return self.__targetValue

    def get_allFeatures(self):
        return self.__features

    def get_feature(self, featureName):
        if featureName not in self.__featuresIndex:
            raise Exception('The feature ' + str(featureName) + ' does not exist.')
            return 1
        return self.__features[self.__featuresIndex[featureName][0]:self.__featuresIndex[featureName][0]+self.__featuresIndex[featureName][1]]

    def set_feature(self, featureName, featureValue):
        if self.__featuresIndex[featureName][1] != len(featureValue):
            raise Exception('Size of feature mismatch in set_feature. Expected ' + str(self.__featuresIndex[featureName][1]) + '.')
            return 1
        self.__features[self.__featuresIndex[featureName][0]:self.__featuresIndex[featureName][0]+self.__featuresIndex[featureName][1]] = featureValue
        return 0

    def add_feature(self, featureName, featureValue):
        if featureName in self.__featuresIndex:
            raise Exception('The feature ' + str(featureName) + ' already exists.')
            return 1
        begin = len(self.__features)
        self.__features = self.__features + featureValue
        self.__featuresIndex[featureName] = (begin, len(featureValue))
        return 0

    def get_volatility(self):
        return self.get_feature('volatility')

    def get_returns(self):
        return self.get_feature('returns')

    def get_classification(self):
        return self.__localClassification

    def is_classified(self):
        if self.__localClassification is not None:
            return True
        return False

    def set_classification(self, classification, probabilityDictionary):
        self.__localClassification = classification
        self.__classificationDetails = probabilityDictionary

    def add_features(self, featuresnames, featuresList):
        self.__features[featuresnames] = featuresList
        return 0

    def set_targetValue(self, targetValue):
        self.__targetValue = targetValue
        return 0

# KairosAsset handles the KairosDays


class KairosAsset:
    def __init__(self, listKairosDays=[]):
        self.__daysList = sorted(listKairosDays, key=KairosDay.get_date)
        self.__averageClassification = None
        self.__classificationDetails = None

    def set_classification(self, classification, probabilityDictionary):
        self.__averageClassification = classification
        self.__classificationDetails = probabilityDictionary

    def get_daysNumber(self):
        return len(self.__daysList)

    def __getitem__(self, day):
        return self.__daysList[day]

    def find(self, id):
        for day in self.__daysList:
            if day.get_id() == id:
                return day
        return None

# A KairosBucket handles several days


class KairosBucket:
    def __init__(self, listkairosassets=[]):
        self.__assetsList = listkairosassets

    def get_assetsNumber(self):
        return len(self.__assetsList)

    def __getitem__(self, asset):
        return self.__assetsList[asset]

    def find(self, id):
        for asset in self.__assetsList:
            if asset.find(id) is not None:
                return asset.find(id)
        return None
