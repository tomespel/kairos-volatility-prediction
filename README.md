# Volatility Prediction in Financial Markets
A repository for the Kairos package developed for CFM's ENS Data Challenge. Further information about this challenge is available at the following [link](https://challengedata.ens.fr/en/challenge/34/volatility_prediction_in_financial_markets.html). The official leaderboard is available at this [address](http://datachallenge.cfm.fr).

## Table of Contents

## Background
Volatility is a fundamental metric in modern finance. In this challenge, we use past volatilities and price changes of financial instruments to predict future volatility and control the risk of financial portfolios.
Here is [the video](https://www.college-de-france.fr/site/stephane-mallat/Prediction-de-volatilite-de-marches-financiers-par-CFM.htm) of the challenge's presentation at Collège de France.

Kairos refers to an [ancient Greek diety](https://en.wikipedia.org/wiki/Kairos). The word καιρός itself means *opportune moment*. In modern greek, it means the weather.

## Features

We have developed the Kairos package for predicting volatility at the end of the day. The package has been developed for the `Python 3.7` language. Dependencies are specified in the package itself.

## Installation

## Usage

### Input Files
The input files should be using the `.csv` format and have the following structure. We recommend using `';'` as separator in the file.

|ID|date|product_id|volatility 09:30:00|...|volatility 13:55:00|return 09:30:00|...|return 13:55:00|
|---|||||||||
|1|1|1|0.6627|...|0.0523|-1|...|-1|
|2|1|2|0.2853|...|0.0711|1|...|-1|
|3|1|3|1.1516|...|0.1179|-1|...|1|

## Contribute and support

The team includes the following members, with the associated GitHub identifiers.

| Name | GitHub id |
| --- | --- |
|Mehdi Tomas|mehditomas|
|Thomas Espel|tjespel|
