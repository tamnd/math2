---
tag: RSQW92W4PD
kind: example
name: Sylvester's test on a tridiagonal 3 × 3 matrix
msc: [15B57, 15A15]
topics: [SS4EVPKT3A]
audience: ug1
instance_of: [0KX66CZMBB]
illustrates: [0WKEF78PMV, 0HYC2RHD3M]
uses: [0SD528P0EK, 0QQCG3JWJ4]
sources:
  - url: https://en.wikipedia.org/wiki/Sylvester%27s_criterion
    locator: Proof for the case of positive definite matrices
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Eigenvalues
---

## Example

Let
$$A = \begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{pmatrix}.$$
We show that $A$ is [[positive definite|0QQCG3JWJ4]] by three different tests, and the three answers agree.

1. $A$ is real and symmetric, since $a_{12} = a_{21} = -1$, $a_{23} = a_{32} = -1$ and $a_{13} = a_{31} = 0$.
2. The leading principal [[minors|0SD528P0EK]] of size $1$ and $2$ are $\Delta_1 = 2$ and $\Delta_2 = 2 \cdot 2 - (-1)(-1) = 3$.
3. The third leading minor is $\Delta_3 = \det A$. Expansion along the first row gives
$$\det A = 2 \bigl( 2 \cdot 2 - (-1)(-1) \bigr) - (-1) \bigl( (-1) \cdot 2 - (-1) \cdot 0 \bigr) + 0 = 6 - 2 = 4.$$
4. All three leading minors $2, 3, 4$ are positive, so $A$ is positive definite by [[Sylvester's criterion|0WKEF78PMV]].
5. For the eigenvalue test, expand $\det(A - tI)$ along the first row:
$$\det(A - tI) = (2 - t)\bigl( (2 - t)^2 - 1 \bigr) - (2 - t) = (2 - t)\bigl( (2 - t)^2 - 2 \bigr).$$
The roots are $t = 2$ and $t = 2 \pm \sqrt2$, that is, about $0.586$, $2$ and $3.414$.
All three are positive, so [[the eigenvalue test|0HYC2RHD3M]] gives the same answer.
6. For the form itself, write it as a sum of squares:
$$x^{\mathsf{T}} A x = 2x_1^2 + 2x_2^2 + 2x_3^2 - 2x_1 x_2 - 2x_2 x_3 = x_1^2 + (x_1 - x_2)^2 + (x_2 - x_3)^2 + x_3^2.$$
The sum is $0$ only when $x_1 = 0$, $x_2 = x_1$ and $x_3 = x_2$, that is, only at $x = 0$.

Check: the product of the eigenvalues is $2 (2 - \sqrt2)(2 + \sqrt2) = 2 \cdot 2 = 4$, which is $\det A = \Delta_3$, as it must be.

## Remarks

Each test has its own cost.
Sylvester's test needs three determinants, and here they are small.
The eigenvalue test needs the roots of a cubic, which is hard in general and easy here only because of the factor $2 - t$.
The sum of squares is the most direct proof, and it shows why the matrix is positive definite: each square measures one difference of neighbors.

The same pattern holds for the $n \times n$ matrix with $2$ on the diagonal and $-1$ next to it.
Expanding along the last row gives the recurrence $\Delta_k = 2\Delta_{k-1} - \Delta_{k-2}$, and with $\Delta_1 = 2$ and $\Delta_2 = 3$ it gives $\Delta_k = k + 1 > 0$.
This matrix is the second difference matrix of numerical analysis, which approximates $-u''$ on a grid.
If we change the diagonal entries from $2$ to $1$, the $2 \times 2$ leading minor becomes $1 - 1 = 0$, and the matrix is no longer positive definite.
In fact the form of the new matrix is $1 + 1 + 1 - 2 - 2 = -1$ at $(1, 1, 1)$, so it is not even semidefinite.

## Explanations

### L1 human

We test whether a $3 \times 3$ matrix is positive definite.
Sylvester's test looks at the top left corners of size $1$, $2$ and $3$.
Their determinants are $2$, $3$ and $4$, and all of them are positive.
So the matrix is positive definite.

### L2 human

The three tests in the example give the same answer, and that is the content of two theorems.
Sylvester's criterion and the eigenvalue test are both equivalent to the definition for symmetric matrices, so we may use whichever test is cheapest.
For a hand computation of a small matrix, the leading minors are usually cheapest.
For a large matrix on a computer, the Cholesky factorization is the usual test.
It succeeds exactly when the pivots of elimination are positive, and here they are $\Delta_1 = 2$, $\Delta_2 / \Delta_1 = \tfrac32$ and $\Delta_3 / \Delta_2 = \tfrac43$.
Watch out: the leading minors test only positive definiteness; for semidefiniteness every principal minor must be checked.
