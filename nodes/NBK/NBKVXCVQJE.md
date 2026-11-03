---
tag: NBKVXCVQJE
kind: concept
name: SABR volatility model
msc: [91G20, 91G30, 60H10]
specializes: [2KQF3JSAQ7]
sources:
  - url: https://en.wikipedia.org/wiki/SABR_volatility_model
same_as:
  wikidata: Q7388452
  wikipedia: SABR volatility model
---

## Summary

The SABR model is a [[stochastic volatility|2KQF3JSAQ7]] model for a forward price or forward rate.
The name stands for "stochastic alpha, beta, rho", after its parameters.
It was introduced by Hagan, Kumar, Lesniewski and Woodward in 2002, together with an asymptotic formula for the [[implied volatility|XNA12XG7ZK]] it produces.
That formula makes it fast to fit the model to a [[volatility smile|2TYE23YVS5]], and it is widely used for interest rate options.

## Explanations

### L1 human

The SABR model describes a forward price whose randomness has a size that itself moves randomly.
One parameter, $\beta$, sets how the size of the moves scales with the level of the forward.
A second parameter sets how wildly the volatility moves, and a third sets how the two noises are correlated.
Together they bend the implied volatility curve into a smile or a skew.
For example, $\beta = 1$ makes moves proportional to the level, as in the Black model.
