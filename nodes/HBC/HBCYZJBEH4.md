---
tag: HBCYZJBEH4
kind: proof
name: Proof of the formula for the distance from a point to a line
msc: ["51N20"]
topics: [VKVAJ94SKZ]
audience: school
proves: 01AAYNSBN6
methods: [0NTF6DMVAP, 01XM7JEKHY]
uses: [0MP9BCF6DP, 0NPPGHQNXQ, 0XKBKGTCPC, 0S52TNNTH9, 0WQJJCCTC8, 0BVTDM872V]
sources:
  - url: https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
    locator: Proofs
  - url: https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_plane
    locator: Why this is the closest point
---

## Proof

We find the foot of the perpendicular and compare every other point of the [[line|0MP9BCF6DP]] with it.

1. Let $n = (a, b)$, a [[normal vector|0WQJJCCTC8]] of $L$. Its [[length|0XKBKGTCPC]] $\sqrt{a^2 + b^2}$ is positive, since $n \neq 0$.
2. Let $k = a x_0 + b y_0 + c$, let $t = k / (a^2 + b^2)$, and let $Q_0 = P - t n$.
3. $Q_0 \in L$, since $a (x_0 - t a) + b (y_0 - t b) + c = k - t (a^2 + b^2) = 0$.
4. For $Q \in L$, the [[dot product|0S52TNNTH9]] gives $n \cdot Q = -c$, by the equation of $L$.
5. By steps 3 and 4, $n \cdot Q_0 = -c = n \cdot Q$. So $n \cdot (Q_0 - Q) = 0$.
6. Write $P - Q = t n + (Q_0 - Q)$, by step 2. The two parts are orthogonal by step 5.
7. By the [[Pythagorean theorem for orthogonal vectors|0BVTDM872V]], $\|P - Q\|^2 = t^2 \|n\|^2 + \|Q_0 - Q\|^2 \geq t^2 \|n\|^2$.
8. The [[Euclidean distance|0NPPGHQNXQ]] is $d(P, Q) = \|P - Q\|$. By step 7, $d(P, Q) \geq |t| \, \|n\|$.
9. For $Q = Q_0$, $d(P, Q_0) = \|t n\| = |t| \, \|n\|$. So the bound of step 8 is reached.
10. Hence the least distance is $|t| \, \|n\| = \dfrac{|k|}{\sqrt{a^2 + b^2}}$, which is the formula. $\blacksquare$

## Idea

Move from $P$ along the normal vector $(a, b)$ until the path hits the line.
The path from $P$ to any other point of the line is the hypotenuse of a right triangle with this normal segment as a leg.
So it is at least as long, and the normal segment gives the distance.

## Variants

- Cauchy-Schwarz: for $Q \in L$, $|k| = |n \cdot (P - Q)| \leq \|n\| \, \|P - Q\|$, which gives the lower bound at once.
- Area: for two points $A$, $B$ of $L$, the triangle $ABP$ has the area $\tfrac{1}{2} \|B - A\| \operatorname{dist}(P, L)$. The $2 \times 2$ determinant of $B - A$ and $P - A$ gives the same area.
