---
tag: KHFJXQDZGC
kind: proof
name: Proof of the thin QR decomposition by Gram-Schmidt
msc: [15A23, 65F25]
topics: [8GQVME4SZZ]
audience: ug1
proves: 0ERWG4NXQ9
uses: [0VT6P0GNQR, 0EVHJFTG9Z, 0MKABWDRNC, 0EX045E2BP, 0DTY8B9HMS, 4D7MRG4D91, 0EB9N0S33C, 0PDVQEP0ZC]
methods: [0ASJVEFA9J, X5HG1RNWQX, 0NTF6DMVAP]
sources:
  - book: isbn:9780321982384
    locator: Section 6.4
  - url: https://en.wikipedia.org/wiki/QR_decomposition
    locator: Using the Gram–Schmidt process
---

## Proof

This proof covers parts 1, 2 and 3 of the statement.
We build $Q$ by Gram-Schmidt and read off $R$, then compare two factorizations through $A^* A$, and finally rewrite the normal equations.
Let $a_1, \dots, a_n \in \mathbb{K}^m$ be the columns of $A$, which are [[linearly independent|0EVHJFTG9Z]], and let $\ip{x}{y} = y^* x$.

Part 1, existence.

1. Define vectors by the [[Gram-Schmidt process|0VT6P0GNQR]]: for $j = 1, \dots, n$, set
$$v_j = a_j - \sum_{i < j} \ip{a_j}{q_i} q_i, \qquad q_j = \frac{v_j}{\norm{v_j}}.$$
2. We prove by induction on $j$ the claim that $v_j \ne 0$, that $q_1, \dots, q_j$ are orthonormal, and that $\operatorname{span}(q_1, \dots, q_j) = \operatorname{span}(a_1, \dots, a_j)$.
3. For $j = 1$ the sum is empty, so $v_1 = a_1$, and $a_1 \ne 0$ because an independent family contains no zero vector.
4. For $j > 1$, suppose $v_j = 0$; then $a_j = \sum_{i < j} \ip{a_j}{q_i} q_i$ lies in $\operatorname{span}(q_1, \dots, q_{j-1})$, which is $\operatorname{span}(a_1, \dots, a_{j-1})$ by the claim for $j - 1$.
5. That contradicts the independence of the columns, so $v_j \ne 0$ and $q_j$ is defined, with $\norm{q_j} = 1$.
6. For $k < j$, linearity in the first argument and the orthonormality of $q_1, \dots, q_{j-1}$ give $\ip{v_j}{q_k} = \ip{a_j}{q_k} - \ip{a_j}{q_k} \cdot 1 = 0$, so $q_j$ is orthogonal to $q_1, \dots, q_{j-1}$.
7. The vector $q_j$ is a combination of $a_j$ and $q_1, \dots, q_{j-1}$, so it lies in $\operatorname{span}(a_1, \dots, a_j)$ by the claim for $j - 1$.
8. Conversely, step 1 gives $a_j = \norm{v_j} q_j + \sum_{i < j} \ip{a_j}{q_i} q_i$, so $a_j$ lies in $\operatorname{span}(q_1, \dots, q_j)$, and the two [[spans|0DTY8B9HMS]] agree; this proves the claim for $j$.
9. Define $r_{ij} = \ip{a_j}{q_i}$ for all $i, j$.
10. For $i > j$, the vector $a_j$ lies in $\operatorname{span}(q_1, \dots, q_j)$, which is orthogonal to $q_i$, so $r_{ij} = 0$ and $R = (r_{ij})$ is [[upper triangular|0MKABWDRNC]].
11. For $i = j$, step 8 and orthonormality give $r_{jj} = \ip{a_j}{q_j} = \norm{v_j}$, which is real and positive by step 5.
12. By the [[matrix-vector product|0PDVQEP0ZC]] and steps 10 and 11, column $j$ of $QR$ is $\sum_{i < j} r_{ij} q_i + \norm{v_j} q_j$, which is $a_j$ by step 8, so $A = QR$.
13. Entry $(i, j)$ of $Q^* Q$ is $q_i^* q_j = \ip{q_j}{q_i}$, which is $1$ for $i = j$ and $0$ otherwise, so $Q^* Q = I_n$, and part 1 is proved.

Part 2, uniqueness.

14. We use two facts on upper triangular $n \times n$ matrices. A product $ST$ is upper triangular with diagonal entries $s_{ii} t_{ii}$, because a term $s_{ik} t_{kj}$ can be nonzero only for $i \le k \le j$. If all $t_{ii} \ne 0$, back substitution in $Tx = e_j$ gives $x_i = 0$ for $i > j$, so $T$ is invertible and $T^{-1}$ is upper triangular with diagonal entries $1 / t_{ii}$.
15. Let $A = Q_1 R_1 = Q_2 R_2$ be two factorizations as in part 1; then $A^* A = R_1^* Q_1^* Q_1 R_1 = R_1^* R_1$, and in the same way $A^* A = R_2^* R_2$.
16. The diagonals of $R_1$ and $R_2$ are positive, so by step 14 both are [[invertible|0EB9N0S33C]] with upper triangular inverses.
17. From $R_1^* R_1 = R_2^* R_2$ we get $(R_2^*)^{-1} R_1^* = R_2 R_1^{-1}$.
18. The right side is upper triangular by step 14, and the left side is the conjugate transpose of the upper triangular matrix $R_1 R_2^{-1}$, so it is lower triangular.
19. Hence $D = R_2 R_1^{-1}$ is diagonal, with entries $d_j = r^{(2)}_{jj} / r^{(1)}_{jj} > 0$ by step 14, so $D$ is real, $D^* = D$ and $R_2 = D R_1$.
20. Then $R_1^* R_1 = R_2^* R_2 = R_1^* D^2 R_1$, and multiplying by $(R_1^*)^{-1}$ on the left and by $R_1^{-1}$ on the right gives $D^2 = I$.
21. So $d_j^2 = 1$ with $d_j > 0$, which forces $d_j = 1$ and $R_2 = R_1$.
22. Finally $Q_2 = A R_2^{-1} = A R_1^{-1} = Q_1$, and part 2 is proved.

Part 3, least squares.

23. By the [[normal equations|4D7MRG4D91]] over $\mathbb{K}$, the least-squares solutions of $Ax = b$ are the solutions of $A^* A x = A^* b$, and there is exactly one because the columns are independent.
24. By step 15, $A^* A = R^* R$, and $A^* b = R^* Q^* b$, so the normal equations read $R^* R x = R^* Q^* b$.
25. The matrix $R^*$ is invertible by step 16, so multiplying by $(R^*)^{-1}$ shows that the normal equations are equivalent to $R x = Q^* b$, and part 3 is proved.

## Idea

Gram-Schmidt turns the columns of $A$ into orthonormal vectors one at a time, and each $a_j$ is a combination of $q_1, \dots, q_j$ only.
The coefficients of these combinations are the entries of the triangular matrix $R$.
Uniqueness holds because two such factorizations differ by a matrix that is both upper and lower triangular, has a positive diagonal and squares to $I$, and only the identity does all three.
For least squares, the identity $Q^* Q = I$ makes the normal equations collapse to a triangular system.

## Variants

The [[proof by clearing the first column|ZRPHF64HFG]] uses unitary matrices instead of Gram-Schmidt, and it gives the square case without any independence.
In computation, modified Gram-Schmidt, Householder reflections or Givens rotations replace step 1, because classical Gram-Schmidt loses orthogonality in floating point.
