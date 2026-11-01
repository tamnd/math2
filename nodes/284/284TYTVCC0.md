---
tag: 284TYTVCC0
kind: definition
name: Kolmogorov backward equation
msc: [60J60, 35K10, 60H10]
defines: KQMJ7M57ER
uses: [9HDQ094ADQ, VPA41PWRR1, 22735FGJV6, 09EGC6F8PT, HZM2ASCDY4, 2J1RVQB0CM]
sources:
  - url: https://en.wikipedia.org/wiki/Kolmogorov_backward_equations_(diffusion)
---

## Definition

Let $b \colon \R^n \to \R^n$ and $\sigma \colon \R^n \to \R^{n \times m}$ be functions, and let $a = \sigma \sigma^{T}$.
Consider the [[diffusion|9HDQ094ADQ]] given by the stochastic differential equation $dX_t = b(X_t) \, dt + \sigma(X_t) \, dB_t$, where $B$ is an $m$-dimensional [[Brownian motion|22735FGJV6]].
Its [[generator|VPA41PWRR1]] is the differential operator
$$\mathcal{L} g(x) = \sum_{i=1}^n b_i(x) \, \partial_i g(x) + \frac12 \sum_{i,j=1}^n a_{ij}(x) \, \partial_i \partial_j g(x),$$
with [[partial derivatives|09EGC6F8PT]] $\partial_i$ in the variable $x$.
The *Kolmogorov backward equation* of the diffusion is the equation
$$\partial_t u(t, x) = \mathcal{L} u(t, x), \quad t > 0, \ x \in \R^n,$$
for a function $u \colon [0, \infty) \times \R^n \to \R$, with an initial condition $u(0, x) = f(x)$.

## Remarks

Under regularity conditions on $b$, $\sigma$ and $f$, the function $u(t, x) = E[f(X_t) \mid X_0 = x]$ solves the backward equation.
If $X$ has transition densities $p(t, x, y)$, they satisfy $\partial_t p = \mathcal{L}_x p$, where $\mathcal{L}_x$ acts on the starting point $x$.
The forward, or Fokker–Planck, equation acts instead on the end point $y$.
Example: for the [[Ornstein–Uhlenbeck process|HZM2ASCDY4]] $dX = -X \, dt + dB$ in $\R$ and $f(y) = y$, one has $u(t, x) = x e^{-t}$.
Check: $\partial_t u = -x e^{-t}$ and $\mathcal{L} u = -x \, \partial_x u + \tfrac12 \partial_{xx} u = -x e^{-t}$.
Non-example: for the same process, $v(t, x) = x e^{t}$ has $\partial_t v = x e^{t}$ but $\mathcal{L} v = -x e^{t}$, so it does not solve the equation.
The equation follows from [[Itô's lemma|2J1RVQB0CM]] applied to $s \mapsto u(t - s, X_s)$.
