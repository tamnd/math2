---
tag: Y1M82VZYS2
kind: concept
name: Hahn polynomials
msc: [33C45, 42C05]
sources:
  - url: https://en.wikipedia.org/wiki/Hahn_polynomials
same_as:
  wikidata: Q1568814
  wikipedia: Hahn polynomials
---

## Summary

The Hahn polynomials $Q_n(x; \alpha, \beta, N)$ are a finite family of orthogonal polynomials on the points $0, 1, \dots, N$.
Their weight is the beta-binomial distribution, a discrete version of the Jacobi weight.
They are terminating ${}_3F_2$ hypergeometric series and sit in the [[Askey scheme|RR2S05C09B]] just below the Wilson and Racah polynomials.
As $N \to \infty$ after rescaling they tend to the [[Jacobi polynomials|TRD7DSF2KR]], and they also appear as Clebsch–Gordan coefficients of $SU(2)$.

## Explanations

### L1 human

The Jacobi polynomials are perpendicular for a weight on a continuous interval.
Replace the interval by the $N + 1$ points $0, 1, \dots, N$ and the weight by a matching discrete weight.
The polynomials that are perpendicular for this discrete weight are the Hahn polynomials.
For each degree $n$ from $0$ to $N$ there is exactly one of them, normalised to take the value $1$ at $x = 0$.
