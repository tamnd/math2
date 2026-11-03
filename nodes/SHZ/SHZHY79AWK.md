---
tag: SHZHY79AWK
kind: definition
name: Scale factor
msc: ["83F05"]
defines: J70F32P86W
uses: [ECJMS4VDTF]
sources:
  - url: https://en.wikipedia.org/wiki/Scale_factor_(cosmology)
---

## Definition

Let $(M, g)$ be a [[Friedmann–Lemaître–Robertson–Walker spacetime|ECJMS4VDTF]] $M = I \times \Sigma$ with metric $g = -dt^2 + a(t)^2 \gamma_k$, where $\gamma_k$ is a Riemannian metric of constant curvature $k$ on the three-manifold $\Sigma$.
The smooth positive function $a \colon I \to (0, \infty)$ is the *scale factor*.
The function $H = \dot a / a$ on $I$, where the dot is the derivative in $t$, is the *Hubble parameter*.

## Remarks

The pair $(a, \gamma_k)$ is fixed only up to $a \mapsto \lambda a$ and $\gamma_k \mapsto \lambda^{-2} \gamma_k$ for $\lambda > 0$; the Hubble parameter does not change.
A common normalization is $a(t_0) = 1$ at the present time $t_0$; another, for $k \neq 0$, is $k = \pm 1$.
Example: for $a(t) = t^{2/3}$ on $I = (0, \infty)$, the Hubble parameter is $H = 2/(3t)$.
Non-example: a function $a$ that vanishes somewhere on $I$ is not a scale factor, because then $g$ is degenerate there.
For two comoving points at comoving distance $\chi$, the proper distance at time $t$ along the slice is $D(t) = a(t)\chi$.
