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

Every matrix of the form $B^* B$ is positive semidefinite, it is definite exactly when the columns of $B$ are independent, and every positive semidefinite matrix has this form.

Let $B$ be an $m \times n$ complex matrix, and let $B^*$ be its [[conjugate transpose|0DXKE10PHF]].

1. The $n \times n$ matrix $B^* B$ is [[positive semidefinite|01MMVW8CKC]].
2. $B^* B$ is [[positive definite|0KX66CZMBB]] if and only if the columns of $B$ are [[linearly independent|0CRMGPAH83]].
3. Conversely, every positive semidefinite $n \times n$ matrix $A$ equals $B^* B$ for some $n \times n$ matrix $B$.
4. If $A$ is positive definite and $A = B^* B$, then the columns of $B$ are independent, and $B$ can be chosen square and invertible.

For real matrices the same holds with $B^{\mathsf{T}} B$ and real $B$.
In particular, $A^* A$ and $A A^*$ are positive semidefinite for every matrix $A$, since $A A^* = (A^*)^* A^*$.
The [[proof|1KF3RPY39H]] uses the identity $x^* B^* B x = \norm{Bx}^2$.

## Remarks

### A first factorization

Take $B = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$, whose columns $(1, 1)$ and $(1, 0)$ are independent.
Multiply out:
$$B^{\mathsf{T}} B = \begin{pmatrix} 1 \cdot 1 + 1 \cdot 1 & 1 \cdot 1 + 1 \cdot 0 \\ 1 \cdot 1 + 0 \cdot 1 & 1 \cdot 1 + 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}.$$
Its form is $\norm{Bx}^2 = (x_1 + x_2)^2 + x_1^2$, which is $0$ only when $x_1 = 0$ and $x_2 = 0$.
So $B^{\mathsf{T}} B$ is positive definite, as part 2 says.
For $B = \begin{pmatrix} 1 & 1 \end{pmatrix}$ the two columns are equal, and $B^{\mathsf{T}} B$ is [[the all-ones matrix|YAAQD2E1BZ]], which is only semidefinite.

### Why each hypothesis is needed

Part 2 needs independent columns, and the all-ones example shows what happens without them: a dependence $x_1 b_1 + x_2 b_2 = 0$ with $x = (1, -1)$ makes the form $\norm{Bx}^2$ zero.
Part 3 needs the matrix to be positive semidefinite, because part 1 shows that every $B^* B$ is.
For instance $\operatorname{diag}(1, -1)$ is not $B^* B$ for any $B$, since its form is $-1$ at $(0, 1)$.

### What it gives you

The entry $(i, j)$ of $B^* B$ is $b_i^* b_j$ for the columns $b_1, \dots, b_n$ of $B$, so $B^* B$ is a [[Gram matrix|00SPJSDT3Z]] of the columns.
With the convention $G_{ij} = \ip{v_i}{v_j}$ of the [[Gram matrix definition|0HX8HZ1WTQ]] and $\ip{x}{y} = y^* x$, we get $B^* B = G^{\mathsf{T}} = \overline{G}$, and $\overline{G}$ is positive semidefinite exactly when $G$ is.
So a matrix is positive semidefinite exactly when it is the Gram matrix of some vectors, and positive definite exactly when those vectors are independent.
The [[Gram matrix invertibility statement|EM1QNRGWQ8]] follows from part 2 and the [[eigenvalue test|0HYC2RHD3M]].
In the [[normal equations|4D7MRG4D91]] $A^{\mathsf{T}} A x = A^{\mathsf{T}} b$, the matrix $A^{\mathsf{T}} A$ is positive definite when the columns of $A$ are independent, so the least-squares solution is unique.

### The converse and the choice of factor

Parts 3 and 4 are the converses of parts 1 and 2.
The factor $B$ is far from unique: if $A = B^* B$ and $W$ is [[unitary|0D6RMJ10M9]], then $(WB)^* (WB) = B^* W^* W B = A$.
Two choices are standard.
The [[Cholesky factor|0WKG8CYY6A]] makes $B$ upper triangular with positive diagonal, for positive definite $A$.
The [[square root|EQ98KW1ZN4]] makes $B$ itself positive semidefinite, and then $B$ is unique.

### Generalizations

In any inner product space, the Gram matrix of vectors $v_1, \dots, v_n$ is positive semidefinite, and it is positive definite exactly when the $v_i$ are independent.
For a linear map $T$ between finite-dimensional inner product spaces, $T^* T$ is a positive semidefinite operator, and this is the starting point of the [[singular value decomposition|000NPTMX6J]].

## History

The Gram matrix is named after the Danish mathematician Jørgen Pedersen Gram.

## Explanations

### L1 human

For any matrix $B$, the matrix $B^{\mathsf{T}} B$ gives $x^{\mathsf{T}} B^{\mathsf{T}} B x = \norm{Bx}^2$.
A squared length is never negative, so $B^{\mathsf{T}} B$ is positive semidefinite.
The value is zero only when $Bx = 0$, and if the columns of $B$ are independent, that happens only for $x = 0$.

### L2 human

Here is a typical use: show that $A = \begin{pmatrix} 5 & 3 \\ 3 & 2 \end{pmatrix}$ is positive definite by writing it as $B^{\mathsf{T}} B$.
The entries of $A$ ask for columns $b_1, b_2$ with $\norm{b_1}^2 = 5$, $\norm{b_2}^2 = 2$ and $b_1 \cdot b_2 = 3$.
The columns $b_1 = (2, 1)$ and $b_2 = (1, 1)$ work: $4 + 1 = 5$, $1 + 1 = 2$ and $2 + 1 = 3$.
They are independent, since $\det \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} = 1 \ne 0$, so $A$ is positive definite by part 2.
This is how positive definite matrices usually arrive in practice: as inner products of some vectors.
Watch out: $B B^{\mathsf{T}}$ is also positive semidefinite, but it is $m \times m$, and it is definite when the rows of $B$, not the columns, are independent.

### L3 human

Parts 1 to 4 identify positive semidefinite matrices with Gram matrices of vectors in $\C^n$.
The rank of $B^* B$ equals the rank of $B$, which is the dimension of the span of the columns.
So the positive semidefinite $n \times n$ matrices of rank $r$ correspond to lists of $n$ vectors in $\C^r$ that span $\C^r$, taken up to unitary maps of $\C^r$.
The same identification is the start of the theory of reproducing kernels, and of semidefinite programming, where a positive semidefinite unknown matrix stands for an unknown configuration of vectors.
