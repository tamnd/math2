---
tag: FT1YKVBFC9
kind: concept
name: Birkhoff interpolation
msc: [41A05, 65D05]
sources:
  - url: https://en.wikipedia.org/wiki/Birkhoff_interpolation
same_as:
  wikidata: Q3800523
  wikipedia: Birkhoff interpolation
---

## Summary

Birkhoff interpolation asks for a polynomial whose derivatives of chosen orders take chosen values at chosen nodes.
Unlike Hermite interpolation, it does not require that all lower derivatives are also prescribed.
It contains [[polynomial interpolation|SS1YMS2NPC]] and [[Hermite interpolation|9Z50M2WPTP]] as special cases.
Unlike these, it does not always have a unique solution, even when the number of conditions equals the number of coefficients.
The main question of the theory is which patterns of conditions, encoded in an incidence matrix, are poised, that is, solvable uniquely for all data.

## Explanations

### L1 human

Suppose you know the value of a quadratic at $-1$ and at $1$ and its slope at $0$.
That is three conditions for three coefficients, so one might expect exactly one answer.
But for $p(x) = c_0 + c_1 x + c_2 x^2$ the slope at $0$ is $c_1$, and the two values only fix $c_0 + c_2$ and $c_1$.
So the slope is either forced or contradicted, and $c_0$ and $c_2$ are not fixed separately.
Birkhoff interpolation studies when such gaps in the conditions are harmless.
The [[definition|AE08JXN7CA]] sets up the incidence matrix.
