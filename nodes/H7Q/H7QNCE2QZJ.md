---
tag: H7QNCE2QZJ
kind: concept
name: Newton polygon
msc: [12J25, 11S05]
sources:
  - url: https://en.wikipedia.org/wiki/Newton_polygon
same_as:
  wikidata: Q115646
  wikipedia: Newton polygon
---

## Summary

The Newton polygon of a polynomial over a valued field is a broken line built from its coefficients $a_i$, see the [[definition|D186VNHFZJ]].
It is the lower boundary of the [[convex hull|0FQSDC2EQ2]] of the points $(i, v(a_i))$.
Its slopes and their lengths give the [[valuations|B85T5VKR3M]] of the roots and how many roots have each valuation.
It is a quick tool for factoring polynomials over $p$-adic fields and for finding [[Puiseux series|SENTYNSKSF]] solutions of algebraic equations.

## Explanations

### L1 human

Plot one point for each coefficient: the horizontal position is the power of $X$, the height is how divisible the coefficient is by $p$.
Stretch a string under these points from the leftmost to the rightmost point and pull it tight from below.
The broken line you get is the Newton polygon.
Each straight piece with slope $s$ and width $\ell$ says: exactly $\ell$ roots have valuation $-s$.
For $X^2 + X + p$ the pieces have slopes $-1$ and $0$, so one root is divisible by $p$ and the other is not.
