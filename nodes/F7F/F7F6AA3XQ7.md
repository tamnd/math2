---
tag: F7F6AA3XQ7
kind: statement
role: theorem
name: Elementary matrices perform row operations and have elementary inverses
msc: ["15A23"]
topics: [P8J6QR66TJ]
audience: ug1
about: [01REXW3WWE]
uses: [0M79HRJCRR, 04XWH28452, 032Q9FB8MT, 0TWTS88TWN]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_matrix
    locator: Elementary row operations
  - book: isbn:9780321982384
    locator: Section 2.2
  - book: isbn:9780135367971
    locator: Section 1.6
---

## Statement

Let $F$ be a field and let $E$ be an $m \times m$ [[elementary matrix|0M79HRJCRR]] over $F$, obtained from $I_m$ by the [[elementary row operation|04XWH28452]] $\rho$.

1. For each $m \times p$ matrix $A$ over $F$, the [[product|032Q9FB8MT]] $EA$ is the matrix $\rho(A)$ obtained from $A$ by the operation $\rho$.
2. $E$ is [[invertible|0TWTS88TWN]], and $E^{-1}$ is the elementary matrix of the inverse operation: $P_{ij}^{-1} = P_{ij}$, $D_i(c)^{-1} = D_i(c^{-1})$ and $T_{ij}(c)^{-1} = T_{ij}(-c)$.
3. For each $p \times m$ matrix $A$ over $F$, right multiplication performs a column operation. Here $AP_{ij}$ exchanges columns $i$ and $j$ of $A$, $AD_i(c)$ multiplies column $i$ by $c$, and $AT_{ij}(c)$ adds $c$ times column $i$ to column $j$.

## Remarks

### Why each hypothesis is needed

In type $D_i(c)$ the scalar $c$ must be nonzero; otherwise $D_i(0)$ has a zero row and is singular.
In type $T_{ij}(c)$ the indices must differ; $I + cE_{ii}$ is the scaling $D_i(1 + c)$, and for $c = -1$ it is singular.

### Consequences

- If $A$ reduces to $R$ by the row operations $\rho_1, \dots, \rho_k$, then $R = E_k \cdots E_1 A$, where $E_s$ is the matrix of $\rho_s$.
- The matrix $E = E_k \cdots E_1$ is invertible, by the [[inverse of a product|0S4WTRE9GG]], and $A = E^{-1} R$.
- Row equivalent matrices have the same solutions of $Ax = 0$, since $EAx = 0$ if and only if $Ax = 0$.

### Converse

Each invertible matrix that performs a row operation by left multiplication is the elementary matrix of that operation, because $E = EI_m = \rho(I_m)$.

### Generalizations

The statement holds over each commutative ring, with $c$ a unit in type $D_i(c)$.
Part 1 holds for each row operation $\rho$ that is linear on columns: $\rho(A)$ is always $\rho(I_m) A$.

## Explanations

### L1 human

To do a row operation on a matrix, we can multiply it on the left by the elementary matrix of that operation.
To undo the row operation, we do the opposite operation, and its elementary matrix is the inverse.

### L2 human

Worked example: let $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $E = T_{12}(1) = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.

1. $EA = \begin{pmatrix} 1 + 3 & 2 + 4 \\ 3 & 4 \end{pmatrix} = \begin{pmatrix} 4 & 6 \\ 3 & 4 \end{pmatrix}$: row 2 was added to row 1.
2. $AE = \begin{pmatrix} 1 & 1 + 2 \\ 3 & 3 + 4 \end{pmatrix} = \begin{pmatrix} 1 & 3 \\ 3 & 7 \end{pmatrix}$: column 1 was added to column 2.
3. $E^{-1} = T_{12}(-1) = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$, and $E^{-1}(EA) = \begin{pmatrix} 4 - 3 & 6 - 4 \\ 3 & 4 \end{pmatrix} = A$.

A trap: the column operation of $T_{ij}(c)$ has the indices in the other order.

### L3 human

Part 1 says that each row operation is a linear map on the columns of $A$.
So it is given by left multiplication with the image of $I_m$.
The three types generate $\mathrm{GL}_m(F)$, by [[invertibility and row reduction|1ZK55FS2BF]].
