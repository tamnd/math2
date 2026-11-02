---
tag: AFBY76MAX7
kind: definition
name: Porous medium equation
msc: [35K65, 35K55, 76S05]
defines: DGVNNYKBHC
uses: [1CCTH8X2FT, 0E0B6RA8K0, VP2HN86VAG]
sources:
  - url: https://en.wikipedia.org/wiki/Porous_medium_equation
---

## Definition

Let $\Omega \subseteq \R^n$ be open and let $m > 1$ be a real number.
The *porous medium equation* is the [[parabolic equation|1CCTH8X2FT]] for a function $u \colon \Omega \times (0, T) \to [0, \infty)$:
$$u_t = \Delta (u^m),$$
where $\Delta$ is the [[Laplacian|0E0B6RA8K0]] in $x$.

## Remarks

Example: the Barenblatt solution
$$U(x, t) = t^{-\alpha} \Big( C - k \abs{x}^2 t^{-2\alpha/n} \Big)_+^{1/(m-1)}, \qquad \alpha = \frac{n}{n(m - 1) + 2}, \quad k = \frac{\alpha (m - 1)}{2 m n},$$
with a constant $C > 0$ and $s_+ = \max(s, 0)$, solves the equation on $\R^n \times (0, \infty)$ in the weak sense.
For each $t$ its support is the ball $\abs{x} \le (C/k)^{1/2}\, t^{\alpha/n}$, so it spreads at finite speed.
Non-example: for $m = 1$ the equation is the [[heat equation|VP2HN86VAG]], which is excluded; its solutions with nonnegative nonzero data are positive everywhere for $t > 0$.
Writing $\Delta(u^m) = \nabla \cdot (m u^{m-1} \nabla u)$ shows that the equation is degenerate parabolic where $u = 0$.
The case $0 < m < 1$ is called the fast diffusion equation.
