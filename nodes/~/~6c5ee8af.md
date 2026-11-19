---
tag: ~6c5ee8af
kind: proof
name: Proof that elementary row operations are reversible and keep the solution set
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
proves: ~6410ee51
uses: [0DE5R5EB4D, 0JTRMBQ1SA, 01REXW3WWE, 032Q9FB8MT]
methods: [0NTF6DMVAP, 0WCP0PVET6, MKHVRNW68H]
sources:
  - book: isbn:9780135367971
    locator: Chapter 1
  - url: https://en.wikipedia.org/wiki/Elementary_matrix
    locator: Elementary row operations
---

## Proof

Write $R_1, \dots, R_m$ for the rows of $M$.

Part 1, reversibility, by cases on the type of $\rho$.

1. If $\rho$ swaps $R_i$ and $R_j$, take $\rho' = \rho$. Swapping twice gives the original order.
2. If $\rho$ replaces $R_i$ by $cR_i$ with $c \ne 0$, take $\rho'$ to replace $R_i$ by $c^{-1} R_i$. This exists because $F$ is a field.
3. Then $c^{-1}(cR_i) = R_i$, and the other rows do not change.
4. If $\rho$ replaces $R_i$ by $R_i + cR_j$ with $i \ne j$, take $\rho'$ to replace $R_i$ by $R_i - cR_j$.
5. Since $i \ne j$, the row $R_j$ is the same after $\rho$. So $\rho'$ gives $(R_i + cR_j) - cR_j = R_i$.

Part 2, matrix form.

6. By [[matrix multiplication|032Q9FB8MT]], row $i$ of $EM$ is $\sum_{l} e_{il} R_l$, where $(e_{i1}, \dots, e_{im})$ is row $i$ of $E$.
7. Row $i$ of $E = \rho(I_m)$ is obtained from the rows $e_1^T, \dots, e_m^T$ of $I_m$ by the same rule that $\rho$ applies to rows.
8. For a swap, row $i$ of $E$ is $e_j^T$, so row $i$ of $EM$ is $R_j$. This is row $i$ of $\rho(M)$.
9. For scaling, row $i$ of $E$ is $c e_i^T$, so row $i$ of $EM$ is $cR_i$. This is row $i$ of $\rho(M)$.
10. For row addition, row $i$ of $E$ is $e_i^T + c e_j^T$, so row $i$ of $EM$ is $R_i + cR_j$.
11. In each case the other rows of $E$ are the rows $e_l^T$ of $I_m$, so the other rows of $EM$ are the rows $R_l$.
12. So $EM = \rho(M)$ for every $M$.
13. Put $E' = \rho'(I_m)$. By step 12 and part 1, $E'E = E'\rho(I_m) = \rho'(\rho(I_m)) = I_m$.
14. In the same way $EE' = \rho(\rho'(I_m)) = I_m$, since $\rho$ undoes $\rho'$ by the same case analysis.
15. So $E$ is invertible with inverse $E'$. Such a matrix is an [[elementary matrix|01REXW3WWE]].

Part 3, solution sets, by double inclusion.

16. Let $s \in F^n$ with $As = b$. By part 2 with $M = [A \mid b]$, we have $A' = EA$ and $b' = Eb$.
17. Then $A's = E(As) = Eb = b'$. So every solution of $Ax = b$ solves $A'x = b'$.
18. Conversely, let $A's = b'$. By part 1, $[A \mid b] = \rho'([A' \mid b'])$.
19. Step 17 applied to $\rho'$ shows that $s$ solves $Ax = b$.
20. So the two solution sets are equal. This proves the theorem.

## Idea

Each operation can be undone by an operation of the same type, which needs inverses of nonzero scalars.
Each operation is multiplication on the left by a fixed invertible matrix.
A solution of the old system solves every combination of its equations, so it solves the new system; the inverse operation gives the converse.

## Variants

Part 3 can be proved without matrices.
Each new equation is a linear combination of the old equations, so old solutions solve the new system.
The old equations are combinations of the new ones, by the inverse operation, so the converse holds too.
