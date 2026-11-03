---
tag: A59QR1A8JB
kind: definition
name: Critical phenomena
msc: [82B27, 82B26]
defines: 57789VKKAY
uses: [FPYQWE8X12, ENWMTRJRND, R0KGM32QN6]
sources:
  - url: https://en.wikipedia.org/wiki/Critical_phenomena
---

## Definition

Consider a lattice system in the [[thermodynamic limit|FPYQWE8X12]] with free energy density $f(T, h)$, where $T > 0$ is the temperature and $h$ is an external field.
Let $\xi(T, h)$ be its correlation length, the decay rate of the truncated two-point [[correlation function|ENWMTRJRND]].
A point $(T_c, h_c)$ is a *critical point* if:

1. $f$ is not real-analytic at $(T_c, h_c)$;
2. the first partial derivatives of $f$ are continuous at $(T_c, h_c)$, so that the transition is continuous;
3. $\xi(T, h) \to \infty$ as $(T, h) \to (T_c, h_c)$.

*Critical phenomena* are the behaviours of the thermodynamic quantities and of the correlation functions as $(T, h) \to (T_c, h_c)$, and at the critical point itself.

## Remarks

Example: the [[Ising model|R0KGM32QN6]] on $\Z^2$ with coupling $J$ has a critical point at $h_c = 0$ and $\sinh(2 J / (k_B T_c)) = 1$.
Onsager's solution shows that $f$ is singular there with a logarithmic specific heat, while the magnetization tends continuously to $0$ and $\xi \to \infty$.

Non-example: the same model at $T < T_c$ and $h = 0$.
The magnetization $\partial f / \partial h$ jumps from $-m^*$ to $m^*$ when $h$ crosses $0$, so clause 2 fails, and $\xi$ stays finite; the transition is first order.

Typical critical phenomena are power laws $\abs{T - T_c}^{\lambda}$, whose powers are the [[critical exponents|SQ41AZGZ2P]], and the power-law decay of correlations at $(T_c, h_c)$.
