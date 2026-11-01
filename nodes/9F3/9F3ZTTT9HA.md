---
tag: 9F3ZTTT9HA
kind: concept
name: Cumulant
msc: ["60E10", "62E10"]
sources:
  - url: https://en.wikipedia.org/wiki/Cumulant
same_as:
  wikidata: Q746007
  wikipedia: Cumulant
---

## Summary

The cumulants $\kappa_1, \kappa_2, \dots$ of a real random variable are the Taylor coefficients at $0$ of its [[cumulant generating function|0N2SP6K9ZC]], the logarithm of the [[moment-generating function|0WQVXP7PDB]].
The first cumulant is the [[mean|0WQNRCNY3M]] and the second is the [[variance|0477R9PYAE]].
Cumulants of a sum of [[independent|0GQ938GDE0]] random variables are the sums of their cumulants, which makes them easier to use than [[moments|01XAHPADBA]].
The [[normal distribution|05AQE0QR0D]] is the law whose cumulants of order $3$ and higher all vanish.

## Explanations

### L1 human

Moments of a sum of independent variables mix in a complicated way, but cumulants just add.
The first cumulant tells where the distribution sits, and the second how spread out it is.
The third measures how lopsided it is, and the fourth how heavy its tails are compared with a normal law.
For a [[Poisson|0XB9GQTN9G]] variable with mean $\lambda$, every cumulant equals $\lambda$.
For a normal variable, only the first two cumulants are nonzero.
