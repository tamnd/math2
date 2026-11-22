---
tag: ZRPHF64HFG
kind: proof
name: Proof of the QR decomposition by clearing the first column
msc: [15A23, 65F25]
topics: [8GQVME4SZZ]
audience: ug1
proves: 0ERWG4NXQ9
uses: [0D6RMJ10M9, 0QRBVFJ50X, 0MKABWDRNC, 0EX045E2BP, 0VGSYBWHV2, 09VYHEF2VT, 0Y85GYEGSF, 0753Y2X5K6, 09GK5PS824, 04CPJ6AF00, 0K1KKMFHYH, FBSAPTP1PR]
sources:
  - url: https://linear.pugetsound.edu/scla/html/section-QR.html
---

## Proof

This proof covers part 4 of the statement, the square case, and the [[proof by Gram-Schmidt|KHFJXQDZGC]] covers parts 1 to 3.
We prove existence by induction on $n$, clearing the first column with a unitary matrix, and we prove uniqueness by comparing two factorizations.

Facts on unitary matrices.

1. For $x, y \in \C^n$ let $\ip{x}{y} = y^* x = \sum_i x_i \overline{y_i}$, where $^*$ is the [[conjugate transpose|0EX045E2BP]]; this is an [[inner product|0VGSYBWHV2]], because it is linear in $x$, satisfies $\ip{y}{x} = \overline{\ip{x}{y}}$, and gives $\ip{x}{x} = \sum_i \abs{x_i}^2 > 0$ for $x \ne 0$.
2. For an $n \times n$ matrix $W$ with columns $w_1, \dots, w_n$, entry $(i, j)$ of $W^* W$ is $w_i^* w_j = \ip{w_j}{w_i}$, so $W$ is [[unitary|0D6RMJ10M9]] if and only if its columns form an [[orthonormal family|09VYHEF2VT]].
3. For complex matrices $X$ and $Y$ with $XY$ defined, $(XY)^* = Y^* X^*$, by the [[transpose of a product|09GK5PS824]] and complex conjugation of every entry.
4. If $U$ and $V$ are unitary, then $(UV)^*(UV) = V^* U^* U V = V^* V = I_n$, so $UV$ is unitary.
5. If $U$ is unitary, then $U^* U = I_n$, and the [[one-sided inverse theorem|0753Y2X5K6]] gives $U U^* = I_n$; since $(U^*)^* = U$, this says that $U^*$ is unitary.

Clearing one column.

6. We claim that for each $a \in \C^n$ there are a unitary $H$ and a number $\alpha \in \C$ with $Ha = \alpha e_1$, and for $a = 0$ we take $H = I_n$ and $\alpha = 0$.
7. For $a \ne 0$, the unit vector $u = a / \norm{a}$ forms an orthonormal family, and by the [[existence of an orthonormal basis|0Y85GYEGSF]] it extends to an orthonormal basis $u = w_1, w_2, \dots, w_n$ of $\C^n$.
8. The matrix $W$ with columns $w_1, \dots, w_n$ is unitary by step 2, and $W e_1 = w_1$, so $a = \norm{a}\, W e_1$.
9. Put $H = W^*$, which is unitary by step 5, and $\alpha = \norm{a}$; then $Ha = \norm{a}\, W^* W e_1 = \alpha e_1$, which proves the claim.

Existence.

10. For $n = 1$ take $Q = (1)$ and $R = A$, since every $1 \times 1$ matrix is [[upper triangular|0MKABWDRNC]].
11. Let $n \ge 2$, assume existence for size $n - 1$, let $a$ be the first column of $A$, and take $H$ and $\alpha$ as in step 6.
12. The first column of $HA$ is $Ha = \alpha e_1$, so $HA$ has the block form below, with a row $r$ of length $n - 1$ and an $(n - 1) \times (n - 1)$ matrix $A'$:
$$HA = \begin{pmatrix} \alpha & r \\ 0 & A' \end{pmatrix}.$$
13. By the induction hypothesis, $A' = Q' R'$ with $Q'$ unitary and $R'$ upper triangular.
14. The block matrix $G = \begin{pmatrix} 1 & 0 \\ 0 & Q' \end{pmatrix}$ satisfies $G^* G = \begin{pmatrix} 1 & 0 \\ 0 & Q'^* Q' \end{pmatrix} = I_n$, so $G$ is unitary.
15. The matrix $R = \begin{pmatrix} \alpha & r \\ 0 & R' \end{pmatrix}$ is upper triangular because $R'$ is, and block multiplication gives $GR = \begin{pmatrix} \alpha & r \\ 0 & Q'R' \end{pmatrix} = HA$.
16. Multiplying $GR = HA$ on the left by $H^*$ and using $H^* H = I_n$ gives $A = H^* G R$.
17. Put $Q = H^* G$, which is unitary by steps 4 and 5, so $A = QR$, and the induction is complete.
18. For real $A$, repeat steps 6 to 17 in $\R^n$ with $\ip{x}{y} = y^{\mathsf{T}} x$; the orthonormal basis of step 7 exists over $\R$ as well, so every matrix built is real.
19. For real matrices $X^* = X^{\mathsf{T}}$, so a real unitary matrix is an [[orthogonal matrix|0QRBVFJ50X]], and $Q$ is orthogonal and $R$ is real.

Uniqueness.

20. Let $T$ be an invertible upper triangular $n \times n$ matrix; by the [[determinant of a triangular matrix|0K1KKMFHYH]], $\det T = t_{11} \cdots t_{nn}$, and this is nonzero by the [[invertibility criterion|FBSAPTP1PR]], so every $t_{ii} \ne 0$.
21. Fix $j$ and let $x$ be column $j$ of $T^{-1}$, so $Tx = e_j$; for $i > j$, row $i$ of this system reads $\sum_{k \ge i} t_{ik} x_k = 0$.
22. Taking $i = n, n - 1, \dots, j + 1$ in turn, we get $t_{ii} x_i = -\sum_{k > i} t_{ik} x_k = 0$, since the later $x_k$ already vanish, so $x_i = 0$ for all $i > j$.
23. Row $j$ then reads $t_{jj} x_j = 1$, so $T^{-1}$ is upper triangular with diagonal entries $1 / t_{jj}$.
24. If $S$ and $T$ are upper triangular, a term $s_{ik} t_{kj}$ of $(ST)_{ij}$ can be nonzero only for $i \le k \le j$, so $ST$ is upper triangular with diagonal entries $s_{ii} t_{ii}$.
25. Now let $A$ be invertible, and let $A = Q_1 R_1 = Q_2 R_2$ with $Q_1, Q_2$ unitary and $R_1, R_2$ upper triangular with positive diagonal entries.
26. The [[determinant is multiplicative|04CPJ6AF00]], so $0 \ne \det A = \det Q_1 \det R_1$, and $R_1$ is invertible.
27. From $Q_1 R_1 = Q_2 R_2$ we get $Q_2^* Q_1 R_1 = R_2$, so the matrix $T = Q_2^* Q_1$ equals $R_2 R_1^{-1}$.
28. By steps 23 and 24, $T$ is upper triangular with positive diagonal entries, and by steps 4 and 5 it is unitary.
29. Since $T^* T = I_n$, the one-sided inverse theorem gives $T^{-1} = T^*$, which is upper triangular by step 23.
30. But $T^*$ is the conjugate transpose of an upper triangular matrix, so it is also lower triangular, and hence $T^*$ and $T$ are diagonal.
31. The diagonal entries $t_{jj}$ are positive reals with $t_{jj}^2 = (T^* T)_{jj} = 1$, so $t_{jj} = 1$ and $T = I_n$.
32. Then $R_2 = T R_1 = R_1$, and $Q_1 = Q_2 Q_2^* Q_1 = Q_2 T = Q_2$, using $Q_2 Q_2^* = I_n$ from step 5.

So every complex $n \times n$ matrix is $QR$, with real orthogonal factors for real $A$, and the factorization is unique for invertible $A$ when the diagonal of $R$ is positive.

## Idea

A unitary matrix can turn any vector into a multiple of $e_1$, because we can choose an orthonormal basis that starts with the direction of that vector.
Doing this to the first column of $A$ leaves a smaller block in the lower right corner, which we factor by induction.
For uniqueness, two factorizations differ by a matrix that is both unitary and triangular with positive diagonal, and only the identity is both.

## Variants

The [[proof by Gram-Schmidt|KHFJXQDZGC]] builds $Q$ column by column, but it needs independent columns.
In numerical work, the unitary $H$ of step 6 is chosen as a Householder reflection, which sends $a$ to a multiple of $e_1$ by one explicit formula instead of a basis extension.
