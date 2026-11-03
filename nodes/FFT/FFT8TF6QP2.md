---
tag: FFT8TF6QP2
kind: concept
name: Black–Scholes model
msc: [91G20, 60H30]
sources:
  - url: https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model
same_as:
  wikidata: Q1338307
  wikipedia: Black–Scholes model
---

## Summary

The Black–Scholes model is a continuous-time model of a market with a riskless bond and a stock whose price follows a [[geometric Brownian motion|D48DR46B97]].
Options can be hedged perfectly in it, so their prices solve the [[Black–Scholes equation|ZFTNJ2YREG]].
For European calls and puts this gives the closed-form Black–Scholes formula.
It was published by Fischer Black and Myron Scholes, and by Robert Merton, in 1973, and it is the reference model of option pricing.

## Explanations

### L1 human

In this model the stock price wiggles randomly, with a typical size of percentage moves measured by the volatility $\sigma$.
By continuously adjusting a mix of stock and cash, a trader can copy the payoff of an option exactly.
So the option is worth what this copying strategy costs.
The resulting price depends on the volatility but not on the average growth rate of the stock.
