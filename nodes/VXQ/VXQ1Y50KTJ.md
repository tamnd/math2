---
tag: VXQ1Y50KTJ
kind: concept
name: Baskakov operator
msc: [41A36, 41A35, 41A25]
sources:
  - url: https://en.wikipedia.org/wiki/Baskakov_operator
same_as:
  wikidata: Q4867603
  wikipedia: Baskakov operator
---

## Summary

The Baskakov operators are [[positive linear operators|AQDXWH4812]] that approximate functions on $[0, \infty)$ by sampling them at the points $k/n$.
Their weights come from the negative binomial distribution.
They belong to a family that also contains the [[Bernstein polynomials|0JT92VK307]] and the [[Szász–Mirakyan operators|GRQJ49XQNR]].

## Explanations

### L1 human

Like the Bernstein and Szász–Mirakyan operators, the Baskakov operator replaces $f(x)$ by a weighted average of the samples $f(k/n)$.
The weights are probabilities, they add up to $1$, and they concentrate near $k/n \approx x$ for large $n$.
Here they come from counting failures before the $n$-th success in repeated trials.
Because the weights have mean $x$, linear functions are reproduced exactly.
