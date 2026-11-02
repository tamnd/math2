---
tag: GXN2NEHC8X
kind: problem
name: Obstacle problem
msc: [35R35, 35J86, 49J40]
uses: [YR42E2W19Q, 6QS7X5GVMY, M4CEZ5K9HP, 02AS45T3H9, 0DEB0JMN0W, PQ25NHV0KS]
about: [YR42E2W19Q, 6QS7X5GVMY]
sources:
  - url: https://en.wikipedia.org/wiki/Obstacle_problem
same_as:
  wikidata: Q3406250
  wikipedia: Obstacle problem
history:
  posed_by: "Jacques-Louis Lions and Guido Stampacchia"
  first_stated: "1967"
  notes: "Lions and Stampacchia set the obstacle problem as a variational inequality in Variational inequalities, Comm. Pure Appl. Math. 20 (1967)."
---

## Problem

Let $\Omega \subseteq \R^n$ be a bounded open set with Lipschitz boundary.
Let $\psi \colon \overline{\Omega} \to \R$ be a continuous function in the [[Sobolev space|M4CEZ5K9HP]] $H^1(\Omega)$ with $\psi \le 0$ on $\partial \Omega$, the obstacle.
Let
$$K = \set{v \in H^1_0(\Omega) : v \ge \psi \text{ almost everywhere in } \Omega}.$$
Find $u \in K$ that minimizes the Dirichlet energy
$$D(v) = \frac{1}{2} \int_\Omega \abs{\nabla v}^2 \, dx$$
over all $v \in K$.

## Remarks

The set $K$ is nonempty, closed and [[convex|02AS45T3H9]] in $H^1_0(\Omega)$, since it contains $\max(\psi, 0)$.
So the problem has exactly one solution, by the Stampacchia theorem for [[variational inequalities|6QS7X5GVMY]] and the Poincaré inequality.
Equivalently, $u \in K$ satisfies $\int_\Omega \nabla u \cdot \nabla (v - u) \, dx \ge 0$ for all $v \in K$.
When $u$ is regular enough, this is the complementarity system $u \ge \psi$, $\Delta u \le 0$, and $\Delta u = 0$ where $u > \psi$.
So $u$ is [[harmonic|0DEB0JMN0W]] in the open set $\set{u > \psi}$ and equals $\psi$ on the contact set $\set{u = \psi}$.
The boundary of the contact set inside $\Omega$ is not known in advance, so this is a [[free boundary problem|YR42E2W19Q]].
If $\psi$ is smooth, the solution has bounded second derivatives locally, and this is the best regularity possible in general, since $\Delta u$ jumps across the free boundary.
In dimension one with $\Omega = (-1, 1)$, the solution is the smallest concave function above $\psi$ that vanishes at $\pm 1$: it is linear off the contact set.

## Explanations

### L1 human

Stretch an elastic membrane over a frame and push an obstacle up from below.
The membrane rests on the obstacle in some places and is free elsewhere.
Where it is free, it takes the shape of least tension, a harmonic function.
The problem is to find the shape of the membrane and the region where it touches the obstacle.
That region is not known at the start: finding its edge is part of the problem.
