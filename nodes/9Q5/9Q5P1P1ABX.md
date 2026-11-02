---
tag: 9Q5P1P1ABX
kind: statement
role: theorem
name: Napoleon's theorem
msc: [51M04]
uses: [0CTNFGYMM2, 0X7EEWES5G, 01KJJ9A400]
about: [0CTNFGYMM2]
sources:
  - url: https://en.wikipedia.org/wiki/Napoleon%27s_theorem
same_as:
  wikidata: Q637418
  wikipedia: Napoleon's theorem
---

## Statement

Let $ABC$ be a [[triangle|0CTNFGYMM2]] in the Euclidean plane.
On each side of $ABC$ erect an equilateral triangle, either all three outside $ABC$ or all three overlapping $ABC$ inwards.
Let $X$, $Y$ and $Z$ be the [[centroids|0X7EEWES5G]] of the equilateral triangles on $BC$, $CA$ and $AB$.
Then $XYZ$ is an equilateral triangle.

## Remarks

A short proof uses rotations.
For the outer case, the rotations by $120^\circ$ about $Z$, $X$ and $Y$, in the same sense, send $A$ to $B$, $B$ to $C$ and $C$ to $A$.
Their composition has total angle $360^\circ$, so it is a translation, and it fixes $A$, so it is the identity.
Three rotations by $120^\circ$ whose composition is the identity have centres that form an equilateral triangle.
The triangle $XYZ$ is called the outer or the inner Napoleon triangle.
Both Napoleon triangles have the same centroid as $ABC$, and the area of the outer one minus the area of the inner one equals the area of $ABC$.
For an equilateral triangle $ABC$ the inner Napoleon triangle degenerates to a single point, its centre.

## Explanations

### L1 human

Take any triangle, even a very lopsided one.
Draw an equilateral triangle on each of its sides, pointing outwards, and mark the centre of each.
The three centres always form an equilateral triangle.
The irregular shape of the starting triangle disappears completely.

### L2 human

The theorem is a standard exercise for complex numbers or for compositions of rotations in the plane.
The same equilateral triangles appear in the construction of the [[Fermat point|QM0CGSQ4TF]].
The lines joining each vertex to the apex of the outer equilateral triangle on the opposite side meet in one point.
It is one of the first examples where a [[regular polygon|01KJJ9A400]] is produced from an arbitrary triangle by a fixed recipe.
