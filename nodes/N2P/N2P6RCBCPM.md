---
tag: N2P6RCBCPM
kind: counterexample
name: An invertible matrix without an LU decomposition
msc: ["15A06", "15A23"]
topics: [DXSXFVDMXQ]
audience: ug1
uses: [0RKG5YW66Y, 0JVJ2WCXZH, 0EB9N0S33C, 00J3KZP8Y0, 0N4XY7Z3NN]
sources:
  - url: https://en.wikipedia.org/wiki/LU_decomposition
    locator: Existence and uniqueness
---

## Counterexample

Being invertible is not enough for elimination without swaps: a zero in the top left corner already blocks it.
Let $A = \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix}$ over $\mathbb{R}$.
Its determinant is $0 \cdot 1 - 1 \cdot 1 = -1 \neq 0$, so $A$ is [[invertible|0EB9N0S33C]].
Suppose that $A = LU$, with $L = \begin{bmatrix} 1 & 0 \\ \ell & 1 \end{bmatrix}$ [[lower triangular|00J3KZP8Y0]] and $U = \begin{bmatrix} u_{11} & u_{12} \\ 0 & u_{22} \end{bmatrix}$ [[upper triangular|0N4XY7Z3NN]].

1. The product is $LU = \begin{bmatrix} u_{11} & u_{12} \\ \ell u_{11} & \ell u_{12} + u_{22} \end{bmatrix}$.
2. The $(1, 1)$ entries give $u_{11} = 0$.
3. The $(2, 1)$ entries give $\ell u_{11} = 1$.
4. By step 2, $\ell u_{11} = 0$, which is not $1$.

So $A$ has no [[LU decomposition|0RKG5YW66Y]] of this form.
The statement "every invertible matrix has an LU decomposition" is false.

## Remarks

### Any lower triangular factor fails too

If $L$ may be any lower triangular matrix, the $(1, 1)$ entries give $\ell_{11} u_{11} = 0$, so $\ell_{11} = 0$ or $u_{11} = 0$.
If $\ell_{11} = 0$, the first row of $LU$ is zero, and if $u_{11} = 0$, its first column is zero.
Neither holds for $A$.

### The repair is a row exchange

With $P = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ we get $PA = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} = I \cdot PA$, an LU decomposition with $L = I$.
In general every square matrix has a factorization $PA = LU$ with $P$ a permutation matrix.
An invertible matrix has an LU decomposition with unit $L$ if and only if all its leading principal minors are nonzero, and here the first one is $a_{11} = 0$.

## Explanations

### L1 human

[[Gaussian elimination|0JVJ2WCXZH]] without swaps uses the top left entry to remove the entries below it.
Here the top left entry is $0$, so we cannot start.
The matrix is still invertible, so a zero in that place does not mean that something is wrong with the matrix.

### L2 human

1. Write $A = LU$ with unknown entries $\ell$, $u_{11}$, $u_{12}$ and $u_{22}$.
2. Multiply and compare the four entries with those of $A$.
3. The first entry forces $u_{11} = 0$, and then the entry below it is $0$, not $1$.
4. Swap the two rows of $A$, and the new matrix is already upper triangular.

This example is why computer programs compute $PA = LU$ and not $A = LU$.
Watch out: a matrix with a zero in a pivot place need not be singular, and a matrix with nonzero pivots can still be badly conditioned.
