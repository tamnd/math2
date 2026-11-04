---
tag: ZRPHF64HFG
kind: proof
name: Proof of the QR decomposition by clearing the first column
msc: [15A23, 65F25]
proves: 0ERWG4NXQ9
uses: [0D6RMJ10M9, 0QRBVFJ50X, 0MKABWDRNC, 0EX045E2BP, 0VGSYBWHV2, 09VYHEF2VT, 0Y85GYEGSF, 0753Y2X5K6, 09GK5PS824, 04CPJ6AF00, 0K1KKMFHYH, FBSAPTP1PR]
sources:
  - url: https://linear.pugetsound.edu/scla/html/section-QR.html
---

## Proof

We prove existence by induction on $n$, and uniqueness by comparing two factorisations.

1. For $x, y \in \C^n$ let $\ip{x}{y} = y^* x = \sum_i x_i \overline{y_i}$, where $^*$ is the [[conjugate transpose|0EX045E2BP]]. This is an [[inner product|0VGSYBWHV2]], since it is linear in $x$, $\ip{y}{x} = \overline{\ip{x}{y}}$, and $\ip{x}{x} = \sum_i \abs{x_i}^2 > 0$ for $x \ne 0$.
2. Let $W$ be an $n \times n$ complex matrix with columns $w_1, \dots, w_n$. The $(i, j)$ entry of $W^* W$ is $w_i^* w_j = \ip{w_j}{w_i}$. So $W$ is [[unitary|0D6RMJ10M9]] if and only if its columns form an [[orthonormal family|09VYHEF2VT]].
3. For complex matrices $X$ and $Y$ with $XY$ defined, $(XY)^* = Y^* X^*$. This follows from the [[transpose of a product|09GK5PS824]] by taking complex conjugates of all entries.
4. Let $U$ and $V$ be unitary $n \times n$ matrices. Then $(UV)^*(UV) = V^* U^* U V = V^* V = I_n$, so $UV$ is unitary.
5. Since $U^* U = I_n$, the [[one-sided inverse theorem|0753Y2X5K6]] gives $U U^* = I_n$. As $(U^*)^* = U$, this says that $U^*$ is unitary.
6. Claim: for each $a \in \C^n$ there are a unitary $H$ and a number $\alpha \in \C$ with $Ha = \alpha e_1$, where $e_1$ is the first standard basis vector. If $a = 0$, take $H = I_n$ and $\alpha = 0$.
7. If $a \ne 0$, let $\norm{a} = \sqrt{\ip{a}{a}}$ and $u = a / \norm{a}$. The family $(u)$ is orthonormal. By the [[existence of an orthonormal basis|0Y85GYEGSF]], it extends to an orthonormal basis $u = w_1, w_2, \dots, w_n$ of $\C^n$.
8. Let $W$ be the matrix with columns $w_1, \dots, w_n$. By step 2, $W$ is unitary. Also $W e_1 = w_1$, so $a = \norm{a}\, W e_1$.
9. Put $H = W^*$, which is unitary by step 5, and $\alpha = \norm{a}$. Then $Ha = \norm{a}\, W^* W e_1 = \alpha e_1$. This proves the claim.
10. Existence for $n = 1$: take $Q = (1)$ and $R = A$. Every $1 \times 1$ matrix is [[upper triangular|0MKABWDRNC]].
11. Let $n \ge 2$ and assume existence for size $n - 1$. Let $a$ be the first column of $A$, and take $H$ and $\alpha$ as in step 6.
12. The first column of $HA$ is $Ha = \alpha e_1$. So $HA = \begin{pmatrix} \alpha & r \\ 0 & A' \end{pmatrix}$, with a row $r$ of length $n - 1$ and an $(n-1) \times (n-1)$ matrix $A'$.
13. By the induction hypothesis, $A' = Q' R'$ with $Q'$ unitary and $R'$ upper triangular.
14. Let $G = \begin{pmatrix} 1 & 0 \\ 0 & Q' \end{pmatrix}$. Then $G^* G = \begin{pmatrix} 1 & 0 \\ 0 & Q'^* Q' \end{pmatrix} = I_n$, so $G$ is unitary.
15. Let $R = \begin{pmatrix} \alpha & r \\ 0 & R' \end{pmatrix}$. It is upper triangular because $R'$ is. Block multiplication gives $GR = \begin{pmatrix} \alpha & r \\ 0 & Q'R' \end{pmatrix} = HA$.
16. Multiply step 15 on the left by $H^*$. Since $H^* H = I_n$, we get $A = H^* G R$.
17. Put $Q = H^* G$. It is unitary by steps 4 and 5. So $A = QR$, which completes the induction.
18. Real case: let $A$ be real. Repeat steps 6 to 17 in $\R^n$ with the inner product $\ip{x}{y} = y^T x$. The existence theorem of step 7 also holds over $\R$, so $W$ is real.
19. For real matrices, $X^* = X^T$, so a real unitary matrix is an [[orthogonal matrix|0QRBVFJ50X]]. All matrices built in steps 6 to 17 are then real, so $Q$ is orthogonal and $R$ is real.
20. Uniqueness, first a lemma. Let $T$ be an invertible upper triangular $n \times n$ matrix with entries $t_{ij}$. By the [[determinant of a triangular matrix|0K1KKMFHYH]], $\det T = t_{11} \cdots t_{nn}$.
21. By the [[invertibility criterion|FBSAPTP1PR]], $\det T \ne 0$. So $t_{ii} \ne 0$ for all $i$.
22. Fix $j$ and let $x$ be column $j$ of $T^{-1}$, so $Tx = e_j$. For $i > j$, row $i$ of this system reads $\sum_{k \ge i} t_{ik} x_k = 0$.
23. For $i = n, n-1, \dots, j+1$ in turn, this gives $t_{ii} x_i = -\sum_{k > i} t_{ik} x_k = 0$, since the later $x_k$ already vanish. So $x_i = 0$ for all $i > j$.
24. Row $j$ then reads $t_{jj} x_j = 1$. So $T^{-1}$ is upper triangular, with diagonal entries $1/t_{jj}$.
25. If $S$ and $T$ are upper triangular, then $(ST)_{ij} = \sum_k s_{ik} t_{kj}$, and a term is nonzero only if $i \le k \le j$. So $ST$ is upper triangular with diagonal entries $s_{ii} t_{ii}$.
26. Now let $A$ be invertible, and let $A = Q_1 R_1 = Q_2 R_2$ with $Q_1, Q_2$ unitary and $R_1, R_2$ upper triangular with positive diagonal entries.
27. Since the [[determinant is multiplicative|04CPJ6AF00]], $0 \ne \det A = \det Q_1 \det R_1$. So $\det R_1 \ne 0$, and $R_1$ is invertible.
28. From $Q_1 R_1 = Q_2 R_2$ we get $Q_2^* Q_1 R_1 = R_2$, so $T = Q_2^* Q_1$ equals $R_2 R_1^{-1}$.
29. By steps 24 and 25, $T$ is upper triangular with positive diagonal entries. By steps 4 and 5, $T$ is unitary.
30. Since $T^* T = I_n$, the one-sided inverse theorem gives $T^{-1} = T^*$. By step 24, $T^*$ is upper triangular.
31. But $T^*$ is the conjugate transpose of an upper triangular matrix, so it is lower triangular. Hence $T^*$ is diagonal, and so is $T$.
32. The diagonal entries $t_{jj}$ are positive reals with $t_{jj}^2 = (T^* T)_{jj} = 1$. So $t_{jj} = 1$ and $T = I_n$.
33. Then $R_2 = T R_1 = R_1$. Also $Q_2^* Q_1 = I_n$, so $Q_1 = Q_2 Q_2^* Q_1 = Q_2$, using $Q_2 Q_2^* = I_n$ from step 5.
34. So every complex $n \times n$ matrix is $QR$, with real orthogonal factors for real $A$. The factorisation is unique for invertible $A$ with positive diagonal in $R$.

## Idea

A unitary matrix can turn any vector into a multiple of $e_1$. Doing this to the first column of $A$ leaves a smaller block, which we factor by induction. For uniqueness, two factorisations differ by a matrix that is both unitary and triangular with positive diagonal, and only the identity is both.
