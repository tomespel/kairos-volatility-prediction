import thomas.extract as extract
import matplotlib.pyplot as plt

training = extract.TrainingData(0.005)
training.get_data().head()

# There are 318 products.

all_returns = training.raw_returns()
all_returns = all_returns.loc[all_returns['product_id']==1]

for index in all_returns.index:
    plt.plot(all_returns.loc[index].drop(["date", "product_id"]), label= int(all_returns.loc[index]["date"]))
plt.legend()
plt.title("Evolution of returns for product 1 at different dates")
plt.show()

all_volatilities = training.raw_volatilities()
all_volatilities = all_volatilities.loc[all_volatilities['product_id']==1]

for index in all_volatilities.index:
    plt.plot(all_volatilities.loc[index].drop(["date", "product_id"]), label= int(all_volatilities.loc[index]["date"]))
plt.legend()
plt.title("Evolution of volatilities for product 1 at different dates")
plt.show()
