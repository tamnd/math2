---
tag: EXGNVT1VG2
kind: definition
name: Generalized coordinates
msc: [70G10, 70H03]
defines: BCF1EX9W2M
uses: [MGYKGP7PW3, AXA8HN8Y45]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_coordinates
---

## Definition

Consider a system of $N$ point particles with position vector $x \in \R^{3N}$, subject to [[holonomic constraints|AXA8HN8Y45]] that may depend on time $t$.
For each $t$, let $Q_t \subseteq \R^{3N}$ be the set of positions allowed at time $t$, the [[configuration space|MGYKGP7PW3]] at that time.
Let $V \subseteq \R^n$ be open and let $I$ be an open interval of times.
*Generalized coordinates* on a part of the system's configurations are given by a smooth map
$$x \colon V \times I \to \R^{3N}, \qquad (q, t) \mapsto x(q, t),$$
such that:

1. For each $t \in I$, the map $q \mapsto x(q, t)$ is injective and its image is an open subset of $Q_t$.
2. For each $(q, t)$, the $3N \times n$ matrix $\partial x / \partial q$ has rank $n$.

The numbers $q_1, \dots, q_n$ are then called generalized coordinates, and $\dot q_1, \dots, \dot q_n$ are the generalized velocities.

## Remarks

Example: for a planar pendulum of length $\ell > 0$, take $V = (-\pi, \pi)$ and $x(\theta) = (\ell \sin\theta, -\ell\cos\theta)$; this map is injective onto the circle minus the top point, and $\partial x/\partial\theta = (\ell\cos\theta, \ell\sin\theta) \ne 0$.
Non-example: the map $(r, \theta) \mapsto (r\sin\theta, -r\cos\theta)$ with $r$ near $\ell$ is not a choice of generalized coordinates for the pendulum, because it takes values outside the circle $x^2 + y^2 = \ell^2$, which violates clause 1.
Clause 2 makes the generalized coordinates local coordinates of the configuration space as a manifold.
Usually one set of generalized coordinates covers almost all configurations, but not all of them, as for the pendulum and the top point.
