---
tag: YFKA3KVTGR
kind: concept
name: Holomorphic functional calculus
msc: [47A60, 46H30]
sources:
  - url: https://en.wikipedia.org/wiki/Holomorphic_functional_calculus
same_as:
  wikidata: Q1625064
  wikipedia: Holomorphic functional calculus
---

## Summary

Let $a$ be an element of a unital [[Banach algebra|9KYWN94QDN]], and let $f$ be a [[holomorphic function|0NAHXR1FRH]] on a neighbourhood of the [[spectrum|EH0CZ19RKP]] of $a$.
The holomorphic functional calculus gives a meaning to $f(a)$.
It is defined by a Cauchy integral of $f$ against the [[resolvent|J5YNNKSB9P]] of $a$.
The map $f \mapsto f(a)$ is an algebra homomorphism that extends the evaluation of polynomials, and it satisfies the spectral mapping theorem $\sigma(f(a)) = f(\sigma(a))$.
It works for all bounded operators on a Banach space, not only normal ones, and it gives spectral projections, logarithms and square roots of operators.

## Explanations

### L1 human

For a polynomial $p$ and a square matrix $A$, the matrix $p(A)$ is clear: replace $z$ by $A$.
The holomorphic functional calculus does the same for any function given locally by power series, using Cauchy's integral formula instead of a formula for $f$.
The value $f(\lambda)$ is replaced by the integral of $f(\lambda)$ times $(\lambda - a)^{-1}$ around the spectrum.
For example, if $A = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$ and $f = \exp$, the calculus gives the diagonal matrix with entries $e^2$ and $e^3$.
If the spectrum splits into two parts, the function equal to $1$ near one part and $0$ near the other gives a projection onto the matching invariant subspace.
