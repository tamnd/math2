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
Let $a_1, \dots, a_n \in \mathbb{K}^m$ be the columns of $A$, which are [[linearly independent|0EVHJFTG9Z]], and let $\ip{x}{y} = y^* x$.

Part 1, existence.

1. Define vectors by the [[Gram-Schmidt process|0VT6P0GNQR]]: for $j = 1, \dots, n$, set $v_j = a_j - \sum_{i < j} \ip{a_j}{q_i} q_i$ and $q_j = v_j / \norm{v_j}$.
2. Claim, for $j = 1, \dots, n$: $v_j \ne 0$, the vectors $q_1, \dots, q_j$ are orthonormal, and $\operatorname{span}(q_1, \dots, q_j) = \operatorname{span}(a_1, \dots, a_j)$. We prove it by induction on $j$, and for $j = 1$ the empty sum gives $v_1 = a_1$.
3. $v_j \ne 0$: if $v_j = 0$, then $a_j = \sum_{i < j} \ip{a_j}{q_i} q_i$ lies in $\operatorname{span}(q_1, \dots, q_{j-1})$, which is $\operatorname{span}(a_1, \dots, a_{j-1})$ by the claim for $j - 1$. This contradicts the independence of the columns. For $j = 1$, $a_1 \ne 0$ because an independent family has no zero vector.
4. Orthogonality: for $k < j$, linearity in the first argument and the orthonormality of $q_1, \dots, q_{j-1}$ give $\ip{v_j}{q_k} = \ip{a_j}{q_k} - \ip{a_j}{q_k} \cdot 1 = 0$. So $q_j$ is orthogonal to $q_1, \dots, q_{j-1}$, and $\norm{q_j} = 1$ by its definition.
5. Spans: $q_j$ is a combination of $a_j$ and $q_1, \dots, q_{j-1}$, so it lies in $\operatorname{span}(a_1, \dots, a_j)$. Conversely, step 1 gives $a_j = \norm{v_j} q_j + \sum_{i < j} \ip{a_j}{q_i} q_i$, so $a_j \in \operatorname{span}(q_1, \dots, q_j)$. This proves the claim for $j$, by the definition of the [[span|0DTY8B9HMS]].
6. Define $r_{ij} = \ip{a_j}{q_i}$ for all $i, j$. For $i > j$, $a_j$ lies in $\operatorname{span}(q_1, \dots, q_j)$, which is orthogonal to $q_i$; so $r_{ij} = 0$, and $R = (r_{ij})$ is [[upper triangular|0MKABWDRNC]].
7. For $i = j$: $\ip{a_j}{q_j} = \ip{\norm{v_j} q_j + \sum_{k < j} r_{kj} q_k}{q_j} = \norm{v_j}$, by step 5 and orthonormality. So $r_{jj} = \norm{v_j}$ is real and positive by step 3.
8. Column $j$ of $QR$ is $\sum_i r_{ij} q_i = \sum_{i < j} r_{ij} q_i + \norm{v_j} q_j$, by the [[matrix-vector product|0PDVQEP0ZC]] and steps 6 and 7. By step 5, this is $a_j$. So $A = QR$.
9. Entry $(i, j)$ of $Q^* Q$ is $q_i^* q_j = \ip{q_j}{q_i}$, which is $1$ for $i = j$ and $0$ otherwise. So $Q^* Q = I_n$. This proves part 1.

Part 2, uniqueness.

10. Two facts on upper triangular $n \times n$ matrices. A product $ST$ is upper triangular, because $(ST)_{ij} = \sum_k s_{ik} t_{kj}$ and a term can be nonzero only for $i \le k \le j$; its diagonal entries are $s_{ii} t_{ii}$. If all $t_{ii} \ne 0$, then $T$ is invertible, and back substitution in $T x = e_j$ gives $x_i = 0$ for $i > j$, so $T^{-1}$ is upper triangular with diagonal entries $1 / t_{ii}$.
11. Let $A = Q_1 R_1 = Q_2 R_2$ be two factorizations as in part 1. Then $A^* A = R_1^* Q_1^* Q_1 R_1 = R_1^* R_1$, and in the same way $A^* A = R_2^* R_2$.
12. $R_1$ and $R_2$ have positive diagonals, so by step 10 they are [[invertible|0EB9N0S33C]] with upper triangular inverses. From $R_1^* R_1 = R_2^* R_2$ we get $(R_2^*)^{-1} R_1^* = R_2 R_1^{-1}$.
13. The right side is upper triangular by step 10. The left side is the conjugate transpose of $R_1 R_2^{-1}$, which is upper triangular, so the left side is lower triangular. Hence $D = R_2 R_1^{-1}$ is diagonal.
14. By step 10, the diagonal entries of $D$ are $d_j = r^{(2)}_{jj} / r^{(1)}_{jj} > 0$. So $D$ is real, $D^* = D$, and $R_2 = D R_1$.
15. Then $R_1^* R_1 = R_2^* R_2 = R_1^* D^2 R_1$. Multiplying by $(R_1^*)^{-1}$ on the left and $R_1^{-1}$ on the right gives $D^2 = I$, so $d_j^2 = 1$ and $d_j = 1$.
16. Hence $R_2 = R_1$, and $Q_2 = A R_2^{-1} = A R_1^{-1} = Q_1$. This proves part 2.

Part 3, least squares.

17. By the [[normal equations|4D7MRG4D91]] over $\mathbb{K}$, the least-squares solutions of $Ax = b$ are the solutions of $A^* A x = A^* b$, and there is exactly one because the columns are independent.
18. By step 11, $A^* A = R^* R$, and $A^* b = R^* Q^* b$. So the normal equations read $R^* R x = R^* Q^* b$.
19. $R^*$ is invertible, by step 12. Multiplying by $(R^*)^{-1}$ shows that the normal equations are equivalent to $R x = Q^* b$. This proves part 3.

## Idea

Gram-Schmidt turns the columns of $A$ into orthonormal vectors, one at a time, and each $a_j$ is a combination of $q_1, \dots, q_j$ only; the coefficients form the triangular matrix $R$.
Uniqueness holds because two such factorizations differ by a matrix that is both upper and lower triangular with positive diagonal and squares to $I$.
For least squares, $Q^* Q = I$ makes the normal equations collapse to a triangular system.

## Variants

The [[proof by clearing the first column|ZRPHF64HFG]] uses unitary matrices instead of Gram-Schmidt, and it gives the square case without independence.
In computation, modified Gram-Schmidt, Householder reflections or Givens rotations replace step 1, because classical Gram-Schmidt loses orthogonality in floating point.
