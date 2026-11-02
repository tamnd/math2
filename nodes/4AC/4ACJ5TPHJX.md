---
tag: 4ACJ5TPHJX
kind: definition
name: Knot sum
msc: [57K10]
defines: AGZSZW7GYE
uses: [QYEAZTYGPT]
sources:
  - url: https://en.wikipedia.org/wiki/Connected_sum
    locator: Connected sum of knots
---

## Definition

Let $K_1$ and $K_2$ be oriented tame [[knots|QYEAZTYGPT]] in $S^3$.
Choose disjoint closed $3$-balls $B_1, B_2 \subset S^3$ with $K_i \subset B_i$.
Choose a band $b \cong [0,1] \times [0,1]$ in $S^3$ that meets $B_1 \cup B_2$ only in $\set{0, 1} \times [0,1]$.
Require $\set{i-1} \times [0,1] \subset K_i$ for $i = 1, 2$.
Choose the band so that the orientations of $K_1$ and $K_2$ agree with an orientation of the knot below.
The *knot sum* $K_1 \# K_2$ is the oriented knot
$$\big( (K_1 \cup K_2) \setminus (\set{0,1} \times (0,1)) \big) \cup \big( [0,1] \times \set{0, 1} \big).$$

## Remarks

The isotopy class of $K_1 \# K_2$ does not depend on the balls or the band.
Example: if $K_2$ is the [[unknot|1TQ06R4Q66]], the band slides into a trivial arc and $K_1 \# K_2$ is isotopic to $K_1$.
Non-example: if the band is allowed to enter $B_1$ away from $K_1$, it may wind around $K_1$.
Gluing along such a band can give a knot different from $K_1 \# K_2$, so the condition on the band matters.
The sum is commutative and associative on isotopy classes of oriented knots.
The genus of a [[Seifert surface|K866ND3WF7]] is additive, $g(K_1 \# K_2) = g(K_1) + g(K_2)$, so a nontrivial knot has no inverse.
In a diagram, the sum is drawn by placing the two diagrams side by side and replacing two facing arcs by two parallel arcs.
