---
tag: WWQJQXJECK
kind: problem
name: Shape optimization
msc: [49Q10, 49J20, 35R30]
uses: [S2BBZPAFDR, GC5BDZ6QBC, 1EQM0DJ4NC, 9XFEG6ANGM]
about: [S2BBZPAFDR]
sources:
  - url: https://en.wikipedia.org/wiki/Shape_optimization
same_as:
  wikidata: Q7489239
  wikipedia: Shape optimization
history:
  posed_by: "Jacques Hadamard"
  first_stated: "1907"
  notes: "Hadamard computed the variation of a boundary value problem under a change of the domain in his memoir on clamped elastic plates (1907)."
---

## Problem

Let $D \subseteq \R^d$ be a bounded open set, called the design region.
Let $\mathcal{O}$ be a class of open subsets $\Omega \subseteq D$, the admissible shapes, for example those with a given volume.
For each $\Omega \in \mathcal{O}$ let $y_\Omega$ be the solution of a boundary value problem for a [[partial differential equation|GC5BDZ6QBC]] on $\Omega$.
Let $J(\Omega) = j(\Omega, y_\Omega)$ be a real-valued shape [[functional|1EQM0DJ4NC]].
The *shape optimization problem* is to find $\Omega^* \in \mathcal{O}$ with $J(\Omega^*) \le J(\Omega)$ for every $\Omega \in \mathcal{O}$.

## Remarks

It is a form of [[optimal control of partial differential equations|S2BBZPAFDR]] in which the control is the domain itself.
Example: minimize the first Dirichlet eigenvalue $\lambda_1(\Omega)$ of the Laplacian among open sets $\Omega \subseteq \R^d$ of a given volume.
The Rayleigh–Faber–Krahn inequality solves it: the minimizers are the balls.
In general minimizers need not exist in a given class of shapes, since minimizing sequences can develop holes or oscillating boundaries.
One then restricts the class, for example by a uniform cone condition or a perimeter bound, or relaxes the problem; relaxation leads to topology optimization.
Gradient methods use the [[shape derivative|9XFEG6ANGM]] of $J$, often computed with an adjoint equation.

## Explanations

### L1 human

Shape optimization asks for the best shape of an object: a wing with least drag, a beam with greatest stiffness, a drum with lowest tone.
The quality of a shape is measured through the solution of a physical equation on that shape.
For example, among all drums of the same area, the round drum has the lowest fundamental tone.
