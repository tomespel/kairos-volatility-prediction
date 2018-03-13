# Challenge Information

Source: https://challengedata.ens.fr/en/challenge/34/volatility_prediction_in_financial_markets.html .

## Short description
Use past volatilities and price changes of financial instruments to predict future volatility and control the risk of financial portfolios

Community forum for sharing ideas and making faster progress: http://datachallenge.cfm.fr/
Additional information can also be found on this forum.

Video of the challenge's presentation at Collège de France is available at: https://www.college-de-france.fr/site/stephane-mallat/Prediction-de-volatilite-de-marches-financiers-par-CFM.htm

## Challenge context
The American stock market is the most liquid equity market of the planet and hence provides many opportunities for investments. However, when building a stock portfolio by combining financial assets, we need to estimate its future risk, or volatility. The volatility of an asset is loosely defined as the size of the variations of its price over a period of time: a price that doesn't change between the beginning and the end of a period is more volatile if it fluctuates more during the period; a price that changes smoothly has a higher volatility if its overall change is large. There are multiple ways of capturing these two aspects of volatility. The data uses a unique (but secret) definition. Consequently, it is necessary to estimate the future risk of each individual component of the portfolio. The past volatility of a stock is a good proxy of its future risk, but some intraday patterns remain to be found with cutting edge algorithm. And, this is your challenge.

CFM specializes in developing quantitative trading strategies and building a portfolio from them. Controlling the risk of our client investments is crucial, thus estimating the future risk of financial assets is the cornerstone of our portfolio construction.

## Challenge goals
The goal of the challenge will be to predict the end-of-day volatility for American stocks knowing their past price history's features. American stock markets open at 9:30am and close at 4:00pm, challengers will be provided with trading data between 9:30am and 2:00pm and be asked to predict the volatility between 2:00pm and 4:00pm.

## Data description
The input files contain volatility and return direction of a given set of stocks and dates aggregated over five minute periods. Each line is defined by a unique 'ID' and is related to a given day (defined by a 'date') and a given stock (defined by a 'product_id'). Volatilities are standard deviations of stock prices over five-minute period and are time-stamped (from 9:30am to 1:55pm) by the start time of their computation period, yielding 54 volatility samples for each ‘ID’.
Return directions are the sign of the price change during a five-minute period. Like volatility data, they are time-stamped (from 9:30am to 1:55pm) by the start time of their computation period. Hence, for each ‘ID’, the input files provide 54 return direction values.
The first line of this input file is the header, and columns are separated by semicolons. The three first columns correspond respectively to:
- the 'ID': identification number of the line, it is linked to the forecast IDs provided in the output file
- the 'date': related to a specific day, it is shared between several stocks (for practical reasons, days have been randomized),
- and the 'product_id': identification number of the stock, it is related to a specific company (the stock #236 corresponds to the same company in the training and testing files)
The following columns correspond to volatility over 5-min periods, and then to return direction over 5-min periods. Time stamps are given in military format. For instance, a volatility time-stamped by 10:00:00 is the volatility measured between 10:00am and 10:05am.
Here is an example of an input file:
 ```
ID;date;product_id;volatility 09:30:00;volatility 09:35:00;...;volatility 13:55:00;return 09:30:00;…;return 13:55:00
1;1;1;0.6627;0.7168;...;0.0523;-1;...;-1
2;1;2;0.2853;0. 3795;...;0.0711,1;...;-1
3;1;3;1.1516;1.0935;...;0.1179;-1;...;1
```

The training output file contains the target for each 'ID', where the target is the volatility of the same set of stocks and dates measured between 2:00pm and 4:00pm. The first line of this file is the header and columns are separated by semicolons. The columns correspond respectively to the identification number of the line and the value of the actual volatility for this specific line as shown in the following sample:
```
ID;TARGET
1;0.1341
2;0.0461
3;0.1443
4;0.1301
```
Using the testing_input file, challengers must provide a testing output file in the same format as the training output file (associating with each ID number, the predicted volatility for the 2:00pm - 4:00pm period of time).

Submissions can take up to ten minutes due to the size of the testing output file.

Last but not least, the metric used in this challenge to designate the winning participant will be the mean absolute percentage error [MAPE](https://en.wikipedia.org/wiki/Mean_absolute_percentage_error).
