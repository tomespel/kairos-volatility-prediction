# This file is part of the KAIROS package
# Developed in London by mehdithomas and tjespel

# input.py
# This file contains the functions used to extract the data from the samples

import kairos.classes
import csv
import pickle


# Utility functions

def _days_creator(csvReader, targetsList=None):
    outputList = []
    indexes = next(csvReader)
    if targetsList is not None:
        for row in csvReader:
            outputList.append(kairos.classes.KairosDay(dict(zip(indexes[1:],row[1:])), row[0], targetsList[row[0]]))
    else :
        for row in csvReader:
            outputList.append(kairos.classes.KairosDay(dict(zip(indexes[1:],row[1:])), row[0]))
    return outputList


def _assets_creator(daysList):
    tradedAssetsList = list(set([day.get_asset() for day in daysList]))
    assetsList = []
    for tradedAsset in tradedAssetsList:
        assetsList.append(kairos.classes.KairosAsset([day for day in daysList if day.get_asset() == tradedAsset]))
    return assetsList


def _days_getTagetOutputs(csvReader):
    targetOutputs = dict()
    next(csvReader)
    for row in csvReader:
        [tagetId, targetValue] = row
        targetOutputs[tagetId] = float(targetValue)
    return targetOutputs

# User access


def from_csv(pathToInputFile, pathToOutputFile=None, contentsDelimiter=','):

    targets = None
    if pathToOutputFile is not None:
        with open(pathToOutputFile, 'r') as inputFile:
            reader = csv.reader(inputFile, delimiter = contentsDelimiter, quotechar="'", quoting=csv.QUOTE_ALL)
            targets = _days_getTagetOutputs(reader)

    with open(pathToInputFile, 'r') as inputFile:
        reader = csv.reader(inputFile, delimiter = contentsDelimiter, quotechar="'", quoting=csv.QUOTE_ALL)
        elements = _days_creator(reader, targets)
        elements = _assets_creator(elements)
    elements = kairos.classes.KairosBucket(elements)

    return elements


def release(pathToFile):
    fileReader = open(pathToFile, 'rb')
    return pickle.load(fileReader)
