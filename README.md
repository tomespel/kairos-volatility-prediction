# Volatility Prediction in Financial Markets
[![Build Status](https://travis-ci.com/tjespel/kairos-volatility-prediction.svg?token=H7bzknKpKUjcDxrX949q&branch=master)](https://travis-ci.com/tjespel/kairos-volatility-prediction) [![codecov](https://codecov.io/gh/tjespel/kairos-volatility-prediction/branch/master/graph/badge.svg?token=ND0WGgc5Id)](https://codecov.io/gh/tjespel/kairos-volatility-prediction) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Ftjespel%2Fkairos-volatility-prediction.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Ftjespel%2Fkairos-volatility-prediction?ref=badge_shield)

A repository for the Kairos package developed for CFM's ENS Data Challenge. Further information about this challenge is available at the following [link](https://challengedata.ens.fr/en/challenge/34/volatility_prediction_in_financial_markets.html). The official leaderboard is available at this [address](http://datachallenge.cfm.fr).

## Table of Contents

## Background
Volatility is a fundamental metric in modern finance. In this challenge, we use past volatilities and price changes of financial instruments to predict future volatility and control the risk of financial portfolios.
Here is [the video](https://www.college-de-france.fr/site/stephane-mallat/Prediction-de-volatilite-de-marches-financiers-par-CFM.htm) of the challenge's presentation at Collège de France.

Kairos refers to an [ancient Greek deity](https://en.wikipedia.org/wiki/Kairos). The word καιρός itself means *opportune moment*. In modern greek, it means the weather.

## Features

We have developed the Kairos package for predicting volatility at the end of the day. The package has been developed for the `Python 3.7` language. Dependencies are specified in the package itself.

## Installation

## Usage

### Loading the package

In order to use the `Kairos` package functions, you must import it in your `Python 3.7` project.
```
from kairos import *
```
Make sure that all the dependencies are installed. When imported correctly, the package should print the following in the Python console.
```
Kairos features provider imported.
Kairos engine imported.
Kairos succesfully loaded in your project.
```

### Input Files
The input files should be using the `.csv` format and have the following structure. We recommend using `','` as separator in the file.

|ID|date|product_id|volatility 09:30:00|...|volatility 13:55:00|return 09:30:00|...|return 13:55:00|
|---|---|---|---|---|---|---|---|---|
|1|1|1|0.6627|...|0.0523|-1|...|-1|
|2|1|2|0.2853|...|0.0711|1|...|-1|
|3|1|3|1.1516|...|0.1179|-1|...|1|

In order to import a csv file in Kairos, use the following command.
```
myData = kairos.input.from_csv('/csvFilePath/myFile.csv')
```
You can specify the csv delimiter by adding the parameter `contentsDelimiter` in the function.

### File system
Kairos uses a dedicated file system `.krf` to store the data in their current state. In order to store the data, use the following command.
```
kairos.output.freeze(myData, '/pathToFile/myFile.krf')
```
You can restore the data later on using the following command.
```
myData = kairos.input.release('/pathToFile/myFile.krf')
```

The data is structured in one or several `KairosBucket` objects which include `KairosAsset` objects with similar properties. Each `KairosAsset` includes several `KairosDay` objects.

## Credits

The team includes the following members, with the associated GitHub identifiers.

| Name | GitHub id |
| --- | --- |
|Mehdi Tomas|mehditomas|
|Thomas Espel|tjespel|

## License
Apache 2

[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Ftjespel%2Fkairos-volatility-prediction.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Ftjespel%2Fkairos-volatility-prediction?ref=badge_large)
