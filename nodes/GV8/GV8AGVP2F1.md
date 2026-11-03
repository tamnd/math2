---
tag: GV8AGVP2F1
kind: definition
name: Algebraic geometry code
msc: [94B27, 14G50]
defines: DY3CHS08CT
uses: [E85KREWV60, XJM2MT4S3Y, SWJYG87QQH, Z9DN23DAE2, 6W8TDV9VVN, WMVAT9MBZ1, 0ZXZ82FTX2, 5VBWJ7EFTX]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_geometry_code
---

## Definition

Let $X$ be a smooth, projective, geometrically irreducible [[algebraic curve|XJM2MT4S3Y]] over the [[finite field|0ZXZ82FTX2]] $\F_q$, of [[genus|6W8TDV9VVN]] $g$.
Let $P_1, \dots, P_n$ be distinct $\F_q$-[[rational points|SWJYG87QQH]] of $X$.
Let $G$ be a [[divisor|Z9DN23DAE2]] on $X$ defined over $\F_q$ whose support contains none of the $P_i$.
Let $L(G)$ be the Riemann–Roch space of $G$: the $\F_q$-vector space of rational functions $f$ on $X$ with $f = 0$ or $\operatorname{div}(f) + G \ge 0$.
The *algebraic geometry code* $C_L(D, G)$, where $D = P_1 + \cdots + P_n$, is
$$C_L(D, G) = \set{(f(P_1), \dots, f(P_n)) : f \in L(G)}.$$

## Remarks

Each $f \in L(G)$ has no pole at any $P_i$, since the $P_i$ are not in the support of $G$, so the values $f(P_i) \in \F_q$ are defined.
Suppose $\deg G < n$.
A nonzero $f \in L(G)$ that vanishes at $w$ of the points lies in $L(G - \sum_{i \in S} P_i)$ for a set $S$ of size $w$, which is zero when $w > \deg G$.
So the evaluation map is injective, and each nonzero codeword has weight at least $n - \deg G$.
By the [[Riemann–Roch theorem|WMVAT9MBZ1]], the dimension is $k = \ell(G) \ge \deg G + 1 - g$, with equality when $2g - 2 < \deg G$.
Hence $k + d \ge n + 1 - g$.

Example: $X = \mathbb{P}^1$ over $\F_q$, so $g = 0$, with $P_1, \dots, P_n$ distinct points of the affine line and $G = (k - 1) \infty$ for some $1 \le k \le n$.
Then $L(G)$ is the space of polynomials of degree at most $k - 1$, and $C_L(D, G)$ is the [[Reed–Solomon code|5VBWJ7EFTX]] of dimension $k$ at these points.

Non-example: if $G = P_1$, the support condition fails.
The function $1/(x - a_1)$ on $\mathbb{P}^1$, where $P_1$ is the point $x = a_1$, lies in $L(P_1)$ but has a pole at $P_1$, so its value there is not defined.
