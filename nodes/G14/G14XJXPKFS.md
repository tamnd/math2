---
tag: G14XJXPKFS
kind: concept
name: Cramér–von Mises criterion
msc: [62G10, 62G30]
specializes: [087P03NEND]
sources:
  - url: https://en.wikipedia.org/wiki/Cram%C3%A9r%E2%80%93von_Mises_criterion
same_as:
  wikidata: Q783996
  wikipedia: Cramér–von Mises criterion
---

## Summary

The Cramér–von Mises criterion measures how far an [[empirical distribution function|A05WR6TEK5]] is from a hypothesised [[cumulative distribution function|0H8H7ZTHW2]] by an integrated squared difference.
It gives a goodness-of-fit [[hypothesis test|087P03NEND]] that, like the [[Kolmogorov–Smirnov test|YZYHWC6C5F]], has the same null law for every continuous hypothesised distribution.
Where the Kolmogorov–Smirnov statistic looks at the single largest gap, this criterion adds up the squared gaps over the whole line.
A two-sample version compares two empirical distribution functions.

## Explanations

### L1 human

Picture the staircase of the data and the curve of the expected distribution on one graph.
Instead of looking for the single widest gap, square the gap at every point and average these squares along the curve.
A large average means that the data and the curve disagree over a wide range, not only at one place.
For one observation at $0.5$ tested against the uniform law on $[0, 1]$, the statistic is $1/12$.
