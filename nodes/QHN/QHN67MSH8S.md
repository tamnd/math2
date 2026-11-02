---
tag: QHN67MSH8S
kind: concept
name: Inverse distance weighting
msc: [65D05, 41A05, 41A63]
specializes: [BM703GV34G]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_distance_weighting
same_as:
  wikidata: Q1430701
  wikipedia: Inverse distance weighting
---

## Summary

Inverse distance weighting is a simple method of [[multivariate interpolation|BM703GV34G]] for scattered data.
The value at a new point is a weighted average of the data values.
The weight of each data point is a negative power of its distance to the new point.
At a data point the method returns the data value, and near it the weight of that point dominates, so the result is continuous.
It is widely used in geography and engineering because it needs no linear system and its values never leave the range of the data.

## Explanations

### L1 human

To guess the rainfall at a village from nearby rain gauges, trust the closest gauges most.
Inverse distance weighting does exactly this: each gauge gets weight $1/\text{distance}^p$, and the guess is the weighted average.
With two gauges at distances $1$ and $2$ reading $10$ and $40$, and $p = 2$, the weights are $1$ and $1/4$, so the guess is $\frac{10 + 10}{1 + 1/4} = 16$.
At a gauge the distance is $0$, and the method returns the gauge reading itself.
The [[definition|55V8WAJXXJ]] gives the formula.
