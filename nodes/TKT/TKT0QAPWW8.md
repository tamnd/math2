---
tag: TKT0QAPWW8
kind: concept
name: Data assimilation
msc: [86A22, 62M20, "93E11"]
sources:
  - url: https://en.wikipedia.org/wiki/Data_assimilation
same_as:
  wikidata: Q2670177
  wikipedia: Data assimilation
---

## Summary

Data assimilation combines a numerical model of a system with observations of it to estimate the state of the system as well as possible.
The model supplies a prior estimate, the background, and the observations correct it according to the errors expected in each.
It can be seen as a Bayesian [[inverse problem|PCMW7KN5P4]], and in the linear Gaussian case it is a weighted [[least squares|0BYTQ4X1HC]] problem.
It provides the initial conditions of weather forecasts and is used in oceanography, hydrology and many other fields.

## Explanations

### L1 human

A weather model gives a good but imperfect guess of today's weather everywhere, and weather stations, balloons and satellites give accurate but scattered measurements.
Data assimilation blends the two into one best picture of the atmosphere.
Where the measurements are trusted more, the picture follows them; where there are none, it follows the model.
For one number: if the model says $10$ degrees with an uncertainty of $2$ and a thermometer says $12$ with an uncertainty of $1$, the best estimate is $11.6$.
