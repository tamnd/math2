---
tag: DWYPS58A7Q
kind: definition
name: Affine connection
msc: [53B05]
defines: JX65KSVHSJ
uses: [F45VQ47GPV, WY6K3P4YCG, 5ZYRRVE8BW, 68FGQEBD6J]
sources:
  - url: https://en.wikipedia.org/wiki/Affine_connection
---

## Definition

Let $M$ be a smooth manifold with [[tangent bundle|WY6K3P4YCG]] $TM$, and let $\mathfrak{X}(M)$ be the space of smooth vector fields on $M$.
An *affine connection* on $M$ is a [[connection|5ZYRRVE8BW]] on the vector bundle $TM$.
That is, it is a map $\nabla : \mathfrak{X}(M) \times \mathfrak{X}(M) \to \mathfrak{X}(M)$, $(X, Y) \mapsto \nabla_X Y$, that is $C^\infty(M)$-linear in $X$, $\R$-linear in $Y$, and satisfies $\nabla_X (fY) = (Xf) Y + f \nabla_X Y$ for every smooth function $f$.

## Remarks

Example: on $\R^n$ with $Y = \sum_j Y^j \partial_j$, the formula $\nabla_X Y = \sum_j (X Y^j) \, \partial_j$ defines an affine connection, the flat connection; the three conditions follow from the linearity and the product rule of directional derivatives.
Non-example: $(X, Y) \mapsto [X, Y]$ is not an affine connection, since $[fX, Y] = f [X, Y] - (Yf) X$ is not $C^\infty(M)$-linear in $X$.
In a chart, $\nabla$ is given by its Christoffel symbols $\Gamma^k_{ij}$, defined by $\nabla_{\partial_i} \partial_j = \Gamma^k_{ij} \partial_k$.
Every smooth manifold has affine connections: glue the flat connections of charts with a partition of unity.
Two important tensors measure an affine connection: its torsion $\nabla_X Y - \nabla_Y X - [X, Y]$, built with the [[Lie bracket|68FGQEBD6J]], and its curvature.
