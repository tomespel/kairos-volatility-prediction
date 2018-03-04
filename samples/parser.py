import pandas as pd
import random

ratio = 0.2

raw_input = pd.DataFrame.from_csv('training_input.csv', sep=';')
# We take 20% of the products, which means 64 out of 318
products = [i for i in range(1, 319)]
random.shuffle(products)
products = products[:int(318 * ratio + 1)]
# We take 20% of the dates, which means 424 out of 2117
dates = [i for i in range(1, 2117)]
random.shuffle(dates)
dates = dates[:int(2117 * ratio + 1)]

selection = raw_input.loc[raw_input['product_id'].isin(products)].loc[raw_input['date'].isin(dates)]
selection.to_csv('training_input.min.csv')

ids = selection.index.values

raw_output = pd.DataFrame.from_csv('training_output.csv', sep=';')
selection2 = raw_output.loc[raw_output.index.isin(ids)]
selection2.to_csv('training_output.min.csv')
