---
tag: A6EXFAP5EQ
kind: definition
name: Irregular singularity
msc: [34M03, 34M30, 34M35]
defines: AT1W4MMTYR
uses: [QK2J038VB4, H96HXG6CA0, 0QQRP17Z7S]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_singular_point
---

## Definition

Let $p_1, \ldots, p_n$ be meromorphic functions near $z_0 \in \C$, and consider the [[linear equation|0QQRP17Z7S]]
$$y^{(n)} + p_1(z)\, y^{(n-1)} + \cdots + p_n(z)\, y = 0.$$
The point $z_0$ is an *irregular singular point* (or irregular singularity) if it is a [[singular point|QK2J038VB4]] but not a [[regular singular point|H96HXG6CA0]].
Equivalently, $(z - z_0)^k\, p_k(z)$ is not analytic at $z_0$ for at least one $k \in \set{1, \ldots, n}$.
The point $\infty$ is irregular singular if $w = 0$ is irregular singular for the equation obtained by the substitution $z = 1/w$.

## Remarks

Example: $z^2 y'' + y' = 0$ has $p_1 = \frac{1}{z^2}$, and $z\, p_1 = \frac{1}{z}$ is not analytic at $0$, so $0$ is an irregular singular point.
Its solutions are the constants and $\int e^{1/z}\, dz$, and the derivative $e^{1/z}$ of the latter has an essential singularity at $0$.

Non-example: $z^2 y'' + z y' - y = 0$ has $z p_1 = 1$ and $z^2 p_2 = -1$, both analytic, so $0$ is a regular singular point and not irregular; its solutions are $z$ and $z^{-1}$.

For $n = 2$, the point $\infty$ is irregular for $y'' + p y' + q y = 0$ exactly when $z\, p(z)$ or $z^2 q(z)$ is not analytic at $\infty$.
For example, $\infty$ is irregular for the Bessel equation, the Airy equation $y'' = z y$ and the equation $y'' = y$, whose solutions $e^{\pm z}$ have essential singularities at $\infty$.
