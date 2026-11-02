---
tag: CMXHRNWY35
kind: concept
name: Backward error analysis
msc: [65G50, 65F35]
sources:
  - url: https://en.wikipedia.org/wiki/Error_analysis_(mathematics)
---

## Summary

Backward error analysis studies a computed answer by asking for which nearby input it is the exact answer.
The size of that input change is the backward error.
The error of the answer, the forward error, is then bounded by about the [[condition number|AB3S6MHJ8X]] times the backward error.
This splits the analysis into a property of the algorithm (small backward error, that is, [[numerical stability|1AKB4XHMTH]]) and a property of the problem (its conditioning).
It was developed and made systematic by James H. Wilkinson in his work on numerical linear algebra.

## Explanations

### L1 human

Instead of asking "how wrong is my answer?", backward error analysis asks "for which slightly different question is my answer exactly right?".
If the question had to change only by an amount comparable to the rounding errors, the algorithm did as well as one can hope.
For example, a computed root $\hat r$ of a polynomial may be an exact root of a polynomial whose coefficients differ from the given ones only in the last digit.
Whether the answer is then close to the true root depends on how sensitive the problem is, not on the algorithm.
