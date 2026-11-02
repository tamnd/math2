---
tag: AAN6HWAC4A
kind: definition
name: Legendre functions
msc: [33C45, 33C05]
defines: 69XMERM6KJ
uses: [463X5V31D9, 0NT64JV96A]
sources:
  - url: https://en.wikipedia.org/wiki/Legendre_function
---

## Definition

Let $\nu, \mu \in \C$.
The *general Legendre equation* is the [[ordinary differential equation|0NT64JV96A]]
$$(1 - z^2) w'' - 2z w' + \left( \nu(\nu + 1) - \frac{\mu^2}{1 - z^2} \right) w = 0.$$
A *Legendre function* of degree $\nu$ and order $\mu$ is a solution $w$ of this equation on a domain of $\C \setminus \set{-1, 1}$.
The *Legendre function of the first kind* of degree $\nu$ and order $0$ is
$$P_\nu(z) = {}_2F_1\left( -\nu, \nu + 1; 1; \frac{1 - z}{2} \right),$$
where ${}_2F_1$ is the [[hypergeometric function|463X5V31D9]].
The series converges for $\abs{1 - z} < 2$, and $P_\nu$ extends analytically to $\C \setminus (-\infty, -1]$.

## Remarks

For $\nu = n$ a nonnegative integer, the factor $(-n)_k$ vanishes for $k > n$, the series stops, and $P_n$ is the [[Legendre polynomial|QFYGJVA996]] of degree $n$.
Check for $n = 1$: $P_1(z) = 1 + \frac{(-1)(2)}{1} \cdot \frac{1 - z}{2} = z$.
For $\mu = 0$ the equation is [[Legendre's equation|W6VE30V10Y]] with $\lambda = \nu(\nu + 1)$.
A second, independent solution is the Legendre function of the second kind $Q_\nu$; for example $Q_0(x) = \frac12 \ln \frac{1 + x}{1 - x}$ for $-1 < x < 1$.
Non-example: $w(z) = z^2$ is not a Legendre function of order $0$ for any $\nu$, since the equation would require $2 - 6z^2 + \nu(\nu + 1) z^2 = 0$ for all $z$, which fails at $z = 0$.
For general order $\mu$ the functions $P_\nu^\mu$ and $Q_\nu^\mu$ are also given by hypergeometric functions, with a factor $\left( \frac{z + 1}{z - 1} \right)^{\mu/2}$ in front.
