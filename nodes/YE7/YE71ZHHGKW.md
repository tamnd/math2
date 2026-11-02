---
tag: YE71ZHHGKW
kind: definition
name: Chebyshev constant
msc: [31A15, 30C85, 41A50]
defines: DMNN7E2BYA
uses: [0R6EWFKRCF, 0C3QBCR46M, 8A4GGX1MEY]
sources:
  - url: https://en.wikipedia.org/wiki/Conformal_radius
---

## Definition

Let $K$ be a [[compact set|0R6EWFKRCF]] in $\C$ with at least one point.
For a polynomial $p$, let $\norm{p}_K = \max_{z \in K} \abs{p(z)}$.
For an integer $n \ge 1$, let
$$t_n(K) = \inf \set{ \norm{p}_K : p \text{ a monic polynomial of degree } n }.$$
The *Chebyshev constant* of $K$ is $\tau(K) = \lim_{n \to \infty} t_n(K)^{1/n}$.

## Remarks

The infimum is attained, and a [[monic polynomial|0C3QBCR46M]] $p$ of degree $n$ with $\norm{p}_K = t_n(K)$ is a Chebyshev polynomial of $K$.
Since a product of monic polynomials is monic, $t_{m+n}(K) \le t_m(K) \, t_n(K)$.
So the sequence $\log t_n(K)$ is subadditive, and [[Fekete's lemma|8A4GGX1MEY]] shows that the limit exists and equals $\inf_n t_n(K)^{1/n}$.

Example: let $K$ be the unit circle.
For a monic $p(z) = z^n + a_{n-1} z^{n-1} + \cdots + a_0$, Parseval's identity gives $\frac{1}{2\pi} \int_0^{2\pi} \abs{p(e^{i\theta})}^2 \, d\theta = 1 + \sum_k \abs{a_k}^2 \ge 1$.
So $\norm{p}_K \ge 1$, with equality for $p = z^n$, and $t_n(K) = 1$ and $\tau(K) = 1$.

Non-example: the polynomial $2 z^n$ has maximum $2$ on the unit circle, but it is not monic, so it does not enter the infimum.
Without the monic condition the infimum would be $0$.

If $K$ is a finite set with $m$ points, then $p(z) = \prod_{a \in K} (z - a)$ vanishes on $K$, so $t_n(K) = 0$ for $n \ge m$ and $\tau(K) = 0$.
