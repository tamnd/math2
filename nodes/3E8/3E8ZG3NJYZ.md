---
tag: 3E8ZG3NJYZ
kind: concept
name: Multivariate formal power series
msc: [13F25, 13J05]
sources:
  - url: https://en.wikipedia.org/wiki/Formal_power_series
    locator: Power series in several variables
---

## Summary

A formal power series in $X_1, \dots, X_n$ over a [[commutative ring|0310REJJY8]] $R$ is a possibly infinite sum $\sum a_\alpha X^\alpha$ over all monomials $X^\alpha$.
No convergence condition is imposed.
These series form the ring $R[\![X_1, \dots, X_n]\!]$, which extends the one-variable [[formal power series|033WGN00BF]] ring and contains the [[polynomial ring|07GNX8GCYP]] $R[X_1, \dots, X_n]$.
Over a field, this ring is the basic example of a [[complete local ring|G9Q61B8A7C]] and of a regular local ring of dimension $n$.

## Explanations

### L1 human

A polynomial in several variables is a finite sum of monomials such as $3x^2 y$.
A formal power series in several variables allows infinitely many monomials, like $1 + x + y + x^2 + xy + y^2 + \cdots$.
You add and multiply such series as you would polynomials, and every coefficient of a product only needs finitely many terms to compute.
The [[definition|KCBFS516DE]] makes this precise.
