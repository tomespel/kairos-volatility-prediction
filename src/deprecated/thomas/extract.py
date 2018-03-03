import pandas as pd
import time

import matplotlib.pyplot as plt

print("Importing data...")
training_input = pd.read_csv('samples/training_input.csv', ';')
print("Data imported.")

class TrainingData:
    def __init__(self, size):
        if size > 1:
            size = 1
        self.data = training_input[: int(size * len(training_input))]
        self.list_dates = []
        self.list_timeindex = []
        for i in range (53):
            self.list_dates.append(time.strftime('%H:%M:%S', time.gmtime(34200 + i*300)))
            self.list_timeindex.append(34200 + i*300)

    def raw_returns(self):
        returns = self.data[["ID", "date", "product_id"] + ["return " + self.list_dates[i] for i in range (53)]]
        returns = returns.rename(columns = dict([("return " + self.list_dates[i], self.list_timeindex[i]) for i in range (53)]))
        return returns.set_index("ID")

    def raw_volatilities(self):
        volatilities = self.data[["ID", "date", "product_id"] + ["volatility " + self.list_dates[i] for i in range (53)]]
        volatilities = volatilities.rename(columns = dict([("volatility " + self.list_dates[i], self.list_timeindex[i]) for i in range (53)]))
        return volatilities.set_index("ID")

    def get_data(self):
        return self.data
