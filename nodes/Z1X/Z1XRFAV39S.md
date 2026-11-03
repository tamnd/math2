---
tag: Z1XRFAV39S
kind: definition
name: Magnetic vector potential
msc: [78A30, 78A25]
defines: 8PEMR2J7EF
uses: [XRED3C547P, 0NF6GQNXMY, 0299VCW1TH, 2K5D5HH89T, RA4GE6185Q, 0ABK9V9Y64]
sources:
  - url: https://en.wikipedia.org/wiki/Magnetic_vector_potential
---

## Definition

Let $U \subseteq \R^3$ be an open set and let $B \colon U \to \R^3$ be a continuously differentiable [[magnetic field|XRED3C547P]].
A *magnetic vector potential* for $B$ is a continuously differentiable [[vector field|0299VCW1TH]] $A \colon U \to \R^3$ such that
$$\nabla \times A = B \quad \text{on } U,$$
where $\nabla \times$ is the [[curl|0NF6GQNXMY]].

## Remarks

If $U$ is star-shaped, a vector potential exists because $\nabla \cdot B = 0$ by [[Gauss's law for magnetism|2K5D5HH89T]]; this is the Poincaré lemma for $2$-forms.
If $A$ is a vector potential, so is $A + \nabla \chi$ for every twice continuously differentiable function $\chi$, with [[gradient|0ABK9V9Y64]] $\nabla \chi$.
On a simply connected $U$ these are all of them.
This freedom is the gauge freedom, and a condition such as $\nabla \cdot A = 0$ selects one potential.
Example: the uniform field $B = (0, 0, B_0)$ has the vector potential $A(x) = \tfrac{B_0}{2} (-x_2, x_1, 0)$; the check is $\partial_1 A_2 - \partial_2 A_1 = B_0$ and the other components of the curl vanish.
Another vector potential of the same field is $(0, B_0 x_1, 0)$.
Non-example: $A(x) = (x_1, 0, 0)$ is not a vector potential of any nonzero field, since its curl is $0$.
For a steady current density $J$ as in the [[Biot–Savart law|RA4GE6185Q]], $A(x) = \frac{\mu_0}{4 \pi} \int J(y) / \abs{x - y} \, dy$ is a vector potential of its field with $\nabla \cdot A = 0$.
