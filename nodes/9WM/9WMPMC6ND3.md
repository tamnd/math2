---
tag: 9WMPMC6ND3
kind: definition
name: Landau theory
msc: [82B26, 82B27]
defines: XJ4NRM74W6
uses: [XSA203109Z, SQ41AZGZ2P]
sources:
  - url: https://en.wikipedia.org/wiki/Landau_theory
---

## Definition

Let $m \in \R$ be a scalar [[order parameter|XSA203109Z]] whose symmetry group acts by $m \mapsto -m$.
Let $T$ be the temperature, $T_c > 0$ a critical temperature, and $h \in \R$ an external field conjugate to $m$.
The *Landau theory* of the transition is given by a Landau free energy density
$$f_L(m; T, h) = f_0(T) + a_0 (T - T_c) \, m^2 + b \, m^4 - h m,$$
where:

1. $f_0$ is a smooth function of $T$ and $a_0 > 0$, $b > 0$ are constants;
2. without field ($h = 0$), $f_L$ is even in $m$, as the symmetry requires;
3. the equilibrium order parameter $m(T, h)$ is a global minimizer of $m \mapsto f_L(m; T, h)$, and the free energy density is $f(T, h) = \min_m f_L(m; T, h)$.

## Remarks

Example: at $h = 0$, set $a = a_0 (T - T_c)$.
The equation $2 a m + 4 b m^3 = 0$ and the sign of $f_L$ give $m = 0$ for $T \ge T_c$ and $m = \pm \sqrt{a_0 (T_c - T) / (2b)}$ for $T < T_c$.
So $m \sim (T_c - T)^{1/2}$, which is the [[critical exponent|SQ41AZGZ2P]] $\beta = 1/2$.
In the same way, the susceptibility $\partial m / \partial h$ at $h = 0$ is $1/(2a)$ above $T_c$ and $1/(4\abs{a})$ below, so $\gamma = 1$.
At $T = T_c$, $h = 4 b m^3$, so $\delta = 3$, and the free energy $-a^2/(4b)$ below $T_c$ gives a jump of the specific heat, so $\alpha = 0$.

Non-example: a free energy with a cubic term $c\, m^3$, $c \ne 0$, fails clause 2.
Such a term is allowed when no symmetry forbids it, and it makes the transition first order, with a jump of $m$.

For a vector order parameter in $\R^n$ with symmetry $O(n)$, $m^2$ and $m^4$ are replaced by $\abs{m}^2$ and $\abs{m}^4$.
