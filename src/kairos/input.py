# This file is part of the KAIROS package
# Developed in London by mehdithomas and tjespel

# input.py
# This file contains the functions used to extract the data from the samples

import kairos.classes
import csv


# Utility functions

def _elements_creator(csvReader):
    outputList = []
    indexes = next(csvReader)
    for row in csvReader:
        outputList.append(kairos.classes.KairosDay(dict(zip(indexes[1:],row[1:])), row[0]))
    return outputList


def _days_creator(daysList):
    tradedAssetsList = list(set([day.get_asset() for day in daysList]))
    assetsList = []
    for tradedAsset in tradedAssetsList:
        assetsList.append(kairos.classes.KairosAsset([day for day in daysList if day.get_asset() == tradedAsset]))
    return assetsList

# User access

def from_csv(pathToFile, contentsDelimiter=','):
    with open(pathToFile, 'r') as inputFile:
        reader = csv.reader(inputFile, delimiter = contentsDelimiter, quotechar="'", quoting=csv.QUOTE_ALL)
        elements = _elements_creator(reader)
        elements = _days_creator(elements)
    return elements
