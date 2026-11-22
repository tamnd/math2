---
tag: YYBT7MBTY6
kind: example
name: An invertible matrix that is not elementary
msc: ["15A23"]
topics: [P8J6QR66TJ]
audience: ug1
instance_of: [0EB9N0S33C]
not_instance_of:
  - target: 01REXW3WWE
    note: the matrix needs two row operations on the identity, a row exchange and a row scaling, so it is a product of two elementary matrices but not elementary itself
uses: [0M79HRJCRR, 04XWH28452, 032Q9FB8MT]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_matrix
    locator: lead section
---

## Example

Let $A = \begin{pmatrix} 0 & 2 \\ 1 & 0 \end{pmatrix}$ over $\mathbb{Q}$.
We show that $A$ is invertible but is not an [[elementary matrix|0M79HRJCRR]].

1. One row operation on $I_2$ gives one of three shapes: the exchange $P_{12} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, a scaling $D_i(c)$ that is diagonal, or a matrix $T_{ij}(c)$ with both diagonal entries equal to $1$.
2. The matrix $A$ is not $P_{12}$, because its $(1, 2)$ entry is $2$ and not $1$.
3. It is not a scaling, because its off-diagonal entries $2$ and $1$ are nonzero.
4. It is not of type $T_{ij}(c)$, because its diagonal entries are $0$ and not $1$.
5. So $A$ is not elementary.
6. But $A$ is a product of two elementary matrices, a scaling after an exchange:
$$D_1(2) P_{12} = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 2 \\ 1 & 0 \end{pmatrix} = A.$$
7. The inverse of a product reverses the factors, and each factor is undone by an elementary matrix, so
$$A^{-1} = P_{12}^{-1} D_1(2)^{-1} = P_{12} D_1(\tfrac{1}{2}) = \begin{pmatrix} 0 & 1 \\ \tfrac{1}{2} & 0 \end{pmatrix}.$$

Check: $A A^{-1} = \begin{pmatrix} 2 \cdot \tfrac{1}{2} & 0 \\ 0 & 1 \end{pmatrix} = I_2$ and $A^{-1} A = \begin{pmatrix} 1 & 0 \\ 0 & \tfrac{1}{2} \cdot 2 \end{pmatrix} = I_2$.

## Remarks

Invertible and elementary are different notions.
Every elementary matrix is invertible, but an invertible matrix is in general only a product of elementary matrices, as the theorem on [[invertibility and row reduction|1ZK55FS2BF]] says.
The factorization is not unique: scaling the second row first also works, since $P_{12} D_2(2) = \begin{pmatrix} 0 & 2 \\ 1 & 0 \end{pmatrix}$ as well.

If we change the entry $2$ to $1$, the matrix becomes $P_{12}$, which is elementary.
So a single entry decides whether one row operation suffices.

## Explanations

### L1 human

An elementary matrix records exactly one row step done to the identity.
This matrix needs two steps from the identity: exchange the two rows, then double the new first row.

### L2 human

To test whether a matrix is elementary, compare it with the three shapes of step 1.
To invert a product of elementary matrices, invert each factor and reverse the order.
Watch out: a matrix that looks simple, with only two nonzero entries, need not be elementary.
