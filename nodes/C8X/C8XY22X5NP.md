---
tag: C8XY22X5NP
kind: statement
role: theorem
name: Müntz–Szász theorem
msc: [41A30, 41A10]
uses: [XAARVNKXF1, 0BSJSX7ME2, 0X3WGX95FE]
about: [XAARVNKXF1]
sources:
  - url: https://en.wikipedia.org/wiki/M%C3%BCntz%E2%80%93Sz%C3%A1sz_theorem
same_as:
  wikidata: Q3527129
  wikipedia: Müntz–Szász theorem
---

## Statement

Let $0 < \lambda_1 < \lambda_2 < \cdots$ be real numbers with $\lambda_n \to \infty$.
Let $C[0, 1]$ be the space of [[continuous functions|0X3WGX95FE]] $[0, 1] \to \R$ with the supremum norm.
Then the linear span of the functions $1, x^{\lambda_1}, x^{\lambda_2}, \dots$ is [[dense|0BSJSX7ME2]] in $C[0, 1]$ if and only if
$$\sum_{n=1}^{\infty} \frac{1}{\lambda_n} = \infty.$$

## Remarks

The idea of the proof: one first works in $L^2[0, 1]$.
There the distance from $x^m$ to the span of finitely many powers $x^{\lambda_k}$ can be computed exactly with Gram determinants, which here are Cauchy determinants.
The distance is a product of factors $\abs{m - \lambda_k} / (m + \lambda_k + 1)$ times a constant, and this product tends to $0$ exactly when $\sum 1/\lambda_k$ diverges.
A further argument passes from $L^2$ to [[uniform approximation|XAARVNKXF1]] of the monomials $x^m$, and then the Weierstrass theorem finishes the proof.

Example: the exponents $\lambda_n = n$ give the ordinary polynomials, and $\sum 1/n = \infty$, which recovers the Weierstrass approximation theorem on $[0, 1]$.
The primes also work, since $\sum 1/p = \infty$, so combinations of $1$ and $x^p$ for primes $p$ are dense.
The squares do not: $\sum 1/n^2 < \infty$, so the combinations of $1, x, x^4, x^9, \dots$ are not dense in $C[0, 1]$.

The constant function $1$ is needed in the span: every $x^{\lambda_n}$ vanishes at $0$, so without $1$ no function with $f(0) \ne 0$ could be approximated.

## Explanations

### L1 human

Polynomials can approximate every continuous function on $[0, 1]$.
The theorem asks what happens if you may use only some of the powers of $x$.
The answer is a single counting test: you need enough powers, in the sense that the sum of the reciprocals of the exponents is infinite.

### L2 human

The theorem sharpens the Weierstrass theorem and shows how much freedom there is in choosing building blocks.
It is a classic application of complex analysis and Hilbert space methods to approximation; a common proof uses the zeros of bounded analytic functions in a half-plane.
When the series converges, the proof shows more: no power $x^\lambda$ with $\lambda > 0$ outside the set $\set{\lambda_n}$ lies in the closure of the span.
