---
tag: CAPWE7KWRY
kind: definition
name: Gegenbauer polynomials
msc: [33C45, 33C55]
defines: 5TRFA6F79B
uses: [0PHAC833JF]
sources:
  - url: https://en.wikipedia.org/wiki/Gegenbauer_polynomials
---

## Definition

Let $\lambda > -\frac12$ be a real number with $\lambda \ne 0$.
The *Gegenbauer polynomials* $C_n^{(\lambda)}$, $n \ge 0$, are the polynomials defined by the [[generating function|0PHAC833JF]]
$$\frac{1}{(1 - 2xt + t^2)^{\lambda}} = \sum_{n=0}^{\infty} C_n^{(\lambda)}(x) \, t^n,$$
valid for $x \in [-1, 1]$ and $\abs{t} < 1$.

## Remarks

Equivalently, $C_0^{(\lambda)} = 1$, $C_1^{(\lambda)} = 2\lambda x$ and $(n + 1) C_{n+1}^{(\lambda)} = 2(n + \lambda) x \, C_n^{(\lambda)} - (n + 2\lambda - 1) C_{n-1}^{(\lambda)}$ for $n \ge 1$.
Example: $C_2^{(\lambda)}(x) = 2\lambda(\lambda + 1) x^2 - \lambda$.
Check: with $u = 2xt - t^2$, the expansion $(1 - u)^{-\lambda} = 1 + \lambda u + \frac{\lambda(\lambda + 1)}{2} u^2 + \cdots$ has $t^2$-coefficient $-\lambda + 2\lambda(\lambda + 1) x^2$.
They are orthogonal: $\int_{-1}^{1} C_m^{(\lambda)}(x) C_n^{(\lambda)}(x) (1 - x^2)^{\lambda - 1/2} \, dx = 0$ for $m \ne n$.
Special cases: $C_n^{(1/2)}$ is the [[Legendre polynomial|QFYGJVA996]] $P_n$, and $C_n^{(1)}$ is the [[Chebyshev polynomial of the second kind|7CATGEN6KH]] $U_n$.
Non-example: $\lambda = 0$ is excluded, because the generating function is then the constant $1$ and gives $C_n^{(0)} = 0$ for all $n \ge 1$.
