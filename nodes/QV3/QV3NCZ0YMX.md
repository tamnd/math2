---
tag: QV3NCZ0YMX
kind: proof
name: Proof of the intersecting secants theorem by the power of a point
msc: [51M04]
proves: 0J5XR7BW2S
uses: [049DCJZ448, 0NPPGHQNXQ, 02E9VT1RVQ, 060W5CBZP6, 0MP9BCF6DP, 0S52TNNTH9]
sources:
  - url: https://en.wikipedia.org/wiki/Power_of_a_point
    locator: "Secants theorem, chords theorem: common proof"
---

## Proof

We show that each product equals the absolute value of $d(P, O)^2 - r^2$.

1. The points are [[concyclic|049DCJZ448]] in $\mathbb{R}^2$. So there are a point $O$ and a number $r \geq 0$ with $d(X, O) = r$ for $X = A, B, C, D$, where $d$ is the [[Euclidean distance|0NPPGHQNXQ]].
2. For a unit vector $u$, put $q(t) = t^2 + 2t\, u \cdot (P - O) + k$ with $k = \norm{P - O}^2 - r^2$. With the [[dot product|0S52TNNTH9]], $\norm{P + tu - O}^2 - r^2 = q(t)$.
3. Claim: let $X \neq Y$ be points at distance $r$ from $O$, and let $P$ be on the [[line|0MP9BCF6DP]] $XY$. Then $d(P, X)\, d(P, Y) = \abs{k}$.
4. Proof of the claim: let $u = (Y - X)/\norm{Y - X}$. The line $XY$ is $\set{P + tu : t \in \mathbb{R}}$, since it contains $P$ and has the direction $u$. So $X = P + t_1 u$ and $Y = P + t_2 u$, with $t_1 \neq t_2$ since $X \neq Y$.
5. By step 2, $q(t_1) = q(t_2) = 0$. Write $q(t) = t^2 + pt + k$.
6. Subtracting, $0 = q(t_1) - q(t_2) = (t_1 - t_2)(t_1 + t_2 + p)$. Since $t_1 \neq t_2$, we get $p = -(t_1 + t_2)$.
7. Then $0 = q(t_1) = t_1^2 - (t_1 + t_2)t_1 + k = k - t_1 t_2$. So $t_1 t_2 = k$.
8. Since $u$ is a unit vector, $d(P, X) = \abs{t_1}$ and $d(P, Y) = \abs{t_2}$. So $d(P, X)\, d(P, Y) = \abs{t_1 t_2} = \abs{k}$, which proves the claim.
9. Apply the claim to $X = A$, $Y = D$, which is allowed since $A \neq D$ and $P$ is on the line $AD$. This gives $d(P, A)\, d(P, D) = \abs{k}$.
10. Apply it to $X = B$, $Y = C$, since $B \neq C$ and $P$ is on the line $BC$. This gives $d(P, B)\, d(P, C) = \abs{k}$.
11. Hence $d(P, A)\, d(P, D) = d(P, B)\, d(P, C)$. Since $P$ is outside the [[circle|060W5CBZP6]], $k > 0$, and both products equal the [[power|02E9VT1RVQ]] $k$ of $P$.

## Idea

Along a line through $P$, the points of the circle are the roots of a quadratic equation in the signed distance from $P$. The product of the two roots is the constant term $d(P, O)^2 - r^2$. This term depends only on $P$, not on the line, so both secants give the same product.
