---
tag: Z8XNDJSCJS
kind: definition
name: Christoffel symbols
msc: [53B05, 53B20]
defines: FZBA1HA9ZM
uses: [JX65KSVHSJ, Q61VFHCH2J]
sources:
  - url: https://en.wikipedia.org/wiki/Christoffel_symbols
---

## Definition

Let $M$ be a smooth manifold of dimension $n$ with an [[affine connection|JX65KSVHSJ]] $\nabla$.
Let $(U, x^1, \dots, x^n)$ be a chart, and let $\partial_i = \partial / \partial x^i$ be the coordinate vector fields on $U$.
The *Christoffel symbols* of $\nabla$ in this chart are the $n^3$ smooth functions $\Gamma^k_{ij}$ on $U$ determined by
$$\nabla_{\partial_i} \partial_j = \sum_{k=1}^n \Gamma^k_{ij} \, \partial_k \qquad (1 \le i, j \le n).$$

## Remarks

They determine $\nabla$ on $U$: $\nabla_X Y = \sum_k \big( X Y^k + \sum_{i,j} \Gamma^k_{ij} X^i Y^j \big) \partial_k$ for $X = \sum X^i \partial_i$ and $Y = \sum Y^j \partial_j$.
For the Levi-Civita connection of a [[Riemannian metric|Q61VFHCH2J]] with components $g_{ij}$ and inverse matrix $(g^{kl})$,
$$\Gamma^k_{ij} = \tfrac12 \sum_l g^{kl} \big( \partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij} \big).$$
Example: for the flat connection of $\R^2$ in polar coordinates $(r, \theta)$, where $g = dr^2 + r^2 d\theta^2$, this formula gives $\Gamma^r_{\theta\theta} = -r$, $\Gamma^\theta_{r\theta} = \Gamma^\theta_{\theta r} = 1/r$, and all other symbols vanish.
Non-example: the $\Gamma^k_{ij}$ are not the components of a tensor field; under a change of chart they transform with an extra term containing second derivatives of the coordinate change.
So they can vanish at a point in one chart and not in another; in Cartesian coordinates the symbols above are all $0$.
The connection is torsion-free exactly when $\Gamma^k_{ij} = \Gamma^k_{ji}$ in every chart.
