---
tag: 39XSQ9MTZ3
kind: example
name: Rayleigh quotient of a non-symmetric matrix exceeds its eigenvalues
msc: ["15A18", "15A42"]
topics: [3YM9EK6VMB]
audience: ug1
not_instance_of:
  - target: 0NEGN5CRSC
    note: the matrix with rows (1, 4) and (0, 1) is not symmetric, and its Rayleigh quotient takes the values 3 and -1, while its only eigenvalue is 1
illustrates: [T7MFPSY009]
uses: [06WHP8SE98, 0N28QN4CYA]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh_quotient
    locator: Bounds for Hermitian M
---

## Example

Let $A = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}$ act on $\mathbb{R}^2$ with the dot product.
The matrix is upper triangular, so its only eigenvalue is $1$.
It is not [[symmetric|0N28QN4CYA]].

1. For $x = (x_1, x_2)$, we get $x^T A x = x_1^2 + 4 x_1 x_2 + x_2^2$.
2. At $x = (1, 1)$: $x^T A x = 1 + 4 + 1 = 6$ and $x^T x = 2$. So the [[Rayleigh quotient|06WHP8SE98]] is $R(1, 1) = 3$.
3. At $x = (1, -1)$: $x^T A x = 1 - 4 + 1 = -2$ and $x^T x = 2$. So $R(1, -1) = -1$.
4. Both values differ from the only eigenvalue $1$. So the bounds of [[the extreme value statement|T7MFPSY009]] fail for this matrix.

## Remarks

- For a real matrix, $x^T A x = x^T S x$ with the symmetric part $S = \tfrac{1}{2}(A + A^T) = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$.
- The eigenvalues of $S$ are $3$ and $-1$, with the eigenvectors $(1, 1)$ and $(1, -1)$. So the Rayleigh quotient of $A$ ranges over $[-1, 3]$, the range for $S$.
- So for a non-symmetric matrix, the Rayleigh quotient gives information about the symmetric part, not about the eigenvalues.

## Explanations

### L1 human

This shear-like matrix has only one stretch factor, $1$, along its one special direction.
But in other directions it can push a vector forward by a factor of $3$ or backward by a factor of $-1$.
So for a non-symmetric matrix, the Rayleigh quotient does not locate the eigenvalues.

### L2 human

How to compute the range of the Rayleigh quotient of a real matrix $A$:

1. Replace $A$ by its symmetric part $S = \tfrac{1}{2}(A + A^T)$. This does not change $x^T A x$.
2. Find the largest and the smallest eigenvalue of $S$. They are the maximum and the minimum of the quotient.

A trap: the eigenvalues of $A$ and of $S$ can be far apart.
Here they are $1$ for $A$, and $3$ and $-1$ for $S$.
