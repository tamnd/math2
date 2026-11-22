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
Its leading minors are positive, but $M$ is not positive definite, and its form even takes a negative value.

1. $M$ is not [[symmetric|0N28QN4CYA]], since $m_{12} = -3$ and $m_{21} = 0$.
2. The leading principal [[minors|0SD528P0EK]] are
$$\Delta_1 = 1, \qquad \Delta_2 = 1 \cdot 1 - (-3) \cdot 0 = 1,$$
and both are positive.
3. For $x = (1, 1)$ we get $Mx = (1 - 3, 1) = (-2, 1)$, so
$$x^{\mathsf{T}} M x = 1 \cdot (-2) + 1 \cdot 1 = -1 < 0.$$
4. So $M$ is not [[positive definite|0QQCG3JWJ4]] under any convention, since the form is negative at a nonzero vector.
5. The form of $M$ equals the form of its symmetric part
$$S = \tfrac12 (M + M^{\mathsf{T}}) = \begin{pmatrix} 1 & -\tfrac32 \\ -\tfrac32 & 1 \end{pmatrix}.$$
6. The leading minors of $S$ are $1$ and $1 - \tfrac94 = -\tfrac54$, so Sylvester's test on $S$ gives the correct answer.

Check: $x^{\mathsf{T}} S x$ at $x = (1, 1)$ is $1 - \tfrac32 - \tfrac32 + 1 = -1$, the same value as in step 3.

## Remarks

[[Sylvester's criterion|0WKEF78PMV]] assumes that the matrix is Hermitian, and this example shows that the assumption is needed.
It is needed even in books that allow non-symmetric positive definite matrices, since there the test must be run on the symmetric part.
The leading minors of $M$ see the entry $0$ below the diagonal, but the form only sees the sum $m_{12} + m_{21} = -3$ of the two off-diagonal entries.

The eigenvalue test fails in the same way: $M$ is triangular, so its eigenvalues are its diagonal entries $1$ and $1$, both positive.
In fact every upper triangular matrix with positive diagonal has positive leading minors and positive eigenvalues, whatever its entries above the diagonal are.
If we replace $-3$ by $c$, the form is $x_1^2 + c x_1 x_2 + x_2^2$, and it is positive for $x \ne 0$ exactly when $\abs{c} < 2$.

## Explanations

### L1 human

Sylvester's test works only for symmetric matrices.
This matrix is not symmetric, and its two test numbers are $1$ and $1$, both positive.
But at the vector $(1, 1)$ the value of $x^{\mathsf{T}} M x$ is $-1$, so the test would give the wrong answer.

### L2 human

For a real matrix $M$, only the symmetric part enters the form, because $x^{\mathsf{T}} M x$ is a number and so equals its transpose $x^{\mathsf{T}} M^{\mathsf{T}} x$.
Average the two expressions to get $x^{\mathsf{T}} M x = x^{\mathsf{T}} S x$ with $S = \tfrac12 (M + M^{\mathsf{T}})$.
So every test for the sign of the form must be run on $S$, not on $M$.
Watch out: a triangular matrix with a positive diagonal always passes the minor test and the eigenvalue test, so neither test says anything about a non-symmetric matrix.
