---
tag: CEHQSTM1NY
kind: concept
name: Binomial options pricing model
msc: [91G20, 91G60]
sources:
  - url: https://en.wikipedia.org/wiki/Binomial_options_pricing_model
same_as:
  wikidata: Q1138253
  wikipedia: Binomial options pricing model
---

## Summary

The binomial options pricing model is a discrete-time model in which the stock price moves up or down by fixed factors in each period.
It is a [[complete market|A1V152H2CA]] without [[arbitrage|Q626SC54P7]], so every option has a unique price, computed backwards through a tree.
The price is a discounted expectation under an explicit [[risk-neutral measure|858BHBY2BD]].
It was introduced by Cox, Ross and Rubinstein in 1979 and is used both as a teaching model and as a numerical method.

## Explanations

### L1 human

Imagine that each day a stock either goes up by a fixed factor or down by a fixed factor.
After a few days the possible prices form a tree.
At the end of the tree the value of an option is just its payoff.
Working backwards one step at a time, each node's value is a weighted average of the two values after it, discounted.
These weights are not the real odds but the ones that make the stock itself fairly priced.
