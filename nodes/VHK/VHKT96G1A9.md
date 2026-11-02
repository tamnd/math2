---
tag: VHKT96G1A9
kind: definition
name: Gegenbauer transform
msc: [44A20, 33C45]
defines: TMNNRRRGAS
uses: [YCK709QB06, 5TRFA6F79B]
sources:
  - url: https://en.wikipedia.org/wiki/Gegenbauer_polynomials
---

## Definition

Fix a real number $\lambda > -1/2$ with $\lambda \ne 0$, and let $w(x) = (1 - x^2)^{\lambda - 1/2}$ for $-1 < x < 1$.
Let $C_n^{\lambda}$ be the [[Gegenbauer polynomial|5TRFA6F79B]] of degree $n$.
Let $F \colon (-1, 1) \to \C$ be a function such that $w F$ is integrable on $(-1, 1)$.
The *Gegenbauer transform* of $F$ is the sequence
$$f(n) = \int_{-1}^{1} w(x)\, C_n^{\lambda}(x)\, F(x)\, dx, \qquad n = 0, 1, 2, \dots$$

## Remarks

The polynomials $C_n^\lambda$ are orthogonal for $w$, and $F \in L^2(w)$ is recovered as $F = \sum_{n \ge 0} \frac{f(n)}{h_n} C_n^{\lambda}$ with $h_n = \int_{-1}^1 w\, (C_n^\lambda)^2\, dx$.
If $F$ is smooth enough and the boundary terms vanish, the transform of $w^{-1} \frac{d}{dx}\left( (1 - x^2)^{\lambda + 1/2} F' \right)$ is $-n(n + 2\lambda) f(n)$.

Example: $\lambda = 1/2$ gives $w = 1$ and $C_n^{1/2} = P_n$, the Legendre polynomials.
For $F(x) = x$ the transform is $f(1) = \int_{-1}^1 x^2\, dx = 2/3$ and $f(n) = 0$ for $n \ne 1$, since $x = P_1(x)$.

Non-example: for $\lambda = -1/2$ the weight $(1 - x^2)^{-1}$ is not integrable near $\pm 1$, so $F = 1$ has no transform.

The value $\lambda = 0$ is excluded because $C_n^0 = 0$ for $n \ge 1$ in the usual normalization; the Chebyshev polynomials of the first kind take its place.
