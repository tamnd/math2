---
tag: 2TYE23YVS5
kind: concept
name: Volatility smile
msc: [91G20, 91G70]
sources:
  - url: https://en.wikipedia.org/wiki/Volatility_smile
same_as:
  wikidata: Q915788
  wikipedia: Volatility smile
---

## Summary

The volatility smile is the graph of the [[implied volatility|XNA12XG7ZK]] of options on one asset with one maturity, as a function of the strike price.
In the [[Black–Scholes model|FFT8TF6QP2]] this graph would be a flat line, but market data show a curve, often U-shaped or sloping down.
The shape shows that the market assigns heavier tails to the price distribution than the lognormal law of Black–Scholes.
Models such as [[local volatility|GSX1KFCB65]] and [[stochastic volatility|2KQF3JSAQ7]] were built to reproduce it.

## Explanations

### L1 human

Take all call options on one stock that expire on the same day, and compute the implied volatility of each.
Plot these numbers against the strike prices.
If the Black–Scholes model were right, the points would lie on a horizontal line.
In real markets they bend: options far from the current price often have higher implied volatility, which draws a smile.
For stock indices the curve usually falls as the strike grows, and it is then called a skew.
