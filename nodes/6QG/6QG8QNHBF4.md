---
tag: 6QG8QNHBF4
kind: statement
role: theorem
name: Double bubble theorem
msc: [49Q10, 49Q20, 53A10]
uses: [W6R7QNEAF1, Q1TGZK8RN6, KBX8RBZ626]
about: [W6R7QNEAF1]
sources:
  - url: https://en.wikipedia.org/wiki/Double_bubble_theorem
same_as:
  wikidata: Q5299978
  wikipedia: Double bubble theorem
---

## Statement

Let $V_1, V_2 > 0$.
Consider pairs $(E_1, E_2)$ of disjoint [[Caccioppoli sets|W6R7QNEAF1]] in $\R^3$ with volumes $\abs{E_1} = V_1$ and $\abs{E_2} = V_2$.
For such a pair, let $A(E_1, E_2) = \mathcal{H}^2(\partial^* E_1 \cup \partial^* E_2)$ be the total area of the interfaces.
Here $\partial^*$ is the reduced boundary and $\mathcal{H}^2$ is the $2$-dimensional [[Hausdorff measure|Q1TGZK8RN6]], so that a common wall is counted once.
Then $A$ is least for the standard double bubble with volumes $V_1$ and $V_2$.
Every minimizing pair is a standard double bubble, up to a rigid motion and up to sets of measure zero.

The *standard double bubble* is made of three spherical caps, or of two caps and a flat disc when $V_1 = V_2$.
The three pieces have a common boundary circle and meet along it at angles of $120^\circ$.

## Remarks

Michael Hutchings, Frank Morgan, Manuel Ritoré and Antonio Ros proved the theorem, published in 2002.
Existence and regularity of a minimizer come from geometric measure theory.
Hutchings showed that a minimizer is a surface of revolution about a line, with strong limits on the number of components of its regions.
The authors then excluded the remaining non-standard candidates by an instability argument based on rotating parts of the surface.
The case of equal volumes had been proved earlier by Joel Hass and Roger Schlafly with computer help.
The analogous result in the plane, with circular arcs in place of spherical caps, had been proved earlier by a group of undergraduates.
Ben Reichardt later extended the theorem to all dimensions.
For one region instead of two, the corresponding statement is the [[isoperimetric inequality|KBX8RBZ626]]: the ball encloses a given volume with least area.

## Explanations

### L1 human

Blow two soap bubbles that stick together.
They form two spherical pieces separated by a third spherical wall, all meeting along a circle at equal angles.
The theorem says that this familiar shape is the cheapest possible way, in surface area, to enclose and separate two given volumes of air.

### L2 human

The theorem is the simplest case of the problem of least-area clusters, and it shows how hard such problems are.
The single-bubble case is classical, but the two-bubble case needed new ideas in the 1990s.
The $120^\circ$ angles agree with Plateau's laws, which every minimizer must satisfy.
The analogous problem for three or more bubbles in $\R^3$ is much harder.
