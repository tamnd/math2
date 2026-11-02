---
tag: HZRC5N7M9E
kind: definition
name: Chebyshev system
msc: [41A50, 41A52, 41A05]
defines: NY5AK617TR
uses: [0TVJZYB6SH, 0S1FJ8VEX9, 0X3WGX95FE, 00KDZRW4C0]
sources:
  - url: https://en.wikipedia.org/wiki/Equioscillation_theorem
---

## Definition

Let $K$ be a [[compact|0TVJZYB6SH]] [[Hausdorff space|0S1FJ8VEX9]] with at least $n$ points, and let $u_1, \dots, u_n \colon K \to \R$ be [[continuous functions|0X3WGX95FE]].
The family $(u_1, \dots, u_n)$ is a *Chebyshev system* (or *Haar system*) on $K$ if the following holds.
Every linear combination $c_1 u_1 + \cdots + c_n u_n$ with $(c_1, \dots, c_n) \ne 0$ has at most $n - 1$ zeros in $K$.
An $n$-dimensional subspace of $C(K)$ is a *Haar subspace* if it has a basis that is a Chebyshev system.

## Remarks

Equivalently, the [[determinant|00KDZRW4C0]] $\det \big( u_i(x_j) \big)_{i, j = 1}^{n}$ is nonzero for all distinct $x_1, \dots, x_n \in K$.
Equivalently, for all distinct $x_1, \dots, x_n \in K$ and all $y_1, \dots, y_n \in \R$ there is exactly one combination $u = \sum c_i u_i$ with $u(x_j) = y_j$ for all $j$.

Example: $1, x, \dots, x^{n-1}$ on $[a, b]$.
A nonzero polynomial of degree at most $n - 1$ has at most $n - 1$ roots.

Non-example: $1, x^2$ on $[-1, 1]$, with $n = 2$.
The combination $x^2 - 1$ is nonzero but has two zeros, $\pm 1$, more than $n - 1 = 1$.

The trigonometric polynomials of degree at most $m$ form a Haar subspace of dimension $2m + 1$ on the circle $\R / 2\pi\Z$: a nonzero one has at most $2m$ zeros in a period.
