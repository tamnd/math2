---
tag: 0AM050KCAW
kind: statement
role: theorem
name: Gram matrices are positive semidefinite
msc: [15B57, 15A63]
topics: [SS4EVPKT3A]
audience: ug1
about: [01MMVW8CKC, 0KX66CZMBB, 00SPJSDT3Z]
uses: [0880F9EQCP, 0QQCG3JWJ4, 0EX045E2BP, 0EVHJFTG9Z, 0HX8HZ1WTQ]
proofs: [1KF3RPY39H]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Decomposition
  - url: https://en.wikipedia.org/wiki/Gram_matrix
    locator: Positive-semidefiniteness
  - book: isbn:9783031410253
    locator: Chapter 7
---

## Statement

Let $B$ be an $m \times n$ complex matrix, and let $B^*$ be its [[conjugate transpose|0DXKE10PHF]].

1. The $n \times n$ matrix $B^* B$ is [[positive semidefinite|01MMVW8CKC]].
2. $B^* B$ is [[positive definite|0KX66CZMBB]] if and only if the columns of $B$ are [[linearly independent|0CRMGPAH83]].
3. Conversely, every positive semidefinite $n \times n$ matrix $A$ equals $B^* B$ for some $n \times n$ matrix $B$.
4. If $A$ is positive definite, then every $B$ with $A = B^* B$ has independent columns, and $B$ can be chosen square and invertible.

For real matrices the same holds with $B^T B$ and real $B$.

## Remarks

### Why each hypothesis is needed

- In part 2 the columns must be independent. For $B = \begin{pmatrix} 1 & 1 \end{pmatrix}$, the columns are equal and $B^T B$ is [[the all-ones matrix|YAAQD2E1BZ]], which is not positive definite.
- In part 3 the matrix must be positive semidefinite, since every $B^* B$ is by part 1.

### Consequences

- The entry $(i, j)$ of $B^* B$ is $b_i^* b_j$ for the columns $b_i$. So $B^* B$ is the [[Gram matrix|00SPJSDT3Z]] of the columns, up to the order of the two slots. With the convention $G_{ij} = \ip{v_i}{v_j}$ of the [[Gram matrix definition|0HX8HZ1WTQ]], $B^* B = G^T$, and $G^T = \overline{G}$ is positive semidefinite exactly when $G$ is.
- By parts 1 and 3, a matrix is positive semidefinite if and only if it is the Gram matrix of some vectors. By parts 2 and 4, it is positive definite if and only if these vectors are independent.
- The [[Gram matrix invertibility statement|EM1QNRGWQ8]] follows from part 2 and the [[eigenvalue test|0HYC2RHD3M]].
- In the [[normal equations|4D7MRG4D91]] $A^T A x = A^T b$, the matrix $A^T A$ is positive definite when the columns of $A$ are independent.

### Converse

Parts 3 and 4 are the converses of parts 1 and 2.
The factor $B$ is not unique: if $A = B^* B$ and $W$ is [[unitary|0D6RMJ10M9]], then $A = (WB)^* (WB)$.
Two special choices are the [[Cholesky factor|0WKG8CYY6A]], with $B$ upper triangular, and the [[square root|EQ98KW1ZN4]], with $B$ positive semidefinite.

### Generalizations

- In any inner product space, the Gram matrix of vectors $v_1, \dots, v_n$ is positive semidefinite, and it is positive definite if and only if the $v_i$ are independent.
- For an operator $T$ between inner product spaces, $T^* T$ is a positive operator.

## History

The Wikipedia article on definite matrices states the decomposition $A = B^* B$ as a characterization of positive semidefinite matrices.

## Explanations

### L1 human

For any matrix $B$, the matrix $B^T B$ gives $x^T B^T B x = \norm{Bx}^2$.
A squared length is never negative, so $B^T B$ is positive semidefinite.
The value is zero only when $Bx = 0$.
If the columns of $B$ are independent, this happens only for $x = 0$.
Conversely, every positive semidefinite matrix has this form.

### L2 human

Use part 1 to show that a matrix is positive semidefinite: write it as $B^T B$.
Use part 3 in the other direction: a positive semidefinite matrix is a matrix of inner products of some vectors.
Worked example: $\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} = B^T B$ with $B = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$.
The columns $(1, 1)$ and $(1, 0)$ are independent, so the matrix is positive definite.
A trap: the matrix $B B^T$ is also positive semidefinite, but it is $m \times m$, and it is positive definite when the rows of $B$ are independent.

### L3 human

Parts 1 to 4 identify positive semidefinite matrices with Gram matrices of vectors in $\C^n$.
The rank of $B^* B$ equals the rank of $B$, which is the dimension of the span of the vectors.
So positive semidefinite $n \times n$ matrices of rank $r$ correspond to configurations of $n$ vectors in $\C^r$, up to unitary maps.
This identification is the start of the theory of reproducing kernels and of semidefinite programming.
