---
tag: EWFSKZAM6Q
kind: definition
name: Polytrope
msc: [85A15]
defines: 9YTGKNPMCP
uses: [4FC5XQA2RK, ANRZZMH2Q0, 5MXPY6QTZ6]
sources:
  - url: https://en.wikipedia.org/wiki/Polytrope
---

## Definition

Let $n \ge 0$ be a real number and let $K > 0$ be a constant.
Consider a spherically symmetric, self-gravitating ball of fluid in [[hydrostatic equilibrium|4FC5XQA2RK]], with pressure $P$ and density $\rho$.
It is a *polytrope of index $n$* if $P = K \rho^{1 + 1/n}$ at every point.
The number $n$ is the *polytropic index* and $\gamma = 1 + 1/n$ is the *polytropic exponent*.

## Remarks

Write $\rho = \rho_c \theta^n$ with $\rho_c$ the central density, and $r = \alpha \xi$ with $\alpha^2 = (n + 1) K \rho_c^{1/n - 1} / (4 \pi G)$, where $G$ is the gravitational constant.
Then hydrostatic equilibrium becomes the [[Lane–Emden equation|ANRZZMH2Q0]] $\xi^{-2} (\xi^2 \theta')' = -\theta^n$ with $\theta(0) = 1$ and $\theta'(0) = 0$, and the surface is the first zero $\xi_1$ of $\theta$.
Example: for $n = 1$ the solution is $\theta = \sin \xi / \xi$, so $\xi_1 = \pi$ and the radius $R = \pi \alpha$ does not depend on the central density.
Example: $n = 0$ gives a ball of uniform density, since $\rho = \rho_c \theta^0$ is constant.
Non-example: an isothermal ideal gas, with $P$ proportional to $\rho$, is the limit $n \to \infty$ and is not a polytrope of finite index; it leads instead to the [[Emden–Chandrasekhar equation|5MXPY6QTZ6]].
A polytrope has finite radius when $0 \le n < 5$; for $n = 5$ the radius is infinite but the mass is finite.
