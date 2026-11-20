---
tag: T3KXWKC08G
kind: proof
name: Proof that elementary matrices perform row operations and have elementary inverses
msc: ["15A23"]
topics: [P8J6QR66TJ]
audience: ug1
proves: F7F6AA3XQ7
methods: [0NTF6DMVAP, 0WCP0PVET6]
uses: [0M79HRJCRR, 04XWH28452, 032Q9FB8MT, 0TWTS88TWN, 09GK5PS824, 06DW9BAWB1]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_matrix
    locator: Elementary row operations
  - book: isbn:9780135367971
    locator: Section 1.6
---

## Proof

Write $e_k^{\mathsf{T}}$ for row $k$ of $I_m$, and $a_k$ for row $k$ of $A$.

**Part 1.**

1. By the definition of the [[matrix product|032Q9FB8MT]], row $k$ of $EA$ is (row $k$ of $E$) times $A$, which is $\sum_l e_{kl} a_l$.
2. In particular, $e_k^{\mathsf{T}} A = a_k$, and $(u + cv)^{\mathsf{T}} A = u^{\mathsf{T}} A + c\, v^{\mathsf{T}} A$ for row vectors, by linearity of the product.
3. Case $E = P_{ij}$: row $i$ of $E$ is $e_j^{\mathsf{T}}$ and row $j$ is $e_i^{\mathsf{T}}$; the other rows $k$ are $e_k^{\mathsf{T}}$. By steps 1 and 2, rows $i$ and $j$ of $EA$ are $a_j$ and $a_i$, and the other rows are unchanged.
4. Case $E = D_i(c)$: row $i$ of $E$ is $c\, e_i^{\mathsf{T}}$, and the other rows are as in $I_m$. So row $i$ of $EA$ is $c\, a_i$, and the other rows are unchanged.
5. Case $E = T_{ij}(c)$: row $i$ of $E$ is $e_i^{\mathsf{T}} + c\, e_j^{\mathsf{T}}$, and the other rows are as in $I_m$. So row $i$ of $EA$ is $a_i + c\, a_j$, and the other rows are unchanged.
6. In each case $EA = \rho(A)$, by the definition of the three [[row operations|04XWH28452]].

**Part 2.**

7. Each row operation $\rho$ has an inverse operation $\rho'$ of the same type. The operation $\rho'$ exchanges rows $i$ and $j$ again, multiplies row $i$ by $c^{-1}$, or adds $-c$ times row $j$ to row $i$. So $\rho'(\rho(A)) = A$ and $\rho(\rho'(A)) = A$ for each $A$.
8. Let $E' = \rho'(I_m)$, which is the elementary matrix $P_{ij}$, $D_i(c^{-1})$ or $T_{ij}(-c)$.
9. By part 1 applied to $E'$ and the matrix $E$, we get $E'E = \rho'(E) = \rho'(\rho(I_m)) = I_m$, by step 7.
10. By part 1 applied to $E$ and the matrix $E'$, we get $EE' = \rho(E') = \rho(\rho'(I_m)) = I_m$, by step 7.
11. By steps 9 and 10 and the [[definition of the inverse|0TWTS88TWN]], $E$ is invertible with $E^{-1} = E'$.

**Part 3.**

12. The [[transpose of a product|09GK5PS824]] gives $AE = (E^{\mathsf{T}} A^{\mathsf{T}})^{\mathsf{T}}$.
13. From the definition, $P_{ij}^{\mathsf{T}} = P_{ij}$, $D_i(c)^{\mathsf{T}} = D_i(c)$ and $T_{ij}(c)^{\mathsf{T}} = (I_m + cE_{ij})^{\mathsf{T}} = I_m + cE_{ji} = T_{ji}(c)$.
14. By part 1, $T_{ji}(c) A^{\mathsf{T}}$ adds $c$ times row $i$ of $A^{\mathsf{T}}$ to row $j$. Row $k$ of $A^{\mathsf{T}}$ is column $k$ of $A$, so after the transpose, $AT_{ij}(c)$ is $A$ with $c$ times column $i$ added to column $j$.
15. In the same way, $AP_{ij}$ exchanges columns $i$ and $j$, and $AD_i(c)$ multiplies column $i$ by $c$.

## Idea

Row $k$ of $EA$ is the combination of the rows of $A$ given by row $k$ of $E$.
For an elementary $E$, each row of $E$ picks one or two rows of $A$, exactly as the row operation does.
The inverse operation gives the inverse matrix, by part 1 applied twice.

## Variants

Part 3 can also be proved directly from the column view of the product: column $k$ of $AE$ is $A$ times column $k$ of $E$.
