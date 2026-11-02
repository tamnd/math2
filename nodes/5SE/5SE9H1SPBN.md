---
tag: 5SE9H1SPBN
kind: concept
name: L-curve
msc: [65F22, 65J20]
sources:
  - url: https://en.wikipedia.org/wiki/L-curve
same_as:
  wikidata: Q136463112
  wikipedia: L-curve
---

## Summary

The L-curve is a log-log plot of the size of the regularized solution against the size of the residual.
Each point corresponds to one value of the regularization parameter.
For many discrete ill-posed problems the curve is L-shaped.
The parameter at the corner of the L balances fitting the data against amplifying the noise, and choosing it is the L-curve criterion for [[regularization|WTY54BFC46]].

## Explanations

### L1 human

In Tikhonov regularization a parameter controls how much the solution is smoothed.
Small values fit the data closely but let noise blow up the solution.
Large values keep the solution small but fit the data poorly.
Plotting the two errors against each other on logarithmic axes gives an L-shaped curve with a steep part and a flat part.
The corner is a natural compromise, where neither error can be reduced much without a large increase of the other.
