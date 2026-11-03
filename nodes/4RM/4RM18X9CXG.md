---
tag: 4RM18X9CXG
kind: statement
role: fact
name: Coulomb's law
msc: [78A30]
uses: [6XPSV47R56]
about: [6XPSV47R56]
sources:
  - url: https://en.wikipedia.org/wiki/Coulomb%27s_law
same_as:
  wikidata: Q83152
  wikipedia: Coulomb's law
---

## Statement

Let two point [[charges|6XPSV47R56]] $q_1$ and $q_2$ be at rest at distinct points $x_1$ and $x_2$ of $\R^3$ in vacuum.
Let $\varepsilon_0 > 0$ be the vacuum permittivity.
Then the force exerted by the first charge on the second is
$$F_{12} = \frac{1}{4 \pi \varepsilon_0} \, \frac{q_1 q_2}{\abs{x_2 - x_1}^2} \, \frac{x_2 - x_1}{\abs{x_2 - x_1}}.$$

## Remarks

Coulomb's law is a law of physics, established by experiment, and not a theorem.
The force is along the line through the two charges, it is repulsive when $q_1 q_2 > 0$ and attractive when $q_1 q_2 < 0$, and its size decays like the inverse square of the distance.
By Newton's third law $F_{21} = -F_{12}$, which the formula shows by exchanging the indices.
Forces from several charges add as vectors; this superposition principle is part of the law.
For example, two charges of $1$ coulomb at distance $1$ metre repel with a force of about $9 \times 10^9$ newtons.
The same inverse-square form appears in Newton's law of gravitation, with masses in place of charges and attraction in place of repulsion.

## Explanations

### L1 human

Coulomb's law tells how strongly two charged objects push or pull each other.
Double one of the charges and the force doubles.
Double the distance and the force becomes four times weaker.
Charges of the same sign repel, and charges of opposite sign attract.

### L2 human

Coulomb's law is the starting point of electrostatics.
Dividing the force on a test charge by its charge gives the electric field of the source charges.
The field of a point charge is the gradient of the potential $1/(4 \pi \varepsilon_0 r)$, which is a multiple of the fundamental solution of the Laplacian.
From this one derives Gauss's law and Poisson's equation, which are the differential form of Coulomb's law.
