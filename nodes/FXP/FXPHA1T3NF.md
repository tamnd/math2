---
tag: FXPHA1T3NF
kind: problem
name: Euler's three-body problem
msc: [70F07, 70H06, 70F15]
uses: [29WRN5J730, 0EDKGA2FAK, 0262JP0NV9, N0N7CMRCMH, JE1Z920QKT]
about: [JE1Z920QKT]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_three-body_problem
same_as:
  wikidata: Q4177149
  wikipedia: Euler's three-body problem
history:
  posed_by: "Leonhard Euler"
  first_stated: "1760"
---

## Problem

Let $G > 0$ be the gravitational constant, let $m_1, m_2 > 0$ and let $c > 0$.
Two point masses $m_1$ and $m_2$ are fixed at the points $(0, 0, -c)$ and $(0, 0, c)$ of $\R^3$.
A particle at $x(t) \in \R^3$ moves under their [[Newtonian attraction|29WRN5J730]]:
$$x'' = - \frac{G m_1 (x - (0, 0, -c))}{r_1^3} - \frac{G m_2 (x - (0, 0, c))}{r_2^3},$$
where $r_1$ and $r_2$ are the distances from $x$ to the two fixed points.
Given the initial position and velocity of the particle, determine its motion.

## Remarks

The problem is also called the problem of two fixed centres.
It is solved: Euler showed in 1760 that it can be integrated exactly.
It is a [[Hamiltonian system|0EDKGA2FAK]] with three degrees of freedom and three independent [[first integrals|0262JP0NV9]] in involution, so it is an [[integrable system|N0N7CMRCMH]].
They are the energy, the component of the angular momentum along the axis through the two centres, and a third integral found by separating variables.
In prolate spheroidal coordinates $\xi = (r_1 + r_2)/(2c)$, $\eta = (r_1 - r_2)/(2c)$ and the angle $\varphi$ around the axis, the Hamilton–Jacobi equation separates, and the solution is given by elliptic integrals.

The problem differs from the [[three-body problem|JE1Z920QKT]] because the two centres do not move.
It is used as an approximation for a satellite near an oblate planet and, in quantum mechanics, for the hydrogen molecule ion.

## Explanations

### L1 human

Imagine two stars nailed in place and a small planet moving under the pull of both.
Euler found that, unlike the real three-body problem, this one can be solved exactly.
The trick is to use coordinates built from the sum and the difference of the distances to the two stars, in which the motion splits into simpler independent pieces.
