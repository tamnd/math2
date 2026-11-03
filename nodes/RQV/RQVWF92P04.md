---
tag: RQVWF92P04
kind: definition
name: Initial value formulation of general relativity
msc: ["83C05", "35Q75", "58J45"]
defines: SB7BVCZJ3F
uses: [5HDG31YEPW, A9514690T3, 24CP8Q56CV, 7C2WP33E10, D1SYF8F8RQ, R8KDE9QYNP]
sources:
  - url: https://en.wikipedia.org/wiki/Initial_value_formulation_(general_relativity)
---

## Definition

A *vacuum initial data set* is a triple $(\Sigma, h, K)$ where:

1. $\Sigma$ is a 3-dimensional manifold and $h$ is a [[Riemannian metric|5HDG31YEPW]] on $\Sigma$.
2. $K$ is a symmetric $(0,2)$-tensor field on $\Sigma$.
3. $(h, K)$ satisfy the *constraint equations*
$$R(h) - K_{ij} K^{ij} + (\operatorname{tr}_h K)^2 = 0, \qquad D^j K_{ij} - D_i (\operatorname{tr}_h K) = 0.$$

Here $R(h)$ is the [[scalar curvature|24CP8Q56CV]] of $h$, $D$ is its Levi-Civita connection, and indices are raised with $h$.
A *development* of $(\Sigma, h, K)$ is a 4-dimensional [[Lorentzian manifold|D1SYF8F8RQ]] $(M, g)$ with an embedding $\iota \colon \Sigma \to M$ such that:

1. $g$ solves the vacuum [[Einstein field equations|7C2WP33E10]] $\operatorname{Ric}(g) = 0$.
2. $\iota^* g = h$, and $K$ is the [[second fundamental form|A9514690T3]] of $\iota(\Sigma)$ with respect to the future unit normal.
3. $\iota(\Sigma)$ is a [[Cauchy surface|R8KDE9QYNP]] of $(M, g)$.

The *initial value formulation* of general relativity is the study of the existence, uniqueness and properties of developments of initial data sets.

## Remarks

The first constraint equation is the Hamiltonian constraint and the second is the momentum constraint.
They follow from the Gauss–Codazzi equations: up to constant factors and signs, they are the components $G(n, n)$ and $G(n, \cdot)$ of the Einstein tensor along the unit normal $n$.
With matter, their right-hand sides become $16\pi \rho$ and $8\pi J_i$, where $\rho$ and $J$ are the energy and momentum densities.
Example: $(\R^3, \delta, 0)$ satisfies the constraints, since $R(\delta) = 0$ and $K = 0$, and Minkowski space is a development of it.
Non-example: the round sphere $S^3$ with $K = 0$ is not vacuum data, since its scalar curvature is positive and the Hamiltonian constraint fails.
The sign convention for $K$ differs between authors; the constraint equations are unchanged by $K \mapsto -K$.

## Explanations

### L1 human

Initial data describe space at one instant, and a development is a spacetime in which these data appear as a slice through which every signal passes.
