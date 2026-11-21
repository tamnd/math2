---
tag: G4STVMM9XP
kind: proof
name: Proof that elementary row operations are reversible and keep the solution set
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
proves: K41GT10YM6
uses: [0DE5R5EB4D, 0JTRMBQ1SA, 01REXW3WWE, 032Q9FB8MT]
methods: [0NTF6DMVAP, 0WCP0PVET6, MKHVRNW68H]
sources:
  - book: isbn:9780135367971
    locator: Chapter 1
  - url: https://en.wikipedia.org/wiki/Elementary_matrix
    locator: Elementary row operations
---

## Proof

We check each of the three types for reversibility, then compute $EM$ row by row, and finally compare the two solution sets by double inclusion.
Write $R_1, \dots, R_m$ for the rows of $M$.

Part 1, reversibility, by cases on the type of $\rho$.

1. If $\rho$ swaps $R_i$ and $R_j$, take $\rho' = \rho$. Swapping twice gives the original order.
2. If $\rho$ replaces $R_i$ by $cR_i$ with $c \ne 0$, take $\rho'$ to replace $R_i$ by $c^{-1} R_i$. This inverse exists because $F$ is a field, and $c^{-1}(cR_i) = R_i$, while the other rows do not change.
3. If $\rho$ replaces $R_i$ by $R_i + cR_j$ with $i \ne j$, take $\rho'$ to replace $R_i$ by $R_i - cR_j$. Since $i \ne j$, the row $R_j$ is the same after $\rho$, so $\rho'$ gives $(R_i + cR_j) - cR_j = R_i$.

Part 2, matrix form.

4. By [[matrix multiplication|032Q9FB8MT]], row $i$ of $EM$ is $\sum_{l} e_{il} R_l$, where $(e_{i1}, \dots, e_{im})$ is row $i$ of $E$.
5. The rows of $E = \rho(I_m)$ come from the rows $e_1^{\mathsf{T}}, \dots, e_m^{\mathsf{T}}$ of $I_m$ by the rule that $\rho$ applies to rows.
6. For a swap, row $i$ of $E$ is $e_j^{\mathsf{T}}$ and row $j$ is $e_i^{\mathsf{T}}$, so rows $i$ and $j$ of $EM$ are $R_j$ and $R_i$.
7. For a scaling, row $i$ of $E$ is $c e_i^{\mathsf{T}}$, so row $i$ of $EM$ is $cR_i$.
8. For a row addition, row $i$ of $E$ is $e_i^{\mathsf{T}} + c e_j^{\mathsf{T}}$, so row $i$ of $EM$ is $R_i + cR_j$.
9. In each case the other rows of $E$ are rows $e_l^{\mathsf{T}}$ of $I_m$, so the other rows of $EM$ are the rows $R_l$. Hence $EM = \rho(M)$ for every $M$.
10. Put $E' = \rho'(I_m)$. By step 9 and part 1, $E'E = \rho'(E) = \rho'(\rho(I_m)) = I_m$.
11. In the same way $EE' = \rho(\rho'(I_m)) = I_m$, since by the cases of part 1 the operation $\rho$ also undoes $\rho'$.
12. So $E$ is invertible with inverse $E'$. Such a matrix is an [[elementary matrix|01REXW3WWE]].

Part 3, solution sets, by double inclusion.

13. Let $s \in F^n$ with $As = b$. By part 2 with $M = [A \mid b]$, we have $A' = EA$ and $b' = Eb$.
14. Then $A's = E(As) = Eb = b'$. So every solution of $Ax = b$ solves $A'x = b'$.
15. Conversely, by part 1, $[A \mid b] = \rho'([A' \mid b'])$. Step 14 applied to $\rho'$ shows that every solution of $A'x = b'$ solves $Ax = b$.
16. So the two solution sets are equal. This proves the theorem.

## Idea

Each operation can be undone by an operation of the same type, and for scaling this needs the inverse of a nonzero scalar.
Each operation is multiplication on the left by a fixed invertible matrix.
A solution of the old system solves every combination of its equations, so it solves the new system.
The inverse operation gives the converse.

## Variants

Part 3 can be proved without matrices.
Each new equation is a linear combination of the old equations, so old solutions solve the new system.
The old equations are combinations of the new ones, by the inverse operation, so the converse holds too.
