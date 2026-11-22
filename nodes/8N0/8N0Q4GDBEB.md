---
tag: 8N0Q4GDBEB
kind: proof
name: Proof of the uniqueness of the LU and LDU decompositions
msc: ["15A23"]
topics: [P8J6QR66TJ]
audience: ug2
proves: R424G32KFA
methods: [GQHHNV79PA, 0NTF6DMVAP]
uses: [7X1B65CTG4, 0S4WTRE9GG, 09GK5PS824, 0Q9PGXD9E4, 00J3KZP8Y0, 0N4XY7Z3NN]
sources:
  - url: https://en.wikipedia.org/wiki/LU_decomposition
    locator: LDU decomposition
---

## Proof

We compare two factorizations through the matrix $L_2^{-1} L_1 = U_2 U_1^{-1}$, which is both unit lower triangular and upper triangular and so must be $I_n$; the other parts follow by applying this to $L \cdot (DV)$ and to the transpose.

We use one fact (T) several times.
If $X$ and $Y$ are upper triangular, then $XY$ is upper triangular with diagonal entries $x_{ii} y_{ii}$.
The reason is that entry $(i, j)$ is $\sum_l x_{il} y_{lj}$, and a term is nonzero only if $i \le l \le j$.
The same holds for lower triangular matrices.

**Part 1.**

1. $L_1$ and $L_2$ have diagonal entries $1$, so they are invertible by the theorem on [[triangular matrices|7X1B65CTG4]].
2. $U_i = L_i^{-1} A$ is invertible, as a [[product of invertible matrices|0S4WTRE9GG]]. By the theorem on triangular matrices, its diagonal entries are nonzero, and $U_i^{-1}$ is upper triangular.
3. From $L_1 U_1 = L_2 U_2$ we get $L_2^{-1} L_1 = U_2 U_1^{-1}$, by multiplying on the left by $L_2^{-1}$ and on the right by $U_1^{-1}$.
4. The left side is unit lower triangular, by part 4 of the theorem on triangular matrices. The right side is upper triangular, by the same part.
5. A matrix that is both lower and upper triangular is [[diagonal|0Q9PGXD9E4]]. By step 4 its diagonal entries are those of $L_2^{-1} L_1$, which are $1$. So $L_2^{-1} L_1 = U_2 U_1^{-1} = I_n$.
6. So $L_1 = L_2$ and $U_1 = U_2$.

**Part 2.**

7. By step 2, $D = \operatorname{diag}(u_{11}, \dots, u_{nn})$ has nonzero diagonal entries, so it is invertible with $D^{-1} = \operatorname{diag}(u_{11}^{-1}, \dots, u_{nn}^{-1})$.
8. $V = D^{-1} U$ is $U$ with row $i$ divided by $u_{ii}$. By fact (T), $V$ is upper triangular with diagonal entries $u_{ii}^{-1} u_{ii} = 1$.
9. $L D V = L D D^{-1} U = L U = A$.

**Part 3.**

10. Let $A = L_1 D_1 V_1 = L_2 D_2 V_2$ be two such factorizations. Since $A$ is invertible, $D_1$ and $D_2$ are invertible, as in step 2.
11. By fact (T), $D_i V_i$ is upper triangular with diagonal entries those of $D_i$.
12. By part 1 applied to $A = L_1 (D_1 V_1) = L_2 (D_2 V_2)$, we get $L_1 = L_2$ and $D_1 V_1 = D_2 V_2$.
13. By step 11, the diagonals give $D_1 = D_2$. Multiplying on the left by $D_1^{-1}$ gives $V_1 = V_2$.

**Part 4.**

14. Let $A = A^{\mathsf{T}}$ and $A = LDV$ as in part 2. By the [[transpose of a product|09GK5PS824]], $A = A^{\mathsf{T}} = V^{\mathsf{T}} D^{\mathsf{T}} L^{\mathsf{T}} = V^{\mathsf{T}} D L^{\mathsf{T}}$.
15. $V^{\mathsf{T}}$ is unit lower triangular, $D$ is diagonal, and $L^{\mathsf{T}}$ is unit upper triangular.
16. By part 3, $V^{\mathsf{T}} = L$, so $V = L^{\mathsf{T}}$.

## Idea

Put the lower triangular factors on one side of the equation and the upper triangular factors on the other.
The two sides are then a matrix that is unit lower triangular and also upper triangular, and only the identity matrix has both forms.
Invertibility is used once, to invert $U_1$; this is why the zero matrix, with its many factorizations, is not a counterexample.
The LDU form and its symmetric case follow by applying the same fact to $L \cdot (DV)$ and to the transpose.

## Variants

One can also prove part 1 by solving $A = LU$ for the unknown entries.
Taken row by row, each new equation contains one new unknown entry of $L$ or $U$, and the entries of $L$ are found by dividing by a pivot $u_{kk}$.
The pivots are nonzero because $A$ is invertible, so each equation has exactly one solution.
