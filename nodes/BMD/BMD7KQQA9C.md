---
tag: BMD7KQQA9C
kind: definition
name: Regular singular point
msc: [34M03, 34M35]
defines: H96HXG6CA0
uses: [QK2J038VB4, 081WKEDK6C, 0QQRP17Z7S, 03F7N3915D]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_singular_point
---

## Definition

Let $p_1, \ldots, p_n$ be meromorphic functions near $z_0 \in \C$, and consider the [[linear equation|0QQRP17Z7S]]
$$y^{(n)} + p_1(z)\, y^{(n-1)} + \cdots + p_n(z)\, y = 0.$$
The point $z_0$ is a *regular singular point* of the equation if:

1. $z_0$ is a [[singular point|QK2J038VB4]] of the equation, and
2. for each $k = 1, \ldots, n$, the function $(z - z_0)^k\, p_k(z)$ is [[analytic|081WKEDK6C]] at $z_0$.

The point $\infty$ is a regular singular point if $w = 0$ is one for the equation obtained by the substitution $z = 1/w$.

## Remarks

For $n = 2$, written $y'' + p(z) y' + q(z) y = 0$, condition 2 says that $(z - z_0) p(z)$ and $(z - z_0)^2 q(z)$ are analytic at $z_0$.
For $n = 2$, the point $\infty$ is ordinary or regular singular if and only if $z\, p(z)$ and $z^2 q(z)$ are analytic at $\infty$.

Example: the [[Cauchy–Euler equation|03F7N3915D]] $z^2 y'' + a z y' + b y = 0$ with $(a, b) \ne (0, 0)$ has $p = \frac{a}{z}$ and $q = \frac{b}{z^2}$.
So $0$ is singular, while $z p = a$ and $z^2 q = b$ are constant; hence $0$ is a regular singular point.

Non-example: for $z^2 y'' + y' = 0$, one has $p = \frac{1}{z^2}$, and $z p = \frac{1}{z}$ is not analytic at $0$.
So $0$ is singular but not regular singular; it is an irregular singular point.

Fuchs proved a characterisation by growth.
A singular point is regular singular if and only if every solution grows at most like a power of $\abs{z - z_0}^{-1}$ as $z \to z_0$ in each sector with vertex $z_0$.
