---
tag: C0Z1MKEGZ1
kind: definition
name: Associated Legendre polynomials
msc: [33C45, 33C55]
defines: VPJCSVRY6S
uses: [QFYGJVA996]
sources:
  - url: https://en.wikipedia.org/wiki/Associated_Legendre_polynomials
---

## Definition

Let $\ell$ and $m$ be integers with $0 \le m \le \ell$, and let $P_\ell$ be the [[Legendre polynomial|QFYGJVA996]] of degree $\ell$.
The *associated Legendre polynomial* $P_\ell^m$ is the function on $[-1, 1]$ given by
$$P_\ell^m(x) = (-1)^m (1 - x^2)^{m/2} \frac{d^m}{dx^m} P_\ell(x).$$
For $0 < m \le \ell$ one also sets
$$P_\ell^{-m}(x) = (-1)^m \frac{(\ell - m)!}{(\ell + m)!} P_\ell^m(x).$$

## Remarks

The factor $(-1)^m$ is the Condon–Shortley phase; some authors leave it out.
Examples: $P_\ell^0 = P_\ell$, $P_1^1(x) = -(1 - x^2)^{1/2}$, $P_2^1(x) = -3x (1 - x^2)^{1/2}$ and $P_2^2(x) = 3(1 - x^2)$.
Check for $P_2^2$: $P_2(x) = (3x^2 - 1)/2$ has second derivative $3$, so $P_2^2(x) = (1 - x^2) \cdot 3$.
Each $P_\ell^m$ solves the associated Legendre equation $(1 - x^2) y'' - 2x y' + \left( \ell(\ell + 1) - \frac{m^2}{1 - x^2} \right) y = 0$ on $(-1, 1)$.
For fixed $m$ they are orthogonal: $\int_{-1}^{1} P_k^m(x) P_\ell^m(x) \, dx = \frac{2 (\ell + m)!}{(2\ell + 1)(\ell - m)!} \delta_{k\ell}$.
Non-example: the case $m > \ell$ is excluded, because then the $m$-th derivative of $P_\ell$ is zero and the formula gives only the zero function.
