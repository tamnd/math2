---
tag: 3CJEWF0Y3F
kind: statement
role: theorem
name: Erdős–Mordell inequality
msc: [51M16]
uses: [0CTNFGYMM2, 0NPPGHQNXQ]
about: [0CTNFGYMM2]
sources:
  - url: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Mordell_inequality
same_as:
  wikidata: Q990530
  wikipedia: Erdős–Mordell inequality
---

## Statement

Let $ABC$ be a [[triangle|0CTNFGYMM2]] in the Euclidean plane and let $P$ be a point inside $ABC$ or on its boundary.
Let $p$, $q$, $r$ be the distances from $P$ to the lines $BC$, $CA$, $AB$.
Then
$$PA + PB + PC \ge 2(p + q + r).$$
Equality holds if and only if $ABC$ is equilateral and $P$ is its centre.

## Remarks

Write $a = BC$, $b = CA$ and $c = AB$.
One proof reflects $P$ in the bisector of the angle at $A$ and compares areas; this gives $a \cdot PA \ge b r + c q$.
Adding the three such bounds and using $t + 1/t \ge 2$ for $t > 0$ gives the inequality.
Example: let $ABC$ be equilateral with side $2$ and let $P$ be its centre.
Each distance to a vertex is $2/\sqrt 3$ and each distance to a side is $1/\sqrt 3$, so both sides equal $2\sqrt 3$.
The hypothesis that $P$ lies in the closed triangle is needed.
For some points far outside the triangle, the distances to the side lines are large compared to the distances to the vertices, and the inequality fails.
Erdős posed the inequality as a problem, and Mordell and Barrow gave the first proof.

## Explanations

### L1 human

Stand at a point inside a triangle.
Add up your distances to the three corners, then add up your distances to the three sides.
The first sum is always at least twice the second.
Only the centre of an equilateral triangle makes the two sides equal.

### L2 human

The inequality is a classic of olympiad geometry and a model for many inequalities that compare vertex distances with side distances.
Its proofs use [[Euclidean distance|0NPPGHQNXQ]] and area arguments, or the law of cosines combined with the inequality between arithmetic and geometric means.
