---
tag: K8A688YSPW
kind: statement
role: theorem
name: Miquel's theorem
msc: [51M04]
uses: [0CTNFGYMM2, 060W5CBZP6]
about: [0CTNFGYMM2]
sources:
  - url: https://en.wikipedia.org/wiki/Miquel%27s_theorem
same_as:
  wikidata: Q2449984
  wikipedia: Miquel's theorem
---

## Statement

Let $ABC$ be a [[triangle|0CTNFGYMM2]] in the Euclidean plane.
Let $A'$, $B'$, $C'$ be points on the lines $BC$, $CA$, $AB$, each different from the vertices of $ABC$.
Then the three [[circles|060W5CBZP6]] through $A, B', C'$, through $B, C', A'$ and through $C, A', B'$ have a common point.

## Remarks

The three points on each circle are not collinear, since for example $B'$ and $C'$ lie on two different lines through $A$ and differ from $A$.
For a proof, let $M$ be the second common point of the first two circles, or their point of tangency.
Chasing directed angles in the cyclic quadrilaterals $AB'MC'$ and $BC'MA'$ shows that $CA'MB'$ is cyclic too.
The common point is called the Miquel point.
Example: if $A'$, $B'$, $C'$ are the midpoints of the sides, the Miquel point is the [[circumcentre|0F98FZK14A]] $O$.
Indeed, $\angle OB'A$ and $\angle OC'A$ are right angles, so $O$ lies on the circle with diameter $AO$ through $A$, $B'$, $C'$.

## Explanations

### L1 human

Mark one point on each side of a triangle.
Each corner and the two marked points next to it determine a circle.
The three circles you get always pass through one common point.

### L2 human

Miquel's theorem is a standard exercise in angle chasing with cyclic quadrilaterals.
It is the starting point of a family of results on Miquel points of complete quadrilaterals.
