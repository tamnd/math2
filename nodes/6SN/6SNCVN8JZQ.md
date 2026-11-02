---
tag: 6SNCVN8JZQ
kind: definition
name: Einstein manifold
msc: [53C25, 53C21]
defines: 41S2EZ0KR3
uses: [7CBT4SM83Y, 4GTNM0WHDH]
sources:
  - url: https://en.wikipedia.org/wiki/Einstein_manifold
---

## Definition

Let $(M, g)$ be a [[Riemannian manifold|7CBT4SM83Y]] and let $\operatorname{Ric}$ be its [[Ricci curvature|4GTNM0WHDH]] tensor.
The manifold $(M, g)$ is an *Einstein manifold*, and $g$ is an *Einstein metric*, if there is a real constant $\lambda$ such that
$$\operatorname{Ric} = \lambda g.$$
The constant $\lambda$ is the *Einstein constant*.

## Remarks

Example: the unit sphere $S^n \subset \R^{n+1}$ with $n \ge 2$ has sectional curvature $1$, so $\operatorname{Ric} = (n-1) g$, and it is Einstein with $\lambda = n - 1$.

Non-example: the product $S^2 \times S^3$ of unit spheres has $\operatorname{Ric} = g$ on vectors tangent to $S^2$ and $\operatorname{Ric} = 2g$ on vectors tangent to $S^3$.
No single constant $\lambda$ works, so it is not Einstein.

Taking the trace gives $\lambda = R/n$, where $R$ is the [[scalar curvature|ZHX2VYQDZ3]] and $n = \dim M$, so an Einstein metric has constant scalar curvature.
If $M$ is connected, $n \ge 3$ and $\operatorname{Ric} = f g$ for a smooth function $f$, the contracted Bianchi identity forces $f$ to be constant.
In dimension $2$ every metric satisfies $\operatorname{Ric} = K g$ with $K$ the Gaussian curvature, so a surface is Einstein exactly when its curvature is constant.
The same definition is used for pseudo-Riemannian metrics.
