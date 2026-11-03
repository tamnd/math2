---
tag: W3RVF2K5DJ
kind: definition
name: Conformal bootstrap
msc: [81T40, 81T05]
defines: SQDY0QJYVD
uses: [99KYX4BDRD, 7YMY641GBN]
sources:
  - url: https://en.wikipedia.org/wiki/Conformal_bootstrap
---

## Definition

Let $\phi$ be a real scalar primary field of dimension $\Delta_\phi$ in a [[conformal field theory|99KYX4BDRD]] on $\R^d$.
For distinct points $x_1, \dots, x_4$ write $x_{ij} = \abs{x_i - x_j}$ and use the cross-ratios
$$u = \frac{x_{12}^2 x_{34}^2}{x_{13}^2 x_{24}^2}, \qquad v = \frac{x_{14}^2 x_{23}^2}{x_{13}^2 x_{24}^2}.$$
Conformal invariance gives $\langle \phi(x_1)\phi(x_2)\phi(x_3)\phi(x_4) \rangle = x_{12}^{-2\Delta_\phi} x_{34}^{-2\Delta_\phi} \, g(u, v)$ for a function $g$.
Expand by the [[operator product expansion|7YMY641GBN]] in the channel $\phi(x_1)\phi(x_2)$.
This gives
$$g(u, v) = \sum_{\mathcal{O}} \lambda_{\phi\phi\mathcal{O}}^2 \, G_{\Delta, \ell}(u, v).$$
The sum runs over the primary fields $\mathcal{O}$ in the expansion, of dimension $\Delta$ and spin $\ell$.
The functions $G_{\Delta, \ell}$ are the conformal blocks, which are fixed by conformal symmetry.
The *conformal bootstrap* is the method of finding or constraining the data $\set{(\Delta, \ell, \lambda_{\phi\phi\mathcal{O}})}$ from the following conditions.

1. Crossing symmetry: exchanging $x_1$ and $x_3$ gives $v^{\Delta_\phi} g(u, v) = u^{\Delta_\phi} g(v, u)$.
2. Unitarity: the coefficients $\lambda_{\phi\phi\mathcal{O}}$ are real, and the dimensions satisfy the unitarity bounds $\Delta \ge \frac{d - 2}{2}$ for $\ell = 0$ and $\Delta \ge \ell + d - 2$ for $\ell \ge 1$.
3. The spectrum contains the identity field, with $\Delta = 0$, $\ell = 0$ and $\lambda = 1$, and only even spins $\ell$ appear.

## Remarks

Substituting the block expansion into crossing gives
$$\sum_{\mathcal{O}} \lambda_{\phi\phi\mathcal{O}}^2 \left( v^{\Delta_\phi} G_{\Delta, \ell}(u, v) - u^{\Delta_\phi} G_{\Delta, \ell}(v, u) \right) = 0,$$
a sum with non-negative coefficients.
Assume a gap, for instance that every scalar other than the identity has $\Delta \ge \Delta_*$.
Suppose a linear functional is positive on the identity term and non-negative on every other term allowed by the gap and the unitarity bounds.
Then the equation cannot hold, and that gap is ruled out.
This is the numerical bootstrap of Rattazzi, Rychkov, Tonni and Vichi from 2008.

Example: the generalized free field, with $g(u, v) = 1 + u^{\Delta_\phi} + (u/v)^{\Delta_\phi}$, satisfies crossing: both sides of clause 1 equal $v^{\Delta_\phi} + (uv)^{\Delta_\phi} + u^{\Delta_\phi}$.

Non-example: $g(u, v) = 1 + u^{\Delta_\phi}$ alone fails crossing, since $v^{\Delta_\phi}(1 + u^{\Delta_\phi}) \ne u^{\Delta_\phi}(1 + v^{\Delta_\phi})$ in general.

In two dimensions, with Virasoro symmetry, the method was used by Belavin, Polyakov and Zamolodchikov in 1984 to solve the minimal models exactly.
