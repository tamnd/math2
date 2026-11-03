---
tag: DKX70HTEPG
kind: definition
name: Cyclic coordinate
msc: [70H03, 70H33]
defines: TGC5C62HYE
uses: [47JMCBM3VJ, BCF1EX9W2M, 37Q4BTJMXW]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrangian_mechanics
---

## Definition

Let $L(t, q, \dot q)$ be the Lagrangian of a [[Lagrangian system|47JMCBM3VJ]], written in [[generalized coordinates|BCF1EX9W2M]] $q = (q_1, \ldots, q_n)$ on an open set of $\R^n$.
A coordinate $q_k$ is *cyclic*, or *ignorable*, if $\partial L / \partial q_k = 0$ identically.
That is, $L$ does not depend on $q_k$, though it may depend on $\dot q_k$.

## Remarks

The generalized [[momentum|37Q4BTJMXW]] conjugate to $q_k$ is $p_k = \partial L / \partial \dot q_k$.
If $q_k$ is cyclic, the $k$-th Euler–Lagrange equation reads $\frac{d}{dt} p_k = \partial L/\partial q_k = 0$, so $p_k$ is constant along every motion.
Whether a coordinate is cyclic depends on the choice of coordinates: the same symmetry may be hidden in other coordinates.

Example: a particle of mass $m$ in the plane with a central potential, in polar coordinates, has $L = \tfrac12 m(\dot r^2 + r^2\dot\theta^2) - V(r)$.
The angle $\theta$ does not occur in $L$, so it is cyclic, and $p_\theta = m r^2 \dot\theta$, the angular momentum, is conserved.

Non-example: in the same Lagrangian $r$ is not cyclic, since $\partial L/\partial r = m r\dot\theta^2 - V'(r)$ is not identically $0$.
In Cartesian coordinates the same Lagrangian is $\tfrac12 m(\dot x^2 + \dot y^2) - V(\sqrt{x^2 + y^2})$, and for non-constant $V$ neither $x$ nor $y$ is cyclic.

## Explanations

### L1 human

A coordinate is cyclic when the Lagrangian does not contain it.
Its conjugate momentum is then a conserved quantity.
