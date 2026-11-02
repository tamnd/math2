---
tag: RSNZNG0WA1
kind: concept
name: Askey–Wilson polynomials
msc: [33D45, 33D15]
sources:
  - url: https://en.wikipedia.org/wiki/Askey–Wilson_polynomials
same_as:
  wikidata: Q4807191
  wikipedia: Askey–Wilson polynomials
---

## Summary

The Askey–Wilson polynomials $p_n(x; a, b, c, d \mid q)$ are a family of orthogonal polynomials in one variable with four parameters and a base $q$.
They are defined by a terminating [[basic hypergeometric series|EB4N9RQR51]] ${}_4\phi_3$ in the variable $x = \cos\theta$.
They sit at the top of the $q$-Askey scheme.
The [[continuous q-Hermite polynomials|XFKVZJ55Q5]], the [[Rogers polynomials|7H7SACRYEF]] and many other $q$-orthogonal polynomials are special or limiting cases.
As $q \to 1$ they give the [[Wilson polynomials|1CPF7SWQ3S]].
Askey and Wilson introduced them in 1985.

## Explanations

### L1 human

Classical orthogonal polynomials, like the Legendre or Chebyshev polynomials, are each defined by a formula with few parameters.
The Askey–Wilson polynomials are one formula with five parameters $a, b, c, d, q$ that contains a large number of them as special cases or limits.
They are orthogonal on $[-1, 1]$ for a weight built from infinite products.
For example, the polynomial of degree $1$ is $2(1 - abcd)\, x + (abc + abd + acd + bcd) - (a + b + c + d)$, which is symmetric in the four parameters.
