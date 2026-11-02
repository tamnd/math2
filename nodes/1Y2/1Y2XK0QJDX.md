---
tag: 1Y2XK0QJDX
kind: statement
role: theorem
name: Saccheri–Legendre theorem
msc: [51F05, 51M09]
uses: [VKFPCSRNDH, 0CTNFGYMM2, 0GJAJC6TNZ, 0NTSE7EREA]
about: [VKFPCSRNDH]
sources:
  - url: https://en.wikipedia.org/wiki/Saccheri%E2%80%93Legendre_theorem
same_as:
  wikidata: Q7396621
  wikipedia: Saccheri–Legendre theorem
---

## Statement

Let $\Pi$ be an [[absolute plane|VKFPCSRNDH]] that satisfies the axiom of Archimedes.
Then the sum of the three [[angles|0GJAJC6TNZ]] of every [[triangle|0CTNFGYMM2]] in $\Pi$ is at most two right angles.

## Remarks

The proof starts from a triangle $ABC$ and builds a new triangle with the same angle sum, one of whose angles is at most half of the angle at $A$.
Repeating this $n$ times gives a triangle with the same angle sum and an angle at most $2^{-n}$ times the angle at $A$.
If the angle sum exceeded two right angles by some angle $\varepsilon$, the axiom of Archimedes would give a step where this small angle is less than $\varepsilon$.
Then the other two angles would sum to more than two right angles, which contradicts the [[exterior angle theorem|0NTSE7EREA]].
The axiom of Archimedes is needed: Max Dehn built non-Archimedean geometries in which the other axioms hold and some triangles have angle sum greater than two right angles.

## Explanations

### L1 human

Without the parallel postulate, one cannot prove that the angles of a triangle add up to $180^\circ$.
But one can still prove that they never add up to more than $180^\circ$.
In the Euclidean plane the sum is exactly $180^\circ$, and in the hyperbolic plane it is always less.

### L2 human

The theorem is one of the main results of absolute geometry.
With it, the parallel postulate is equivalent to the existence of a single triangle with angle sum $180^\circ$.
The defect of a triangle is two right angles minus its angle sum.
It is additive when a triangle is cut into two, and in the hyperbolic plane it is proportional to the area.
