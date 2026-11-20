---
tag: 0ERWG4NXQ9
kind: statement
role: theorem
name: QR decomposition
msc: [15A23, 65F25]
topics: [8GQVME4SZZ]
audience: ug1
uses: [0D6RMJ10M9, 0MKABWDRNC, 0VT6P0GNQR, 0EVHJFTG9Z, 0EX045E2BP]
sources:
  - url: https://en.wikipedia.org/wiki/QR_decomposition
    locator: Square matrix
  - url: https://en.wikipedia.org/wiki/QR_decomposition
    locator: Rectangular matrix
  - book: isbn:9780321982384
    locator: Section 6.4
  - book: isbn:9781733146678
    locator: Chapter 4
same_as:
  wikidata: Q653242
  wikipedia: QR decomposition
---

## Statement

Let $\mathbb{K} = \R$ or $\C$, with the standard inner product $\ip{x}{y} = y^* x$ on $\mathbb{K}^m$, where $y^*$ is the [[conjugate transpose|0EX045E2BP]].

1. Thin QR, existence. Let $A$ be an $m \times n$ matrix over $\mathbb{K}$ whose columns $a_1, \dots, a_n$ are [[linearly independent|0EVHJFTG9Z]], so $m \ge n$. Then $A = QR$, where $Q$ is $m \times n$ with orthonormal columns, so $Q^* Q = I_n$, and $R$ is $n \times n$ [[upper triangular|0MKABWDRNC]] with real positive diagonal entries. The columns $q_1, \dots, q_n$ of $Q$ are the vectors produced by the [[Gram-Schmidt process|0VT6P0GNQR]] from $a_1, \dots, a_n$, and $r_{ij} = \ip{a_j}{q_i}$.
2. Uniqueness. In part 1, $Q$ and $R$ are unique.
3. Least squares. In part 1, for every $b \in \mathbb{K}^m$, the unique least-squares solution of $Ax = b$ is the solution $\hat x$ of the triangular system $R \hat x = Q^* b$.
4. Square case. Every $n \times n$ complex matrix is $A = QR$ with $Q$ [[unitary|0D6RMJ10M9]] and $R$ upper triangular. If $A$ is real, $Q$ and $R$ can be chosen real, with $Q$ orthogonal. If $A$ is invertible and the diagonal entries of $R$ are positive, then $Q$ and $R$ are unique.

Parts 1 to 3 have a [[proof by Gram-Schmidt|KHFJXQDZGC]].
Part 4 has a [[proof by clearing the first column|ZRPHF64HFG]], which also covers singular square matrices.

## Remarks

### Warning on the words

An *orthogonal matrix* is a square real matrix whose columns are orthonormal: of length $1$ and pairwise orthogonal.
An *orthogonal set* of vectors only needs to be pairwise orthogonal; its vectors need not have length $1$.
So the $m \times n$ factor $Q$ of part 1 has orthonormal columns, but for $m > n$ it is not an orthogonal matrix: $Q^{\mathsf{T}} Q = I_n$, while $Q Q^{\mathsf{T}} \ne I_m$.
In fact $Q Q^{\mathsf{T}}$ is the [[orthogonal projection|0B8KZRT28M]] onto the column space of $A$.

### Why each hypothesis is needed

- Independent columns in part 1: for $A$ with columns $(1, 0)$ and $(2, 0)$, Gram-Schmidt gives $q_1 = (1, 0)$ and then the zero vector, which cannot be normalized. A factorization still exists, but $R$ has a zero on its diagonal and is not unique.
- Positive diagonal in part 2: if $A = QR$, then also $A = (QD)(D^{-1} R)$ for any diagonal $D$ with entries $\pm 1$, or of modulus $1$ over $\C$. The sign condition removes this freedom.

### Consequences

- The [[thin QR factorization for independent columns|P5S1MTTDP8]] is part 1 over $\R$.
- [[Least squares from a QR factorization|JAHVYKS2VQ]] is part 3 over $\R$.
- $\det(A^* A) = \det(R)^2 = \prod_i r_{ii}^2$ for real $A$ with independent columns, since $A^* A = R^* R$. This is the [[Gram determinant|00SPJSDT3Z]] of the columns.

### Generalizations and computation

In numerical analysis, $A = QR$ is computed by [[Householder reflections|JDH0THTVGM]] or by [[Givens rotations|NM1KPS6E7Y]], which are more stable in floating point than classical Gram-Schmidt.
These methods give the full factorization $A = Q R$ with an $m \times m$ unitary $Q$ and an $m \times n$ upper triangular $R$, and the thin factors are their first $n$ columns and rows.
The QR decomposition is also the basic step of the [[QR algorithm|B6F8YWHYZ5]] for eigenvalues.

## Explanations

### L1 human

The QR decomposition writes a matrix as a matrix with perpendicular unit columns, times a triangular matrix.
The columns of $Q$ are the Gram-Schmidt vectors of the columns of $A$.
The matrix $R$ records how to rebuild each column of $A$ from the columns of $Q$.

### L2 human

For $A = \begin{pmatrix} 1 & 3 \\ 2 & 0 \\ 2 & 3 \end{pmatrix}$, [[the worked QR example|HNAQ6AXB2X]] gives $q_1 = \frac{1}{3}(1, 2, 2)$, $q_2 = \frac{1}{3}(2, -2, 1)$ and $R = \begin{pmatrix} 3 & 3 \\ 0 & 3 \end{pmatrix}$.
The product $QR$ gives back $A$.
The typical use is to solve least-squares problems: $R \hat x = Q^{\mathsf{T}} b$ is triangular and is solved by back substitution.
The trap is to call this $Q$ an orthogonal matrix and to use $Q Q^{\mathsf{T}} = I$, which is false for a $3 \times 2$ matrix.

### L3 human

The QR decomposition is the Gram-Schmidt process in matrix form, and its uniqueness says that the flag of subspaces $\operatorname{span}(a_1) \subseteq \operatorname{span}(a_1, a_2) \subseteq \cdots$ has exactly one adapted orthonormal basis with positive coordinates.
For invertible matrices it is the Iwasawa decomposition $GL_n(\R) = O(n) \cdot T^+$ of the general linear group, with $T^+$ the upper triangular matrices with positive diagonal.
Since $A^* A = R^* R$, the factor $R$ is the Cholesky factor of the [[positive definite matrix|0QQCG3JWJ4]] $A^* A$, which links QR to the [[normal equations|4D7MRG4D91]].
