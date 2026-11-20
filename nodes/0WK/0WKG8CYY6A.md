---
tag: 0WKG8CYY6A
kind: statement
role: theorem
name: Cholesky decomposition
msc: [15A23, 65F05]
topics: [SS4EVPKT3A]
audience: ug1
about: [0KX66CZMBB, 00J3KZP8Y0]
uses: [0QQCG3JWJ4, 0EZSD6T9E0, 0EKZCX4K3P, 0EX045E2BP]
proofs: [NRPFJZNDZ6]
sources:
  - url: https://en.wikipedia.org/wiki/Cholesky_decomposition
    locator: Statement
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Cholesky decomposition
  - book: isbn:9780521839402
    locator: Chapter 7
same_as:
  wikidata: Q515375
  wikipedia: Cholesky decomposition
---

## Statement

Let $A$ be an $n \times n$ complex [[Hermitian matrix|0P17NGQQMQ]].

1. If $A$ is [[positive definite|0KX66CZMBB]], then there is exactly one [[lower triangular matrix|00J3KZP8Y0]] $L$ with positive real diagonal entries such that
$$A = L L^*.$$
2. Conversely, if $A = L L^*$ for a lower triangular $L$ with positive real diagonal entries, then $A$ is positive definite.
3. If $A$ is real and positive definite, then $L$ is real, and $A = L L^T$.

## Remarks

The factor $L$ is the *Cholesky factor* of $A$.
Some books write $A = R^* R$ with $R = L^*$ upper triangular; this is the same decomposition.

### Why each hypothesis is needed

- Positive definiteness is needed for existence with a positive diagonal. If $A = L L^*$ with $L$ invertible, then $A$ is positive definite by part 2. So [[the all-ones matrix|YAAQD2E1BZ]], which is singular, has no such factor.
- The diagonal of $L$ must be positive for uniqueness. If $D$ is diagonal with entries $\pm 1$, then $(LD)(LD)^* = L L^*$.

### Consequences

- [[A $3 \times 3$ example|M3YVJ6CFJ5]] computes $L$ for $\begin{pmatrix} 4 & 2 & -2 \\ 2 & 10 & 2 \\ -2 & 2 & 6 \end{pmatrix}$ and multiplies it back.
- The decomposition is a symmetric form of the [[LU decomposition|0RKG5YW66Y]]. If $D$ is the diagonal of $L$, then $A = (L D^{-1}) (D L^*)$, with $L D^{-1}$ unit lower triangular and $D L^*$ upper triangular.
- It is linked to [[Gram-Schmidt|0VT6P0GNQR]] and the [[QR decomposition|0ERWG4NXQ9]]. If $B = QR$ with $Q$ having orthonormal columns and $R$ upper triangular with positive diagonal, then $B^* B = R^* R$. So $R^*$ is the Cholesky factor of $B^* B$.
- The test "Cholesky succeeds" is a practical test for positive definiteness. The algorithm stops at a nonpositive pivot exactly when $A$ is not positive definite.
- To solve $Ax = b$, solve $Ly = b$ by forward substitution and then $L^* x = y$ by back substitution.

### Converse

Part 2 is the converse of part 1.
So a Hermitian matrix is positive definite if and only if it has a Cholesky factor.

### Generalizations

- A positive semidefinite matrix has a factorization $A = L L^*$ with $L$ lower triangular and nonnegative diagonal, but $L$ need not be unique. This is in the Wikipedia article.
- The $LDL^*$ form writes $A = L D L^*$ with $L$ unit lower triangular and $D$ diagonal. It needs no square roots.

## History

The decomposition was found by André-Louis Cholesky for real matrices and published after his death in 1924, according to the Wikipedia article on the Cholesky decomposition.

## Explanations

### L1 human

A positive definite matrix is the product of a lower triangular matrix and its transpose.
This is like writing a positive number as the square of its positive square root.
For example, $\begin{pmatrix} 4 & 2 \\ 2 & 5 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$.
It is the fastest standard way to solve linear systems with such a matrix.

### L2 human

The entries of $L$ come one column at a time.
For column $j$:

1. $l_{jj} = \sqrt{a_{jj} - \sum_{k < j} \abs{l_{jk}}^2}$.
2. $l_{ij} = \left(a_{ij} - \sum_{k < j} l_{ik} \overline{l_{jk}}\right) / l_{jj}$ for $i > j$.

The number under the square root in item 1 is positive exactly when $A$ is positive definite.
[[The $3 \times 3$ example|M3YVJ6CFJ5]] follows these formulas.
A trap: the formulas need $A$ to be Hermitian, and they read only the lower half of $A$, so they give a wrong answer for a non-symmetric $A$.

### L3 human

The positive definite matrices form one orbit of $GL_n(\C)$ under $A \mapsto P A P^*$, and the Cholesky decomposition picks a canonical $P$ in the triangular group.
In group terms, the lower triangular matrices with positive diagonal act simply transitively on the positive definite cone.
The Cholesky factor of a Gram matrix $B^* B$ is the transpose of the $R$ factor of $B$, so Cholesky is Gram-Schmidt done on the Gram matrix.
In numerical linear algebra the algorithm is backward stable without pivoting, which is a topic of that area.
