---
tag: HBCYZJBEH4
kind: proof
name: Proof of the formula for the distance from a point to a line
msc: [51N20]
proves: 01AAYNSBN6
uses: [0MP9BCF6DP, 0NPPGHQNXQ, 0XKBKGTCPC, 0S52TNNTH9, 0WQJJCCTC8, 0BVTDM872V]
sources:
  - url: https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
    locator: Proofs
  - url: https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_plane
    locator: Why this is the closest point
---

## Proof

We find the foot of the perpendicular and compare every other point of the [[line|0MP9BCF6DP]] with it.

1. Let $n = (a, b)$. It is a [[normal vector|0WQJJCCTC8]] of $L$. Since $(a, b) \neq (0, 0)$, its [[length|0XKBKGTCPC]] $\norm{n} = \sqrt{a^2 + b^2}$ is positive.
2. Let $k = a x_0 + b y_0 + c$, let $t = k / (a^2 + b^2)$, and let $Q_0 = P - t n = (x_0 - t a, \, y_0 - t b)$.
3. The point $Q_0$ lies on $L$. Indeed, $a (x_0 - t a) + b (y_0 - t b) + c = k - t (a^2 + b^2) = k - k = 0$.
4. Let $Q = (x, y)$ be any point of $L$. With the [[dot product|0S52TNNTH9]], $n \cdot Q = a x + b y = -c$. By step 3 also $n \cdot Q_0 = -c$. So $n \cdot (Q_0 - Q) = 0$.
5. We have $P - Q = (P - Q_0) + (Q_0 - Q) = t n + (Q_0 - Q)$. The two summands are orthogonal by step 4.
6. By the [[Pythagorean theorem for orthogonal vectors|0BVTDM872V]], $\norm{P - Q}^2 = t^2 \norm{n}^2 + \norm{Q_0 - Q}^2 \geq t^2 \norm{n}^2$.
7. The [[Euclidean distance|0NPPGHQNXQ]] is $d(P, Q) = \norm{P - Q}$. Taking square roots in step 6 gives $d(P, Q) \geq \abs{t} \, \norm{n}$ for each $Q \in L$.
8. For $Q = Q_0$, we get $d(P, Q_0) = \norm{t n} = \abs{t} \, \norm{n}$. So the bound of step 7 is reached at the point $Q_0$ of $L$.
9. Hence the smallest distance exists and equals $\abs{t} \, \norm{n} = \dfrac{\abs{k}}{a^2 + b^2} \sqrt{a^2 + b^2} = \dfrac{\abs{a x_0 + b y_0 + c}}{\sqrt{a^2 + b^2}}$.

## Idea

Move from $P$ along the normal vector $(a, b)$ until you hit the line. The path from $P$ to any other point of the line is the hypotenuse of a right triangle with this normal segment as a leg. So it is at least as long, and the normal segment gives the distance.
