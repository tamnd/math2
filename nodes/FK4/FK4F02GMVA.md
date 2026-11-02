---
tag: FK4F02GMVA
kind: definition
name: Yamabe flow
msc: ["53E20", "53C21"]
defines: AC6WNX8F9Z
uses: [Q61VFHCH2J, ZHX2VYQDZ3]
sources:
  - url: https://en.wikipedia.org/wiki/Yamabe_flow
---

## Definition

Let $M$ be a smooth manifold and let $T > 0$.
Let $(g(t))_{0 \le t < T}$ be a smooth family of [[Riemannian metrics|Q61VFHCH2J]] on $M$.
It solves the *Yamabe flow* if
$$\frac{\partial g}{\partial t} = -R_{g(t)}\, g(t),$$
where $R_{g(t)}$ is the [[scalar curvature|ZHX2VYQDZ3]] of $g(t)$.

Let $M$ be compact.
The *normalized Yamabe flow* is
$$\frac{\partial g}{\partial t} = \left(r_{g(t)} - R_{g(t)}\right) g(t),$$
where $r_{g(t)}$ is the average of $R_{g(t)}$ over $M$ with respect to the volume of $g(t)$.
It preserves the total volume.

## Remarks

Example: on the unit sphere $S^n$ with $n \ge 2$ and round metric $g_0$, put $g(t) = \rho(t) g_0$.
The scalar curvature of $g_0$ is $n(n-1)$, so that of $g(t)$ is $n(n-1)/\rho(t)$.
The equation becomes $\rho'(t) g_0 = -n(n-1) g_0$, which holds for $\rho(t) = 1 - n(n-1)t$ with $0 \le t < 1/(n(n-1))$.
Non-example: the family $g(t) = (1 + t) g_0$ on the flat torus fails, since the scalar curvature is $0$ but the metric changes.
The right side is a multiple of $g$.
So a solution has the form $g(t) = u(\cdot, t)\, g(0)$ for a positive function $u$ on $M \times [0, T)$, and it stays in the conformal class of $g(0)$.
In dimension $2$ the Ricci curvature equals $\tfrac{1}{2} R g$, so the Yamabe flow coincides with the Ricci flow $\partial g/\partial t = -2 \operatorname{Ric}$.
