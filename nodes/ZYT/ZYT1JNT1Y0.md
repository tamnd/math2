---
tag: ZYT1JNT1Y0
kind: concept
name: Degree of exactness of a quadrature rule
msc: [65D32, 41A55]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_integration
---

## Summary

The degree of exactness of a [[quadrature rule|ADSVMCY77A]] is the largest $d$ such that the rule is exact for all polynomials of degree $\le d$.
It is the standard first measure of the quality of a rule: for smooth integrands, a high degree of exactness usually means a small error.
A rule with $n$ nodes has degree of exactness at most $2n - 1$, and Gaussian quadrature reaches this bound.

## Explanations

### L1 human

Polynomials are the simplest functions, so a good integration recipe should at least get them right.
The degree of exactness counts how far up the ladder $1, x, x^2, x^3, \dots$ the recipe is exact.
The midpoint rule is exact for straight lines but not for $x^2$, so its degree is $1$.
Simpson's rule, with three nodes, is exact even for cubics, so its degree is $3$.
