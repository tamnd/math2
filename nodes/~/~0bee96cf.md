---
tag: ~0bee96cf
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

1. $A$ is real and symmetric, since $a_{12} = a_{21} = -1$, $a_{23} = a_{32} = -1$ and $a_{13} = a_{31} = 0$.
2. The first leading principal [[minor|0SD528P0EK]] is $\Delta_1 = 2$.
3. The second leading minor is $\Delta_2 = 2 \cdot 2 - (-1)(-1) = 3$.
4. The third leading minor is $\Delta_3 = \det A$. Expansion along the first row gives $2(2 \cdot 2 - 1) - (-1)((-1) \cdot 2 - 0) + 0 = 6 - 2 = 4$.
5. All three leading minors $2, 3, 4$ are positive. By [[Sylvester's criterion|0WKEF78PMV]], $A$ is positive definite.
6. Check by eigenvalues. The characteristic polynomial is $\det(A - tI) = (2 - t)\left((2 - t)^2 - 2\right)$. Its roots are $t = 2$ and $t = 2 \pm \sqrt2$.
7. All three eigenvalues $2 - \sqrt2 \approx 0.586$, $2$ and $2 + \sqrt2 \approx 3.414$ are positive. So [[the eigenvalue test|0HYC2RHD3M]] gives the same answer.
8. Check by the form. For $x = (x_1, x_2, x_3)$, we have $x^T A x = x_1^2 + (x_1 - x_2)^2 + (x_2 - x_3)^2 + x_3^2$. This is $0$ only when $x_1 = 0$, $x_2 = x_1$ and $x_3 = x_2$, so only at $x = 0$.

## Remarks

- The product of the eigenvalues is $2(2 - \sqrt2)(2 + \sqrt2) = 2 \cdot 2 = 4 = \Delta_3$, as it must be.
- The same pattern holds for the $n \times n$ matrix with $2$ on the diagonal and $-1$ next to it. Its leading minors are $\Delta_k = k + 1$, by the recurrence $\Delta_k = 2\Delta_{k-1} - \Delta_{k-2}$.
- This matrix is the second difference matrix of numerical analysis, which is a topic of numerical linear algebra.

## Explanations

### L1 human

We test whether a $3 \times 3$ matrix is positive definite.
Sylvester's test looks at the top-left corners of size $1$, $2$ and $3$.
Their determinants are $2$, $3$ and $4$, and all are positive.
So the matrix is positive definite.

### L2 human

Sylvester's test needs $n$ determinants, and here they are small.
The eigenvalue check in steps 6 and 7 needs the roots of a cubic, which is harder in general.
The sum of squares in step 8 is a third proof, and it shows the reason directly.
A trap: the test uses the leading minors only for positive definiteness; for semidefiniteness it needs all principal minors.
