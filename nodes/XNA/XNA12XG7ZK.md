---
tag: XNA12XG7ZK
kind: concept
name: Implied volatility
msc: [91G20, 91G70]
sources:
  - url: https://en.wikipedia.org/wiki/Implied_volatility
same_as:
  wikidata: Q1660345
  wikipedia: Implied volatility
---

## Summary

The implied volatility of an option is the volatility that, put into the [[Black–Scholes model|FFT8TF6QP2]], reproduces the observed market price of the option.
It turns a price into a number on a common scale, so that options with different strikes and maturities can be compared.
Markets often quote options by their implied volatility instead of their price.
If the Black–Scholes model were exact, all options on one asset would have the same implied volatility.

## Explanations

### L1 human

The Black–Scholes formula takes a volatility and returns an option price.
Implied volatility runs this formula backwards: it takes the price seen in the market and returns the volatility.
This works because a higher volatility always gives a higher option price, so each price matches exactly one volatility.
For example, if a call trades at the price that the formula gives for $\sigma = 0.25$, its implied volatility is $25\%$ per year.
