---
tag: E4H8SGZWXW
kind: proof
name: Proof of the change of basis rule for the determinant of a family
msc: [15A15, 15A75]
topics: [DTBK11SR77]
audience: ug2
proves: T1WN2DHS63
methods: [0NTF6DMVAP]
uses: [0V94H674MB, 0VTQTPQGAV, 0BMVBHTWV2, 076JGP6R3T, 04CPJ6AF00, 0Z4BWARC38]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Determinant of n vectors
---

## Proof

We show that the coordinate matrices of $v_1, \dots, v_n$ in the two bases differ by a matrix factor $P$, and then take determinants.

1. Let $P$ be the $n \times n$ matrix whose column $k$ is the [[coordinate vector|0BMVBHTWV2]] $[b'_k]_B$.
   By the [[definition|0V94H674MB]], $\det P = \det_B(B')$.
2. By the choice of $P$, each vector of $B'$ is $b'_k = \sum_i P_{ik} b_i$.
3. Let $v \in V$ and let $c = [v]_{B'}$, so that $v = \sum_k c_k b'_k$.
   Substituting step 2 gives
$$v = \sum_i \Big( \sum_k P_{ik} c_k \Big) b_i.$$
4. Coordinates in the [[basis|0VTQTPQGAV]] $B$ are unique, so the coefficient of $b_i$ in step 3 is entry $i$ of $[v]_B$.
   That coefficient is entry $i$ of the [[matrix product|076JGP6R3T]] $Pc$, so $[v]_B = P [v]_{B'}$.
5. Let $M$ be the matrix with the columns $[v_j]_B$ and $M'$ the matrix with the columns $[v_j]_{B'}$.
   By step 4, column $j$ of $M$ is $P$ times column $j$ of $M'$, so $M = P M'$.
6. By the [[product rule|04CPJ6AF00]], $\det M = \det P \cdot \det M'$.
   By the definition and step 1, this reads
$$\det_B(v_1, \dots, v_n) = \det_B(B') \cdot \det_{B'}(v_1, \dots, v_n).$$
7. Take $v_j = b_j$ for each $j$.
   Then $[b_j]_B$ is the standard column $e_j$, so $\det_B(B) = \det I_n = 1$ by the [[determinant of the identity|0Z4BWARC38]].
8. Step 6 with the family $B$ in place of $v$ gives $1 = \det_B(B) = \det_B(B') \det_{B'}(B)$.
9. Exchange the roles of $B$ and $B'$ in step 6.
   This gives $\det_{B'}(v_1, \dots, v_n) = \det_{B'}(B) \cdot \det_B(v_1, \dots, v_n)$ for every family, which is the last claim.

## Idea

The coordinates of a vector in $B$ are its coordinates in $B'$ multiplied by the change of basis matrix $P$.
So the whole coordinate matrix of the family is multiplied by $P$.
The product rule turns this matrix factor into the number $\det P$, and that number is the determinant of $B'$ in $B$.

## Variants

A proof without matrices uses the fact that the alternating $n$-linear forms on $V$ form a line.
Both $\det_B$ and $\det_{B'}$ lie on that line, so $\det_B = c \det_{B'}$ for some scalar $c$.
Evaluating at $B'$, where $\det_{B'}$ is $1$, gives $c = \det_B(B')$.
