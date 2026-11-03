---
tag: FAVX3MA9BQ
kind: counterexample
name: Painlevé paradox
msc: ["70E18", 70F40]
uses: [4XE2B2PBGC, KNBP19FG6K, EZ9P9ERKNE]
sources:
  - url: https://en.wikipedia.org/wiki/Painlev%C3%A9_paradox
same_as:
  wikidata: Q7124903
  wikipedia: Painlevé paradox
---

## Counterexample

Consider a [[rigid body|EZ9P9ERKNE]] that touches a fixed rigid surface at one point and slides on it.
The contact is unilateral: the normal contact force $\lambda$ satisfies $\lambda \ge 0$, and the body may leave the surface but not enter it.
The tangential contact force obeys Coulomb's law of [[friction|4XE2B2PBGC]] with coefficient $\mu > 0$: during sliding it has size $\mu \lambda$ and opposes the slip velocity.
Let $y$ be the height of the contact point above the surface.
While the contact point slides, [[Newton's laws|KNBP19FG6K]] give
$$\ddot y = A + B \lambda.$$
Here $A$ depends on the positions and velocities.
The coefficient $B$ depends on the positions, on the direction of slip and on $\mu$.
The contact conditions are complementarity conditions:
$$\lambda \ge 0, \qquad \ddot y \ge 0, \qquad \lambda\, \ddot y = 0.$$
If $B > 0$, there is exactly one solution: $\lambda = 0$ when $A \ge 0$ and $\lambda = -A/B$ when $A < 0$.
If $B < 0$ and $A < 0$, there is no solution: $\lambda = 0$ gives $\ddot y = A < 0$, and $\lambda > 0$ gives $\ddot y < 0$.
If $B < 0$ and $A > 0$, there are two solutions: $\lambda = 0$, and $\lambda = -A/B > 0$ with $\ddot y = 0$.
For large enough $\mu$ the coefficient $B$ becomes negative in some positions.
Then the rigid-body equations with Coulomb friction can have no solution or several solutions.

## Remarks

Painlevé's classical example is a thin rod sliding with one end on a rough horizontal plane.
For a uniform rod, the coefficient $B$ can be negative only if $\mu > 4/3$.
A standard resolution allows impulsive contact forces (a tangential impact) in the inconsistent case, so that the velocities jump.
Another is to drop full rigidity and model the contact with a small compliance.

## Explanations

### L1 human

Imagine pushing a pencil whose tip drags on a very rough table.
Friction can push the tip into the table harder the harder the table pushes back, and then the usual equations break down.
In some states they have no answer, and in others they have two.
The paradox shows that perfectly rigid bodies together with the simple Coulomb law of friction are not a complete model.
