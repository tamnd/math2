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

Multiplying by an elementary matrix on the left does its row operation, multiplying on the right does a column operation, and the inverse is the elementary matrix of the reverse operation.
Let $F$ be a field and let $E$ be an $m \times m$ [[elementary matrix|0M79HRJCRR]] over $F$, obtained from $I_m$ by the [[elementary row operation|04XWH28452]] $\rho$.

1. For each $m \times p$ matrix $A$ over $F$, the [[product|032Q9FB8MT]] $EA$ is the matrix $\rho(A)$ obtained from $A$ by the operation $\rho$.
2. $E$ is [[invertible|0TWTS88TWN]], and $E^{-1}$ is the elementary matrix of the inverse operation: $P_{ij}^{-1} = P_{ij}$, $D_i(c)^{-1} = D_i(c^{-1})$ and $T_{ij}(c)^{-1} = T_{ij}(-c)$.
3. For each $p \times m$ matrix $A$ over $F$, right multiplication performs a column operation: $AP_{ij}$ exchanges columns $i$ and $j$ of $A$, $AD_i(c)$ multiplies column $i$ by $c$, and $AT_{ij}(c)$ adds $c$ times column $i$ to column $j$.

## Remarks

### Seeing all three parts at once

Take $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $E = T_{12}(1) = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, which adds row 2 to row 1.
On the left, $E$ adds row 2 to row 1, as part 1 says:
$$EA = \begin{pmatrix} 1 + 3 & 2 + 4 \\ 3 & 4 \end{pmatrix} = \begin{pmatrix} 4 & 6 \\ 3 & 4 \end{pmatrix}.$$
On the right, it adds column 1 to column 2, as part 3 says:
$$AE = \begin{pmatrix} 1 & 1 + 2 \\ 3 & 3 + 4 \end{pmatrix} = \begin{pmatrix} 1 & 3 \\ 3 & 7 \end{pmatrix}.$$
The inverse $E^{-1} = T_{12}(-1)$ subtracts row 2 from row 1 again, and $E^{-1}(EA) = \begin{pmatrix} 4 - 3 & 6 - 4 \\ 3 & 4 \end{pmatrix} = A$.

### Why each condition is needed

In type $D_i(c)$ the scalar must be nonzero, since $D_i(0)$ has a zero row and is singular, so part 2 would fail.
In type $T_{ij}(c)$ the indices must differ.
The matrix $I + cE_{ii}$ is the scaling $D_i(1 + c)$, and for $c = -1$ it is singular.

### What it gives you

The theorem turns a reduction into an equation.
If $A$ reduces to $R$ by the row operations $\rho_1, \dots, \rho_k$, with matrices $E_1, \dots, E_k$, then $R = E_k \cdots E_1 A$.
The matrix $E = E_k \cdots E_1$ is invertible by the [[inverse of a product|0S4WTRE9GG]], so $A = E^{-1} R$.
Row equivalent matrices therefore have the same solutions of $Ax = 0$, since $EAx = 0$ exactly when $Ax = 0$.
This is the base of the theorem on [[invertibility and row reduction|1ZK55FS2BF]] and of [[the method for computing inverses|0Z83DHFMYM]].

### The converse

A matrix that performs a row operation $\rho$ by left multiplication must be the elementary matrix of $\rho$, because $M = MI_m = \rho(I_m)$.
So the elementary matrix of an operation is unique.

### Generalizations

The statement holds over any commutative ring, with $c$ a unit in type $D_i(c)$.
Part 1 holds for every operation on rows that acts on each column by the same linear map, because such an operation is left multiplication by its effect on $I_m$.

## Explanations

### L1 human

To do a row operation on a matrix, we can multiply it on the left by the elementary matrix of that operation.
To undo the row operation, we do the opposite operation, and its elementary matrix is the inverse.

### L2 human

The typical use is to replace "row reduce $A$" by "multiply $A$ on the left by an invertible matrix".
Then facts about products, such as the inverse of a product, apply to row reduction.
Watch out: the column operation of $T_{ij}(c)$ has the indices in the other order, so $AT_{12}(1)$ changes column 2, not column 1.

### L3 human

Part 1 says that each row operation is a linear map on the columns of $A$, so it is left multiplication by the image of $I_m$.
The three types generate $\mathrm{GL}_m(F)$, by [[invertibility and row reduction|1ZK55FS2BF]].
The replacements alone generate $\mathrm{SL}_m(F)$, which the sub-area returns to with [[transvections|0DTCBCKEJP]].
