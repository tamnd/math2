---
tag: Z4NV7VK9T9
kind: concept
name: Little q-Jacobi polynomials
msc: [33D45, 33C45]
specializes: [47WJ34NC9K]
sources:
  - url: https://en.wikipedia.org/wiki/Little_q-Jacobi_polynomials
same_as:
  wikidata: Q6652769
  wikipedia: Little q-Jacobi polynomials
---

## Summary

The little $q$-Jacobi polynomials $p_n(x; a, b \mid q)$ are a family of orthogonal polynomials defined by a terminating [[basic hypergeometric series|EB4N9RQR51]].
They are orthogonal for a discrete weight carried by the points $q^k$ with $k = 0, 1, 2, \ldots$.
As $q \to 1$ with $a = q^\alpha$ and $b = q^\beta$, they tend to the [[Jacobi polynomials|TRD7DSF2KR]] in a shifted variable.
They belong to the $q$-analogue of the [[Askey scheme|RR2S05C09B]].

## Explanations

### L1 human

Ordinary Jacobi polynomials are orthogonal for an integral over an interval.
In the little $q$-Jacobi family the integral is replaced by a sum over the points $1, q, q^2, \ldots$, which pile up at $0$.
The parameter $q$ between $0$ and $1$ controls how dense these points are.
The first nontrivial member is the linear polynomial $p_1(x) = 1 - \frac{1 - abq^2}{1 - aq} x$.
Letting $q$ approach $1$ fills the gaps between the points and gives back the classical Jacobi polynomials.
