---
tag: PYJ4W9RDFE
kind: proof
name: Proof of the Weinstein-Aronszajn identity by two block factorizations
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug2
proves: 0G24VQ1088
methods: [0NTF6DMVAP]
uses: [01AXG9KZQF, 076JGP6R3T, 04CPJ6AF00, 0J9TVTNB4K, 0ZZQ2E1MTE, 0W809K6AW0, 0Z4BWARC38, 06DW9BAWB1]
sources:
  - url: https://en.wikipedia.org/wiki/Weinstein–Aronszajn_identity
---

## Proof

We write one block matrix as a product in two different orders, and we compare the two values of its determinant.

1. Let $A$ be $m \times n$ and $B$ be $n \times m$ over the commutative ring $K$, with $m, n \ge 1$.
   Form the [[block matrix|01AXG9KZQF]] of size $m + n$
$$M = \begin{pmatrix} I_m & -A \\ B & I_n \end{pmatrix},$$
   where $I_m$ and $I_n$ are [[identity matrices|06DW9BAWB1]].
2. Block matrices with the same splitting of rows and columns multiply block by block.
   This holds because each sum $\sum_k X_{rk} Y_{ks}$ in the [[matrix product|076JGP6R3T]] splits into the terms with $k \le m$ and the terms with $k > m$.
3. Put
$$L = \begin{pmatrix} I_m & 0 \\ B & I_n \end{pmatrix}, \qquad U_1 = \begin{pmatrix} I_m & -A \\ 0 & I_n + BA \end{pmatrix}.$$
   By step 2, the four blocks of $L U_1$ are $I_m$, $-A$, $B$ and $B(-A) + (I_n + BA) = I_n$.
   So $L U_1 = M$.
4. Put
$$U_2 = \begin{pmatrix} I_m + AB & -A \\ 0 & I_n \end{pmatrix}.$$
   By step 2, the four blocks of $U_2 L$ are $(I_m + AB) + (-A)B = I_m$, $-A$, $B$ and $I_n$.
   So $U_2 L = M$.
5. The [[transpose|0W809K6AW0]] of $L$ is block upper triangular with diagonal blocks $I_m$ and $I_n$.
   By the rule for the [[determinant of a transpose|0ZZQ2E1MTE]], the rule for [[block triangular matrices|0J9TVTNB4K]] and $\det I = 1$ from the [[determinant of the identity|0Z4BWARC38]], we get $\det L = 1$.
6. By the rule for block triangular matrices, $\det U_1 = \det I_m \cdot \det(I_n + BA) = \det(I_n + BA)$.
7. By the same rule, $\det U_2 = \det(I_m + AB) \cdot \det I_n = \det(I_m + AB)$.
8. By [[multiplicativity of the determinant|04CPJ6AF00]] and steps 3, 5 and 6, $\det M = \det L \cdot \det U_1 = \det(I_n + BA)$.
9. By multiplicativity and steps 4, 5 and 7, $\det M = \det U_2 \cdot \det L = \det(I_m + AB)$.
10. Steps 8 and 9 give two values of the same number $\det M$, so $\det(I_m + AB) = \det(I_n + BA)$.

## Idea

The block matrix $M$ has the identity in both diagonal corners and the two factors $-A$ and $B$ off the diagonal.
We can make it block triangular in two ways, by clearing $B$ or by clearing $-A$ with a block row operation.
Clearing $B$ leaves $I_n + BA$ in the corner, and clearing $-A$ leaves $I_m + AB$.
A block row operation with an identity on the diagonal does not change the determinant, so the two corners have the same determinant.

## Variants

The [[Schur complement formula|0KA7A4ENVJ]] gives the same two values directly.
The complement of the corner $I_m$ is $I_n - B I_m^{-1} (-A) = I_n + BA$, so $\det M = \det(I_n + BA)$.
The complement of the corner $I_n$ is $I_m - (-A) I_n^{-1} B = I_m + AB$, so $\det M = \det(I_m + AB)$.
This is the same argument in other words, because the Schur complement formula is itself proved by the two block factorizations above.
