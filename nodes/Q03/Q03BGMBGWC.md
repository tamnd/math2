---
tag: Q03BGMBGWC
kind: statement
role: theorem
name: Castigliano's method
msc: [74B05, 74K99]
uses: [6W00ZECYT0, E0WD2ATFZD, 0V1EJCT8G6]
about: [6W00ZECYT0]
sources:
  - url: https://en.wikipedia.org/wiki/Castigliano%27s_method
same_as:
  wikidata: Q858978
  wikipedia: Castigliano's method
---

## Statement

Consider an elastic structure in static equilibrium under point forces $F_1, \dots, F_n$, on supports that do no work.
Let $q_i$ be the displacement of the point of application of $F_i$ in the direction of $F_i$.

1. (First theorem) If the structure has a stored strain energy $U$, written as a differentiable function $U(q_1, \dots, q_n)$ of the displacements, then $F_i = \dfrac{\partial U}{\partial q_i}$ for each $i$.
2. (Second theorem) Let the structure obey [[linear elasticity|6W00ZECYT0]], with strain energy written as a function $U(F_1, \dots, F_n)$ of the forces. Then $q_i = \dfrac{\partial U}{\partial F_i}$ for each $i$.

## Remarks

The first theorem follows from the work–energy balance: the change of $U$ when $q_i$ alone changes by $dq_i$ is the work $F_i \, dq_i$.
For the second theorem, linearity gives $q = A F$ with a symmetric flexibility matrix $A$, so $U = \tfrac12 F \cdot A F$ and $\partial U / \partial F_i = (A F)_i = q_i$.
For nonlinear elastic structures the second theorem holds with the complementary energy in place of $U$.
Example: a cantilever of length $L$ and bending stiffness $EI$, loaded by $P$ at its tip, has $U = \int_0^L \frac{(P x)^2}{2EI} \, dx = \frac{P^2 L^3}{6 EI}$, so the tip deflection is $\partial U / \partial P = \frac{P L^3}{3 EI}$.
To find a displacement where no force acts, one adds a fictitious force there, differentiates, and sets it to $0$.

## Explanations

### L1 human

When you load an elastic structure, it stores energy like a spring.
Castigliano's method says that the displacement under a load is the rate at which this stored energy grows with that load.
So, to know how far the tip of a shelf bends, you write down its stored energy and take a derivative.
This often saves much work compared with solving the equations of the deformation directly.

### L2 human

The method is standard in the analysis of beams, frames, trusses and springs.
For statically indeterminate structures, the second theorem applied to a redundant reaction whose support does not move gives $\partial U / \partial R = 0$, an extra equation that determines $R$.
It is closely related to [[Betti's reciprocal theorem|E0WD2ATFZD]], which gives the symmetry of the flexibility matrix, and to the principle of minimum complementary energy.
