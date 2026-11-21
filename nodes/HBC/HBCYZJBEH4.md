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

We find the foot of the perpendicular and then compare every other point of the [[line|0MP9BCF6DP]] with it.

1. Let $n = (a, b)$, a [[normal vector|0WQJJCCTC8]] of $L$. Its [[length|0XKBKGTCPC]] $\sqrt{a^2 + b^2}$ is positive, since $n \neq 0$.
2. Let $k = a x_0 + b y_0 + c$, let $t = k / (a^2 + b^2)$, and let $Q_0 = P - t n$.
3. The point $Q_0$ lies on $L$, since
   $$a (x_0 - t a) + b (y_0 - t b) + c = k - t (a^2 + b^2) = 0.$$
4. For every $Q \in L$, the equation of $L$ says $n \cdot Q = -c$, in terms of the [[dot product|0S52TNNTH9]].
5. By steps 3 and 4, $n \cdot Q_0 = -c = n \cdot Q$, so $n \cdot (Q_0 - Q) = 0$.
6. By step 2, $P - Q = t n + (Q_0 - Q)$, and the two parts are orthogonal by step 5.
7. By the [[Pythagorean theorem for orthogonal vectors|0BVTDM872V]],
   $$\|P - Q\|^2 = t^2 \|n\|^2 + \|Q_0 - Q\|^2 \geq t^2 \|n\|^2.$$
8. The [[Euclidean distance|0NPPGHQNXQ]] is $d(P, Q) = \|P - Q\|$, so step 7 gives $d(P, Q) \geq |t| \, \|n\|$ for every $Q \in L$.
9. For $Q = Q_0$ we get $d(P, Q_0) = \|t n\| = |t| \, \|n\|$, so the bound of step 8 is reached.
10. Hence the least distance exists and equals $|t| \, \|n\| = \dfrac{|k|}{\sqrt{a^2 + b^2}}$, which is the formula. $\blacksquare$

## Idea

Move from $P$ along the normal vector $(a, b)$ until the path hits the line.
The path from $P$ to any other point of the line is the hypotenuse of a right triangle that has this normal segment as a leg.
So every other path is at least as long, and the normal segment gives the distance.

## Variants

The Cauchy-Schwarz inequality gives the lower bound in one line.
For $Q \in L$ we have $n \cdot Q = -c$, so $k = n \cdot (P - Q)$, and then $|k| \leq \|n\| \, \|P - Q\|$.
Dividing by $\|n\|$ gives $d(P, Q) \geq |k| / \|n\|$, and the point $Q_0$ shows that the bound is reached.

Areas give another route.
For two points $A$ and $B$ of $L$, the triangle $ABP$ has area $\tfrac{1}{2} \|B - A\| \operatorname{dist}(P, L)$, base times height over two.
The same area is half the absolute value of the $2 \times 2$ determinant with rows $B - A$ and $P - A$, and comparing the two expressions gives the distance.
