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

Let $A = \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix}$ over $\R$.
Its determinant is $0 \cdot 1 - 1 \cdot 1 = -1 \neq 0$, so $A$ is [[invertible|0EB9N0S33C]].
Suppose that $A = LU$, with $L = \begin{bmatrix} 1 & 0 \\ \ell & 1 \end{bmatrix}$ [[lower triangular|00J3KZP8Y0]] and $U = \begin{bmatrix} u_{11} & u_{12} \\ 0 & u_{22} \end{bmatrix}$ [[upper triangular|0N4XY7Z3NN]].

1. The product is $LU = \begin{bmatrix} u_{11} & u_{12} \\ \ell u_{11} & \ell u_{12} + u_{22} \end{bmatrix}$.
2. The $(1, 1)$ entries give $u_{11} = 0$.
3. The $(2, 1)$ entries give $\ell u_{11} = 1$.
4. By step 2, $\ell u_{11} = 0$, which is not $1$.

So $A$ has no [[LU decomposition|0RKG5YW66Y]] of this form.
The statement "every invertible matrix has an LU decomposition" is false.

## Remarks

If $L$ may be any lower triangular matrix, the same argument applies: the $(1, 1)$ entries give $\ell_{11} u_{11} = 0$, so $\ell_{11} = 0$ or $u_{11} = 0$, and then the first row or the first column of $LU$ is zero, which is false for $A$.
The correct statement needs a row exchange: with $P = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ we get $PA = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} = I \cdot PA$, which is an LU decomposition with $L = I$.
In general every square matrix has a factorization $PA = LU$ with $P$ a permutation matrix.
An invertible matrix has an LU decomposition with unit $L$ if and only if all its leading principal minors are nonzero; here the first one is $a_{11} = 0$.

## Explanations

### L1 human

[[Gaussian elimination|0JVJ2WCXZH]] without swaps uses the top left entry to remove the entries below it.
Here the top left entry is $0$, so we cannot start.
The matrix is still invertible, so a zero in that place does not mean that something is wrong with the matrix.

### L2 human

1. Write $A = LU$ with unknown entries $\ell$, $u_{11}$, $u_{12}$ and $u_{22}$.
2. Multiply and compare the four entries with those of $A$.
3. The first entry forces $u_{11} = 0$, and then the entry below it is $0$, not $1$.
4. Swap the two rows of $A$; the new matrix is already upper triangular.

The typical use is to show why computer programs compute $PA = LU$ and not $A = LU$.
A trap: a matrix with a zero pivot place need not be singular, and a matrix with nonzero pivot places can still be badly conditioned.
