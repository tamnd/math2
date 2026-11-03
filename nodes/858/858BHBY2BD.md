---
tag: 858BHBY2BD
kind: concept
name: Risk-neutral measure
msc: [91G20, 60G42]
sources:
  - url: https://en.wikipedia.org/wiki/Risk-neutral_measure
same_as:
  wikidata: Q1058362
  wikipedia: Risk-neutral measure
---

## Summary

A risk-neutral measure, or equivalent martingale measure, is a [[probability measure|059TJN0NZ1]] under which discounted asset prices are [[martingales|0D0GBNDKDH]].
It has the same null sets as the real-world probability, but it gives each asset an expected return equal to the riskless rate.
By the [[fundamental theorem of asset pricing|TYVNND6JN0]], a market has no [[arbitrage|Q626SC54P7]] exactly when such a measure exists.
Prices of derivatives are then discounted expected payoffs under it.

## Explanations

### L1 human

Real investors demand extra return for risk, so real-world probabilities are awkward for pricing.
A risk-neutral measure is a set of make-believe probabilities that build this extra return into the odds.
Under them, every asset earns on average the safe rate, and a price is just an average of future payoffs, discounted.
For a stock at $100$ that will be $120$ or $90$ with no interest, the risk-neutral probability of the up move is $1/3$, since $\frac{1}{3} \cdot 120 + \frac{2}{3} \cdot 90 = 100$.
