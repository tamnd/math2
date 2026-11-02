---
tag: ZXY0AYKMXZ
kind: statement
role: theorem
name: Maupertuis's principle
msc: [70H30, 49S05]
uses: [7CBT4SM83Y, NSYMQMHPDN, PQ25NHV0KS]
about: [PQ25NHV0KS]
sources:
  - url: https://en.wikipedia.org/wiki/Maupertuis%27s_principle
same_as:
  wikidata: Q644922
  wikipedia: Maupertuis's principle
---

## Statement

Let $M$ be a smooth manifold, the configuration space of a mechanical system.
Let $g$ be a Riemannian metric on $M$, so that the kinetic energy at the velocity $v \in T_qM$ is $T = \tfrac12 g_q(v, v)$.
Let $V \colon M \to \R$ be a smooth potential, so that the motions $q(t)$ solve the Euler–Lagrange equations of $L = T - V$.
Fix an energy value $E$ and let $M_E = \set{q \in M : V(q) < E}$.
For a curve $\gamma \colon [a, b] \to M_E$ define the *abbreviated action*
$$S_0[\gamma] = \int_a^b \sqrt{2\,(E - V(\gamma(s)))}\; \norm{\gamma'(s)}_g \, ds.$$
Let $\gamma$ be a regular curve in $M_E$.
Then, up to reparametrisation, $\gamma$ is the path of a motion with total energy $T + V = E$ if and only if the following holds.
The curve $\gamma$ is a critical point of $S_0$ among curves in $M_E$ with the same endpoints.

## Remarks

The functional $S_0$ is the length functional of the *Jacobi metric* $2(E - V)\,g$ on $M_E$.
So the paths of motion of energy $E$ are the [[geodesics|NSYMQMHPDN]] of the Jacobi metric.
This metric is a conformal change of the kinetic metric $g$ of the [[Riemannian manifold|7CBT4SM83Y]] $(M, g)$.
Along a true motion $\norm{\dot q}_g = \sqrt{2(E - V)}$, so $S_0$ equals $\int 2T\,dt = \int p \cdot dq$, the classical form of the abbreviated action.
The proof compares the Euler–Lagrange equations of the length of the Jacobi metric with those of $L$, after the change of time $dt = \norm{\gamma'}_g / \sqrt{2(E - V)}\, ds$.
Unlike [[Hamilton's principle|FAQ9CH2Z76]], the variation fixes the energy and leaves the travel time free.
For a free particle ($V = 0$), the paths are the geodesics of $g$ itself.
The hypothesis $V < E$ is needed: where $V = E$ the Jacobi metric degenerates, and these are the turning points of the motion.

## Explanations

### L1 human

A moving body with fixed total energy picks a path between two points that makes a certain quantity stationary.
This quantity adds up, along the path, the speed the body would have at each point times the length travelled there, and it ignores how long the trip takes.
So the shape of the path can be found without solving for the timing first.

### L2 human

Maupertuis's principle turns a dynamics problem into a geometry problem.
Orbits of energy $E$ become geodesics of the Jacobi metric $2(E - V)g$, and tools of Riemannian geometry, such as curvature and comparison theorems, then give information on the stability of orbits.
It is derived from the [[stationary-action principle|Q104C67P26]] by fixing the energy instead of the time.
