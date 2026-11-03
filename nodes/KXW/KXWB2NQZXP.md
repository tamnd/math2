---
tag: KXWB2NQZXP
kind: definition
name: Steady-state heat conduction
msc: [80A19, 35J05]
defines: RFWGC57K4H
uses: [SW8X60GYZT, XBQBT9E7JT, 9YJZ1PP2Y8, VP2HN86VAG, S8RG6N1PRT, DWK5N5SKTK]
sources:
  - url: https://en.wikipedia.org/wiki/Heat_equation
---

## Definition

Let a body with constant [[thermal conductivity|XBQBT9E7JT]] $k > 0$ occupy an open set $\Omega \subseteq \R^n$.
Let its temperature $T$ obey the [[heat equation|VP2HN86VAG]] with a heat source of density $f(x)$ per unit volume.
The [[conduction|SW8X60GYZT]] is in *steady state* when $T$ does not depend on time.
Then $T = T(x)$ satisfies the [[Poisson equation|DWK5N5SKTK]]
$$-k \, \Delta T = f \quad \text{in } \Omega.$$
Without sources, $f = 0$, and $T$ satisfies [[Laplace's equation|S8RG6N1PRT]] $\Delta T = 0$.

## Remarks

Example: in a slab $0 < x < L$ with faces held at $T(0) = T_1$ and $T(L) = T_2$ and no sources, $T'' = 0$.
So $T(x) = T_1 + (T_2 - T_1) x / L$, and by [[Fourier's law|9YJZ1PP2Y8]] the flux $q = k (T_1 - T_2) / L$ is the same at every $x$.

Non-example: $T(x, t) = e^{-t} \sin x$ on $0 < x < \pi$ solves the heat equation, but it is not steady, since $\partial_t T \ne 0$.

A steady state needs boundary data that do not change in time.
On a bounded domain with fixed boundary temperatures, solutions of the heat equation tend to the steady state as $t \to \infty$.
