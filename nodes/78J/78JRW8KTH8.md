---
tag: 78JRW8KTH8
kind: statement
role: theorem
name: Fundamental theorem of Riemannian geometry
msc: [53B05, 53B20]
uses: [GH6CXWFNDJ, JX65KSVHSJ, JZNQAN00ZJ, CAZYGE1T4E, FZBA1HA9ZM]
about: [CAZYGE1T4E]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_of_Riemannian_geometry
same_as:
  wikidata: Q2185349
  wikipedia: Fundamental theorem of Riemannian geometry
---

## Statement

Let $(M, g)$ be a [[pseudo-Riemannian manifold|GH6CXWFNDJ]].
Then there is exactly one [[affine connection|JX65KSVHSJ]] $\nabla$ on $M$ with the following two properties, for all smooth vector fields $X, Y, Z$ on $M$:

1. $\nabla$ is torsion-free: $\nabla_X Y - \nabla_Y X = [X, Y]$;
2. $\nabla$ is compatible with $g$: $X\bigl(g(Y, Z)\bigr) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$.

This connection is the [[Levi-Civita connection|CAZYGE1T4E]] of $(M, g)$.

## Remarks

The proof writes the compatibility identity three times with $X, Y, Z$ permuted cyclically and combines them using torsion-freeness.
This gives the Koszul formula
$$2 g(\nabla_X Y, Z) = X g(Y, Z) + Y g(X, Z) - Z g(X, Y) + g([X, Y], Z) - g([X, Z], Y) - g([Y, Z], X).$$
Since $g$ is nondegenerate, the right side determines $\nabla_X Y$, which gives uniqueness.
For existence, one checks that the vector field defined by the Koszul formula is an affine connection with both properties.
In coordinates the formula gives the [[Christoffel symbols|FZBA1HA9ZM]] $\Gamma^k_{ij} = \tfrac{1}{2} \sum_l g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$.
Both conditions are needed for uniqueness: there are many metric-compatible connections with [[torsion|JZNQAN00ZJ]], and many torsion-free connections that do not preserve $g$.

## Explanations

### L1 human

A metric measures lengths and angles at each point, but it does not by itself say how to differentiate vector fields.
This theorem says that once one asks the differentiation rule to keep lengths and angles and not to twist, there is no choice left: exactly one rule works.
So every Riemannian manifold comes with its own canonical way of differentiating.

### L2 human

The theorem is why geodesics, parallel transport and curvature are invariants of the metric alone.
The Koszul formula is also a practical tool: it computes the connection of a left-invariant metric on a Lie group or of a warped product directly from brackets.
The same proof works for any nondegenerate metric, so the result holds for Lorentzian manifolds as used in general relativity.
For a surface in $\R^3$, the Levi-Civita connection is the tangential part of the ordinary derivative.
This is one way to see that Gaussian curvature depends only on the first fundamental form.
