---
tag: QMY5JTZZB8
kind: concept
name: Laurent polynomial ring
msc: [16S36, 13F20]
specializes: [1HM7ZYMPD7]
sources:
  - url: https://en.wikipedia.org/wiki/Laurent_polynomial
---

## Summary

The Laurent polynomial ring $R[x, x^{-1}]$ over a [[ring|0B1261B5ED]] $R$ consists of finite sums $\sum a_i x^i$ in which the exponents $i$ may be negative.
It is the [[monoid ring|1HM7ZYMPD7]] of the additive group $\Z$ over $R$.
In it the variable $x$ is a [[unit|0XVEZDE9J8]] with inverse $x^{-1}$.
It is the group ring of the infinite cyclic group.
Over a field it is the coordinate ring of the line with the origin removed.

## Explanations

### L1 human

A Laurent polynomial is a polynomial that may also contain negative powers of the variable, like $3x^{-2} + 1 + 5x$.
There are still only finitely many terms.
Adding and multiplying works as for polynomials, with the rule $x^i x^j = x^{i+j}$ for all integers $i, j$.
For example, $(x + x^{-1})^2 = x^2 + 2 + x^{-2}$.
The point of the construction is that $x$ now has an inverse, which it does not have among ordinary polynomials.
