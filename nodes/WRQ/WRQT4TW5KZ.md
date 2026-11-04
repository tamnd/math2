---
tag: WRQT4TW5KZ
kind: proof
name: Proof of the intersecting chords theorem by the power of a point
msc: [51M04]
proves: 0YQQYET8YQ
uses: [049DCJZ448, 0NPPGHQNXQ, 02E9VT1RVQ, 060W5CBZP6, VQ4Q2V45RP, 0S52TNNTH9]
sources:
  - url: https://en.wikipedia.org/wiki/Power_of_a_point
    locator: "Secants theorem, chords theorem: common proof"
---

## Proof

We show that each product equals $r^2 - d(S, O)^2$, where $O$ is the centre and $r$ the radius.

1. The points are [[concyclic|049DCJZ448]] in $\mathbb{R}^2$. So there are a point $O$ and a number $r \geq 0$ with $d(X, O) = r$ for $X = A, B, C, D$, where $d$ is the [[Euclidean distance|0NPPGHQNXQ]].
2. Put $q(t) = t^2 + 2t\, u \cdot (S - O) + \norm{S - O}^2 - r^2$ for a unit vector $u$. With the [[dot product|0S52TNNTH9]], $\norm{S + tu - O}^2 - r^2 = q(t)$. So $S + tu$ is at distance $r$ from $O$ if and only if $q(t) = 0$.
3. Claim: let $X$, $Y$ be points at distance $r$ from $O$, and let $S = (1 - s)X + sY$ with $0 < s < 1$. Then $d(X, S)\, d(S, Y) = r^2 - \norm{S - O}^2$.
4. Proof of the claim when $X = Y$: then $S = X$, so both sides are $0$.
5. Now let $X \neq Y$, and let $u = (Y - X)/\norm{Y - X}$ and $L = \norm{Y - X}$. Then $X = S + t_1 u$ and $Y = S + t_2 u$ with $t_1 = -sL < 0$ and $t_2 = (1 - s)L > 0$.
6. By step 2, $q(t_1) = q(t_2) = 0$. Write $q(t) = t^2 + pt + k$ with $k = \norm{S - O}^2 - r^2$.
7. Subtracting, $0 = q(t_1) - q(t_2) = (t_1 - t_2)(t_1 + t_2 + p)$. Since $t_1 \neq t_2$, we get $p = -(t_1 + t_2)$.
8. Then $0 = q(t_1) = t_1^2 - (t_1 + t_2)t_1 + k = k - t_1 t_2$. So $t_1 t_2 = \norm{S - O}^2 - r^2$.
9. Since $u$ is a unit vector, $d(X, S) = \abs{t_1}$ and $d(S, Y) = \abs{t_2}$. By step 5, $\abs{t_1}\abs{t_2} = -t_1 t_2$. By step 8, this is $r^2 - \norm{S - O}^2$, which proves the claim.
10. The point $S$ is inside the [[segment|VQ4Q2V45RP]] $AC$, so $S = (1 - s)A + sC$ with $0 < s < 1$. By the claim, $d(A, S)\, d(S, C) = r^2 - d(S, O)^2$.
11. In the same way, $S$ is inside the segment $BD$, so $d(B, S)\, d(S, D) = r^2 - d(S, O)^2$.
12. Hence $d(A, S)\, d(S, C) = d(B, S)\, d(S, D)$. Both products are minus the [[power|02E9VT1RVQ]] of $S$.

## Idea

Along a line through $S$, the points of the [[circle|060W5CBZP6]] are the roots of a quadratic equation in the signed distance from $S$. The product of the roots is the constant term $d(S, O)^2 - r^2$, which does not depend on the line. The two roots have opposite signs, so each chord through $S$ gives the product $r^2 - d(S, O)^2$.
