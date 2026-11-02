---
tag: ZS2WYH25R0
kind: definition
name: Ricci flow
msc: ["53E20", 35K55]
defines: CR14D9YQTY
uses: [7CBT4SM83Y, Q61VFHCH2J, 4GTNM0WHDH]
sources:
  - url: https://en.wikipedia.org/wiki/Ricci_flow
---

## Definition

Let $M$ be a smooth manifold and let $I \subseteq \R$ be an interval.
A *Ricci flow* on $M$ is a family $(g(t))_{t \in I}$ of [[Riemannian metrics|Q61VFHCH2J]] on $M$ with these properties.
The metric $g(t)$ depends smoothly on $t$, and
$$\frac{\partial g}{\partial t}(t) = -2 \operatorname{Ric}\big(g(t)\big) \quad \text{for all } t \in I,$$
where $\operatorname{Ric}(g)$ is the [[Ricci curvature|4GTNM0WHDH]] tensor of $g$.

## Remarks

Example: let $g_0$ be the round metric of the unit sphere $S^n$ with $n \ge 2$, so $\operatorname{Ric}(g_0) = (n - 1) g_0$.
Let $g(t) = (1 - 2(n - 1)t)\, g_0$ for $t < \frac{1}{2(n-1)}$.
The Ricci tensor does not change when the metric is multiplied by a positive constant, so $\operatorname{Ric}(g(t)) = (n - 1) g_0$.
Thus $\partial_t g = -2(n-1) g_0 = -2\operatorname{Ric}(g(t))$, and $g$ is a Ricci flow that shrinks the sphere to a point at $t = \frac{1}{2(n-1)}$.
Non-example: $g(t) = (1 + 2(n - 1)t)\, g_0$ has $\partial_t g = +2\operatorname{Ric}(g(t))$, which has the wrong sign.
A flat metric, such as that of a flat torus, gives a constant Ricci flow $g(t) = g_0$.
In local coordinates the equation reads $\partial_t g_{ij} = -2 R_{ij}$.
