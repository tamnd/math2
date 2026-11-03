---
tag: RACGWEZE09
kind: definition
name: Boundary layer separation
msc: [76D10]
defines: DMND77PFQT
uses: [XXDE4YP722, YCFPD0GE5G]
sources:
  - url: https://en.wikipedia.org/wiki/Flow_separation
---

## Definition

Consider a steady two-dimensional [[boundary layer|YCFPD0GE5G]] flow $(u, v)$ along the wall $y = 0$, with dynamic viscosity $\mu > 0$, for $x$ in an interval $I$.
Let $\tau_w(x) = \mu \, \partial_y u(x, 0)$ be the wall shear stress.
Assume that $\tau_w > 0$ upstream, on $I \cap (-\infty, x_s)$.
The boundary layer *separates* at the point $x_s \in I$ if $\tau_w(x_s) = 0$ and $\tau_w < 0$ just downstream of $x_s$.
The point $x_s$ is the *separation point*, and downstream of it the flow near the wall is reversed, $u < 0$ for small $y > 0$.

## Remarks

Example: in the [[Prandtl boundary layer equations|XXDE4YP722]] at the wall, $u = v = 0$, so $\mu \, \partial_y^2 u(x, 0) = \partial_x p$.
If $\partial_x p > 0$ (adverse gradient), the profile curves away from the wall there, and a decreasing $\tau_w$ may reach $0$.
This is the typical separation on the rear of a cylinder.

Non-example: the Blasius layer on a flat plate has $\partial_x p = 0$ and $\tau_w(x) \approx 0.332 \, \mu U \sqrt{U / (\nu x)} > 0$ for all $x > 0$, so it never separates.

An adverse pressure gradient is necessary for separation in steady flow: with $\partial_x p \le 0$ the wall shear does not change sign.
At the separation point the steady boundary layer equations with prescribed pressure have a singularity, found by Goldstein, so the outer flow and the layer must be computed together.
In three-dimensional or unsteady flow the vanishing of wall shear no longer marks separation, and other criteria are used.
