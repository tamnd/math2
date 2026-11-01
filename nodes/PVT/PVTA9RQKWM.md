---
tag: PVTA9RQKWM
kind: concept
name: Faber polynomials
msc: ["30E10", "30C10", "41A10"]
sources:
  - url: https://en.wikipedia.org/wiki/Faber_polynomials
same_as:
  wikidata: Q4298932
  wikipedia: Faber polynomials
---

## Summary

The Faber polynomials of a compact set $K$ in the plane are polynomials $F_0, F_1, F_2, \dots$, with $F_n$ of degree $n$.
They are built from the [[conformal map|0VHNKP1N3K]] of the complement of $K$ onto the exterior of the unit disc.
They play for $K$ the role that the powers $z^n$ play for a disc.
Functions holomorphic on a neighbourhood of $K$ can be expanded in Faber series $\sum_n b_n F_n(z)$.
They are a standard tool of polynomial approximation and of geometric function theory.

## Explanations

### L1 human

On a disc centred at $0$, the natural building blocks for holomorphic functions are the powers $z^n$.
For another shape, such as an ellipse or a segment, one first straightens its outside into the outside of a circle by a conformal map $\Phi$.
The $n$-th Faber polynomial is the polynomial part of $\Phi(z)^n$ near infinity.
For the closed unit disc, $\Phi(z) = z$ and $F_n(z) = z^n$.
For the segment $[-1, 1]$ one gets twice the Chebyshev polynomials.
