---
tag: XFKVZJ55Q5
kind: concept
name: Continuous q-Hermite polynomials
msc: [33D45]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_q-Hermite_polynomials
same_as:
  wikidata: Q5165508
  wikipedia: Continuous q-Hermite polynomials
---

## Summary

The continuous $q$-Hermite polynomials $H_n(x \mid q)$ are a family of orthogonal polynomials on $[-1, 1]$ depending on a base $q$.
They are $q$-analogues of the [[Hermite polynomials|MGACY98E9H]], to which they tend after rescaling as $q \to 1$.
At $q = 0$ they are the Chebyshev polynomials of the second kind.
They are one of the simplest families of the $q$-Askey scheme, a special case of the [[Rogers polynomials|7H7SACRYEF]] and of the [[Askey–Wilson polynomials|RSNZNG0WA1]].
They appear in $q$-deformed probability and in the theory of $q$-Gaussian processes.

## Explanations

### L1 human

Write $x = \cos\theta$ and form the sum of $e^{i(n - 2k)\theta}$ over $k = 0, \dots, n$, each weighted by a [[Gaussian binomial coefficient|YS09Z1YNEK]] $\binom{n}{k}_q$.
The result is a polynomial in $x$ of degree $n$, the continuous $q$-Hermite polynomial.
At $q = 0$ all weights are $1$, and the sum is $\frac{\sin((n+1)\theta)}{\sin\theta}$.
For $n = 2$ one gets $H_2(x \mid q) = 4x^2 - (1 - q)$.
