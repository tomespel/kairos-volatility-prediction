# This file is part of the KAIROS package
# Developed in London by mehdithomas and tjespel

# Output.py
# This file contains the functions used to create the output in the standard format

import pickle


def freeze(objects, pathToFile):
    fileHandler = open(pathToFile, 'wb')
    pickle.dump(objects, fileHandler)
    print('Kairos has saved the objects.')
    return 0
