---
tag: KV2HTFBJRC
kind: definition
name: Elliptic-curve cryptography
msc: [94A60, 14G50, 11T71]
defines: X1W8HKH73X
uses: [SJ2BVG9F4W, 0ZXZ82FTX2, 0HJHYMGN3C, 01E9MNJYEX, 01TKKESHSB]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic-curve_cryptography
---

## Definition

Let $\F_q$ be a [[finite field|0ZXZ82FTX2]] and let $E$ be an [[elliptic curve|SJ2BVG9F4W]] over $\F_q$.
Let $E(\F_q)$ be the finite abelian group of its points with coordinates in $\F_q$, together with the point at infinity $O$.
Let $P \in E(\F_q)$ be a point of order $n$.
The *elliptic curve [[discrete logarithm|0HJHYMGN3C]] problem* for $(E, P)$ asks, given $Q$ in the subgroup $\langle P \rangle$, for the integer $k \in \set{0, \dots, n - 1}$ with $Q = kP$.
*Elliptic-curve cryptography* is the use of the group $\langle P \rangle$ in [[public-key|01E9MNJYEX]] schemes whose security rests on the hardness of this problem.

## Remarks

The basic scheme is elliptic-curve [[Diffie–Hellman|01TKKESHSB]].
Alice picks a secret $a$ and publishes $aP$, Bob picks a secret $b$ and publishes $bP$, and both compute the shared point $abP = a(bP) = b(aP)$.

Example: $E \colon y^2 = x^3 + 2x + 2$ over $\F_{17}$, with $P = (5, 1)$.
The point lies on $E$, since $1 = 125 + 10 + 2 = 137 \equiv 1 \pmod{17}$.
Its multiples are $2P = (6, 3)$, $3P = (10, 6)$, $4P = (3, 1)$, and $P$ has order $19$.
With $a = 2$ and $b = 3$, Alice publishes $(6, 3)$, Bob publishes $(10, 6)$, and both obtain $6P$.

Non-example: the curve $y^2 = x^3$ over $\F_p$ is singular at $(0, 0)$, so it is not an elliptic curve.
Its nonsingular points form a group isomorphic to the additive group of $\F_p$, where discrete logarithms are easy to compute.

In practice $n$ is a prime of about $256$ bits and the curve is chosen to avoid known weak classes.
