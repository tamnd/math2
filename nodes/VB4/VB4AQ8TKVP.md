---
tag: VB4AQ8TKVP
kind: example
name: Positive leading minors on a non-symmetric matrix
msc: [15B57, 15A15]
topics: [SS4EVPKT3A]
audience: ug1
not_instance_of:
  - target: 0KX66CZMBB
    note: the matrix has positive leading minors but is not symmetric, and its form is -1 at (1, 1)
illustrates: [0WKEF78PMV]
uses: [0SD528P0EK, 0QQCG3JWJ4, 0N28QN4CYA]
sources:
  - url: https://en.wikipedia.org/wiki/Sylvester%27s_criterion
    locator: Proof for the case of positive definite matrices
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Extension for non-Hermitian square matrices
---

## Example

Let $M = \begin{pmatrix} 1 & -3 \\ 0 & 1 \end{pmatrix}$.

1. $M$ is not [[symmetric|0N28QN4CYA]], since $m_{12} = -3 \ne 0 = m_{21}$.
2. The leading principal [[minors|0SD528P0EK]] are $\Delta_1 = 1$ and $\Delta_2 = 1 \cdot 1 - (-3) \cdot 0 = 1$. Both are positive.
3. For $x = (1, 1)$, we get $Mx = (1 - 3, 1) = (-2, 1)$.
4. So $x^T M x = 1 \cdot (-2) + 1 \cdot 1 = -1 < 0$.
5. So the form $x \mapsto x^T M x$ is not positive, even though both leading minors are positive.
6. The form of $M$ equals the form of the symmetric part $S = \tfrac12(M + M^T) = \begin{pmatrix} 1 & -\tfrac32 \\ -\tfrac32 & 1 \end{pmatrix}$. Its minors are $1$ and $1 - \tfrac94 = -\tfrac54 < 0$, so Sylvester's test on $S$ gives the correct answer.

## Remarks

- [[Sylvester's criterion|0WKEF78PMV]] has the hypothesis that the matrix is Hermitian. This example shows that the hypothesis is needed, even for books that allow non-symmetric positive definite matrices.
- The eigenvalues of $M$ are $1$ and $1$, both positive. So the eigenvalue test also fails for non-symmetric matrices.
- The correct test for a non-symmetric real matrix is to test its symmetric part.

## Explanations

### L1 human

Sylvester's test works only for symmetric matrices.
This matrix is not symmetric, and its test numbers are $1$ and $1$.
But at the vector $(1, 1)$ the value of $x^T M x$ is $-1$.

### L2 human

For a non-symmetric real matrix $M$, only the symmetric part enters the form, because $x^T M x = x^T M^T x$.
So any test must use $\tfrac12(M + M^T)$ and not $M$.
The leading minors of $M$ see the entry $0$ below the diagonal, which the form does not see.
A trap: an upper triangular matrix with a positive diagonal always has positive leading minors, whatever its other entries are.
