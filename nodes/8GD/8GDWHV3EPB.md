---
tag: 8GDWHV3EPB
kind: example
name: The product of an upper and a lower triangular matrix need not be triangular
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
not_instance_of:
  - target: 0N4XY7Z3NN
    note: for U = (1, 1; 0, 1) and L = (1, 0; 1, 1), the product UL = (2, 1; 1, 1) has nonzero entries both above and below the diagonal
uses: [0MKABWDRNC, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: Properties
---

## Example

Let
$$U = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \qquad L = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$$
over $\mathbb{R}$, so that $U$ is upper triangular and $L$ is lower triangular.
We show that their product is neither.

1. By the [[product rule|076JGP6R3T]], row 1 of $U$ against the columns of $L$ gives $(1 + 1, 0 + 1)$, and row 2 gives $(0 + 1, 0 + 1)$:
$$UL = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}.$$
2. The entry $(2, 1)$ of $UL$ is $1 \neq 0$, so $UL$ is not upper [[triangular|0MKABWDRNC]].
3. The entry $(1, 2)$ of $UL$ is $1 \neq 0$, so $UL$ is not lower triangular either.
4. The diagonal of $UL$ is $(2, 1)$, not the product $(1 \cdot 1, 1 \cdot 1) = (1, 1)$ of the diagonals.
5. In the other order,
$$LU = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix},$$
which is again not triangular.

## Remarks

The [[product theorem|45RET2Y995]] needs both factors to be upper triangular, or both lower triangular.
With one factor of each kind, the zeros below the diagonal of $U$ and the zeros above the diagonal of $L$ do not cover each other, and nonzero terms appear on both sides.

The failure is also useful.
Many matrices can be written as a lower triangular factor times an upper triangular factor, and step 5 is such a factorization of $\begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$.
This is the [[LU decomposition|0RKG5YW66Y]] of the topic on [[invertible matrices and factorizations|P8J6QR66TJ]].

## Explanations

### L1 human

An upper triangular matrix has zeros below the diagonal, and a lower triangular one has zeros above it.
When you multiply one of each, the zeros do not survive.
Here the product $\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ has no zero at all.

### L2 human

As maps, $U$ keeps the line through $e_1$, since $Ue_1 = e_1$, and $L$ keeps the line through $e_2$, since $Le_2 = e_2$.
The product $UL$ sends $e_1$ to $U(e_1 + e_2) = (2, 1)$, off the line of $e_1$, and so it is not upper triangular.
Watch out: the diagonal rule $(UV)_{ii} = u_{ii} v_{ii}$ fails here too, so it cannot be used for mixed products.
