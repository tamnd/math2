---
tag: PCNPQ7YBDE
kind: definition
name: Levi-Civita connection
msc: [53B05, 53B20]
defines: CAZYGE1T4E
uses: [GH6CXWFNDJ, JX65KSVHSJ, JZNQAN00ZJ, 68FGQEBD6J, FZBA1HA9ZM]
sources:
  - url: https://en.wikipedia.org/wiki/Levi-Civita_connection
---

## Definition

Let $(M, g)$ be a [[pseudo-Riemannian manifold|GH6CXWFNDJ]], and write $\mathfrak{X}(M)$ for the space of smooth vector fields on $M$.
A *Levi-Civita connection* of $(M, g)$ is an [[affine connection|JX65KSVHSJ]] $\nabla$ on $M$ such that:

1. $\nabla$ is torsion-free: $\nabla_X Y - \nabla_Y X = [X, Y]$ for all $X, Y \in \mathfrak{X}(M)$, where $[X, Y]$ is the [[Lie bracket|68FGQEBD6J]];
2. $\nabla$ is compatible with $g$: $X\bigl(g(Y, Z)\bigr) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$ for all $X, Y, Z \in \mathfrak{X}(M)$.

## Remarks

Example: on $\R^n$ with $g = \sum_i dx_i^2$, let $\nabla_X Y$ be the vector field whose components are $X(Y^1), \ldots, X(Y^n)$.
Then $\nabla_X Y - \nabla_Y X$ has components $X(Y^i) - Y(X^i)$, which is $[X, Y]$, and the product rule gives clause 2 for $g(Y, Z) = \sum_i Y^i Z^i$.

Non-example: on $\R^3$ with the Euclidean metric, let $\nabla_X Y = D_X Y + X \times Y$, where $D$ is the flat connection above and $\times$ is the cross product.
This is an affine connection, and clause 2 holds because $\ip{X \times Y}{Z} + \ip{Y}{X \times Z} = 0$.
Its torsion is $\nabla_X Y - \nabla_Y X - [X, Y] = 2 \, X \times Y$, which is not zero, so clause 1 fails.

The two clauses determine $\nabla$; this is the [[fundamental theorem of Riemannian geometry|78JRW8KTH8]].
In coordinates, $\nabla_{\partial_i} \partial_j = \sum_k \Gamma^k_{ij} \partial_k$ with the [[Christoffel symbols|FZBA1HA9ZM]]
$$\Gamma^k_{ij} = \frac{1}{2} \sum_l g^{kl} \left( \partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij} \right).$$
