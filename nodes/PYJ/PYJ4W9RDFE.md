---
tag: PYJ4W9RDFE
kind: proof
name: Proof of Sylvester's determinant theorem by two block factorizations
msc: [15A15]
proves: 0G24VQ1088
uses: [01AXG9KZQF, 076JGP6R3T, 04CPJ6AF00, 0J9TVTNB4K, 0ZZQ2E1MTE, 0W809K6AW0, 0Z4BWARC38, 06DW9BAWB1]
sources:
  - url: https://en.wikipedia.org/wiki/Weinstein–Aronszajn_identity
---

## Proof

We factor one block matrix in two ways and compare the determinants.

1. Let $A$ be $m \times n$ and $B$ be $n \times m$ over $K$, with $m, n \ge 1$, since matrices have at least one row and column. Let $M = \begin{pmatrix} I_m & -A \\ B & I_n \end{pmatrix}$, a [[block matrix|01AXG9KZQF]] of size $m + n$.
2. By the definition of the [[matrix product|076JGP6R3T]], split each sum $\sum_k X_{rk} Y_{ks}$ into the indices $k \le m$ and $k > m$. So block matrices with the same splitting multiply block by block.
3. Let $L_1 = \begin{pmatrix} I_m & 0 \\ B & I_n \end{pmatrix}$ and $U_1 = \begin{pmatrix} I_m & -A \\ 0 & I_n + BA \end{pmatrix}$, with [[identity matrices|06DW9BAWB1]] $I_m, I_n$.
4. By step 2, the blocks of $L_1 U_1$ are $I_m$, $-A$, $B$ and $-BA + I_n + BA = I_n$. So $L_1 U_1 = M$.
5. Let $U_2 = \begin{pmatrix} I_m + AB & -A \\ 0 & I_n \end{pmatrix}$. We claim that $M = U_2 L_1$.
6. By step 2, the blocks of $U_2 L_1$ are $(I_m + AB) - AB = I_m$, $-A$, $B$ and $I_n$. So $U_2 L_1 = M$.
7. The [[transpose|0W809K6AW0]] of $L_1$ is upper block triangular with diagonal blocks $I_m$ and $I_n$.
8. By the rule for the [[determinant of a transpose|0ZZQ2E1MTE]], the rule for [[block triangular matrices|0J9TVTNB4K]] and the [[determinant of the identity|0Z4BWARC38]], $\det L_1 = 1$.
9. By the rule for block triangular matrices, $\det U_1 = \det I_m \cdot \det(I_n + BA) = \det(I_n + BA)$.
10. In the same way, $\det U_2 = \det(I_m + AB) \cdot \det I_n = \det(I_m + AB)$.
11. By the [[product rule|04CPJ6AF00]] and steps 4, 8 and 9, $\det M = \det(I_n + BA)$.
12. By the product rule and steps 6, 8 and 10, $\det M = \det(I_m + AB)$.
13. By steps 11 and 12, $\det(I_m + AB) = \det(I_n + BA)$.

## Idea

The matrix $\begin{pmatrix} I_m & -A \\ B & I_n \end{pmatrix}$ can be made block triangular by clearing either $B$ or $-A$. Clearing $B$ leaves $I_n + BA$ on the diagonal, and clearing $-A$ leaves $I_m + AB$. Both operations keep the determinant, so the two results agree.
