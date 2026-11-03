---
tag: 2KQF3JSAQ7
kind: concept
name: Stochastic volatility
msc: [91G20, 60H10]
sources:
  - url: https://en.wikipedia.org/wiki/Stochastic_volatility
same_as:
  wikidata: Q596307
  wikipedia: Stochastic volatility
---

## Summary

A stochastic volatility model treats the volatility of an asset price as a random process of its own, instead of a constant.
The asset price and its variance are driven by two [[Brownian motions|22735FGJV6]], which may be correlated.
Such models produce fat tails in the returns and a [[volatility smile|2TYE23YVS5]] in option prices.
The [[Heston model|6PA46G33BB]] and the [[SABR model|NBKVXCVQJE]] are the best known examples.

## Explanations

### L1 human

In the Black–Scholes model the size of the random price moves is fixed once and for all.
Real markets have calm periods and nervous periods, and the nervousness itself changes in an unpredictable way.
A stochastic volatility model lets the volatility wander randomly, like a second price.
For instance, the variance may drift back towards a long-run level while being shaken by its own noise.
When prices fall, volatility often rises, and a negative correlation between the two noises captures this.
