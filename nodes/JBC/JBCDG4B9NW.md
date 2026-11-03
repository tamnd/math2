---
tag: JBCDG4B9NW
kind: concept
name: Greeks
msc: [91G20, 91G60]
sources:
  - url: https://en.wikipedia.org/wiki/Greeks_(finance)
same_as:
  wikidata: Q1321169
  wikipedia: Greeks (finance)
---

## Summary

The Greeks of a derivative security are the partial derivatives of its price with respect to the inputs of a pricing model.
The main ones are delta, gamma, vega, theta and rho, each named after a Greek letter or a letter-like symbol.
They measure how the price reacts to small moves in the underlying price, the volatility, the time and the interest rate.
Traders use them to hedge, that is, to build portfolios whose value does not move to first order.

## Explanations

### L1 human

An option price depends on several things at once: the stock price, how wild the stock is, how long until expiry, and the interest rate.
Each Greek answers one question of the form "if this one input moves a little, how much does the price move?".
Delta is the slope of the price as a function of the stock price.
For example, if a call option has delta $0.6$, a rise of $1$ in the stock price raises the option price by about $0.6$.
Holding $0.6$ shares against a sold call then cancels this first-order risk.
