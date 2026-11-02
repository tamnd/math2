---
tag: PY6K9AWR33
kind: concept
name: Reciprocal gamma function
msc: [33B15, 30D15]
specializes: [0G4F0XB9X2]
sources:
  - url: https://en.wikipedia.org/wiki/Reciprocal_gamma_function
same_as:
  wikidata: Q4810025
  wikipedia: Reciprocal gamma function
---

## Summary

The reciprocal gamma function is the function $z \mapsto 1/\Gamma(z)$, where $\Gamma$ is the [[gamma function|0H5SYBSED9]].
Because $\Gamma$ has no zeros and only simple poles at $0, -1, -2, \ldots$, the reciprocal is an [[entire function|0G4F0XB9X2]] with simple zeros exactly at these points.
It is often more convenient than $\Gamma$ itself: it has an everywhere convergent [[Weierstrass product|53MZ2DGDTQ]] and a [[Hankel contour integral|2V0TG9Z3ZW]] valid for all $z$.

## Explanations

### L1 human

The gamma function has infinitely many points where it blows up.
Turning it upside down, $1/\Gamma$, changes these points into ordinary zeros, and the result is defined and smooth on the whole complex plane.
For example $1/\Gamma(1) = 1$, $1/\Gamma(\tfrac12) = 1/\sqrt{\pi}$, and $1/\Gamma(0) = 0$.
On the positive real axis it starts at $0$, rises to a maximum between $1$ and $2$, and then decays very fast, like one over a factorial.
