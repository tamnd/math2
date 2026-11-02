---
tag: R8SNG5TBKJ
kind: concept
name: Zolotarev polynomials
msc: [41A50, 41A10, 33C45]
sources:
  - url: https://en.wikipedia.org/wiki/Zolotarev_polynomials
same_as:
  wikidata: Q104845847
  wikipedia: Zolotarev polynomials
---

## Summary

Zolotarev polynomials solve an extremal problem close to the one solved by [[Chebyshev polynomials|M6EAR1JHPP]].
Among the real polynomials of degree $n$ whose two leading coefficients are fixed, they have the least maximum absolute value on $[-1, 1]$.
Yegor Zolotarev studied them in the nineteenth century, and in general they are expressed through elliptic functions.

## Explanations

### L1 human

The Chebyshev problem fixes only the leading coefficient and asks for the polynomial that stays smallest on $[-1, 1]$.
The Zolotarev problem fixes the first two coefficients and asks the same question.
When the second coefficient is $0$, the answer is still the scaled Chebyshev polynomial $2^{1-n} T_n$.
When the second coefficient is large, the optimal polynomial still wiggles between two equal bounds, but its shape is more complicated.
