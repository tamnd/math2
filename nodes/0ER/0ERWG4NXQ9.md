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

The QR decomposition is the Gram-Schmidt process written as a product of matrices: a matrix with independent columns is a matrix with orthonormal columns times an upper triangular matrix.

Let $\mathbb{K} = \R$ or $\C$, with the standard inner product $\ip{x}{y} = y^* x$ on $\mathbb{K}^m$, where $y^*$ is the [[conjugate transpose|0EX045E2BP]].

1. Thin QR, existence. Let $A$ be an $m \times n$ matrix over $\mathbb{K}$ whose columns $a_1, \dots, a_n$ are [[linearly independent|0EVHJFTG9Z]], so that $m \ge n$. Then $A = QR$, where $Q$ is $m \times n$ with orthonormal columns, so $Q^* Q = I_n$, and $R$ is $n \times n$ [[upper triangular|0MKABWDRNC]] with real positive diagonal entries. The columns $q_1, \dots, q_n$ of $Q$ are the vectors that the [[Gram-Schmidt process|0VT6P0GNQR]] produces from $a_1, \dots, a_n$, and $r_{ij} = \ip{a_j}{q_i}$.
2. Uniqueness. The factors $Q$ and $R$ in part 1 are unique.
3. Least squares. In part 1, for every $b \in \mathbb{K}^m$, the unique least-squares solution of $Ax = b$ is the solution $\hat x$ of the triangular system $R \hat x = Q^* b$.
4. Square case. Every $n \times n$ complex matrix is $A = QR$ with $Q$ [[unitary|0D6RMJ10M9]] and $R$ upper triangular. If $A$ is real, then $Q$ and $R$ can be chosen real, with $Q$ orthogonal. If $A$ is invertible and the diagonal entries of $R$ are required to be positive, then $Q$ and $R$ are unique.

Parts 1 to 3 have a [[proof by Gram-Schmidt|KHFJXQDZGC]].
Part 4 has a [[proof by clearing the first column|ZRPHF64HFG]], which also covers singular square matrices.

## Remarks

### A first factorization

Take the columns $a_1 = (1, 2, 2)$ and $a_2 = (3, 0, 3)$.
Gram-Schmidt first normalizes $a_1$: its length is $\sqrt{1 + 4 + 4} = 3$, so $q_1 = \tfrac{1}{3}(1, 2, 2)$ and $r_{11} = 3$.
Then it removes from $a_2$ its component along $q_1$, which has size $r_{12} = a_2 \cdot q_1 = (3 + 6)/3 = 3$:
$$v_2 = a_2 - 3 q_1 = (3, 0, 3) - (1, 2, 2) = (2, -2, 1).$$
This has length $3$, so $q_2 = \tfrac{1}{3}(2, -2, 1)$ and $r_{22} = 3$.
The result is
$$\begin{pmatrix} 1 & 3 \\ 2 & 0 \\ 2 & 3 \end{pmatrix} = \frac{1}{3} \begin{pmatrix} 1 & 2 \\ 2 & -2 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} 3 & 3 \\ 0 & 3 \end{pmatrix}.$$
Check: the second column of the product is $q_1 + q_2$ times $3$, which is $(1, 2, 2) + (2, -2, 1) = (3, 0, 3)$.
[[The worked QR example|HNAQ6AXB2X]] continues this calculation and solves a least-squares problem with it.

### Orthogonal matrix or orthogonal set

The words are a trap.
An *orthogonal matrix* is a square real matrix whose columns are orthonormal, that is, of length $1$ and pairwise orthogonal.
An *orthogonal set* of vectors only needs to be pairwise orthogonal, and its vectors need not have length $1$: $\{(1, 1), (1, -1)\}$ is an orthogonal set, but the matrix with these columns is not an orthogonal matrix.
The $m \times n$ factor $Q$ of part 1 has orthonormal columns, but for $m > n$ it is not an orthogonal matrix: $Q^{\mathsf{T}} Q = I_n$ while $Q Q^{\mathsf{T}} \ne I_m$.
In fact $Q Q^{\mathsf{T}}$ is the [[orthogonal projection|0B8KZRT28M]] onto the column space of $A$, and its trace is $n$, not $m$.

### Why each hypothesis is needed

Independent columns are needed in part 1.
For the columns $(1, 0)$ and $(2, 0)$, Gram-Schmidt gives $q_1 = (1, 0)$ and then the zero vector, which cannot be normalized.
A factorization $A = QR$ still exists, for example $Q = I_2$ and $R = A$, but $R$ has a zero on its diagonal.
It is also not unique, since $Q = \operatorname{diag}(1, -1)$ with the same $R$ works too.

The positive diagonal is needed in part 2.
If $A = QR$, then also $A = (QD)(D^{-1} R)$ for every diagonal $D$ whose entries are $\pm 1$, or of modulus $1$ over $\C$.
Requiring $r_{jj} > 0$ removes exactly this freedom.

### What it gives you

Part 3 is the main use: since $Q^* Q = I$, the normal equations $R^* R x = R^* Q^* b$ shrink to $R x = Q^* b$, which back substitution solves.
The statement on [[least squares from a QR factorization|JAHVYKS2VQ]] is this part over $\R$, and the [[thin QR factorization for independent columns|P5S1MTTDP8]] is part 1 over $\R$.
From $A^* A = R^* R$ we also get $\det(A^* A) = \prod_i r_{ii}^2$, the [[Gram determinant|00SPJSDT3Z]] of the columns.

### How computers find it

In numerical analysis, $A = QR$ is computed with [[Householder reflections|JDH0THTVGM]] or [[Givens rotations|NM1KPS6E7Y]], which keep orthogonality in floating point much better than classical Gram-Schmidt.
These methods give the full factorization, with an $m \times m$ unitary $Q$ and an $m \times n$ upper triangular $R$, and the thin factors are the first $n$ columns of $Q$ and the first $n$ rows of $R$.
The QR decomposition is also the basic step of the [[QR algorithm|B6F8YWHYZ5]] for eigenvalues.

## Explanations

### L1 human

The QR decomposition writes a matrix as a matrix with perpendicular unit columns times a triangular matrix.
The columns of $Q$ are what you get when you straighten the columns of $A$ one at a time so that they meet at right angles, and then scale them to length $1$.
The matrix $R$ records how to rebuild each column of $A$ from the columns of $Q$.
For the columns $(1, 2, 2)$ and $(3, 0, 3)$, the second column of $A$ is $3$ times the first unit vector plus $3$ times the second.

### L2 human

Here is a typical use: the least-squares solution of $Ax = b$ for the matrix of the first factorization and $b = (1, 1, 1)$.
First compute $Q^{\mathsf{T}} b$:
$$Q^{\mathsf{T}} b = \left( \frac{1 + 2 + 2}{3}, \frac{2 - 2 + 1}{3} \right) = \left( \frac{5}{3}, \frac{1}{3} \right).$$
The bottom row of $R \hat x = Q^{\mathsf{T}} b$ reads $3 \hat x_2 = \tfrac{1}{3}$, so $\hat x_2 = \tfrac{1}{9}$.
The top row reads $3 \hat x_1 + 3 \cdot \tfrac{1}{9} = \tfrac{5}{3}$, so $\hat x_1 = \tfrac{4}{9}$.
The method never forms $A^{\mathsf{T}} A$, so it avoids the squared condition number of the [[normal equations|4D7MRG4D91]].
The trap is to treat this $Q$ as an orthogonal matrix and use $Q Q^{\mathsf{T}} = I$, which is false for a $3 \times 2$ matrix.

### L3 human

The QR decomposition is Gram-Schmidt in matrix form.
Its uniqueness says that the flag of subspaces $\operatorname{span}(a_1) \subseteq \operatorname{span}(a_1, a_2) \subseteq \cdots$ has exactly one adapted orthonormal basis $q_1, \dots, q_n$ with $\ip{a_j}{q_j} > 0$ for each $j$.
For invertible real matrices it gives the Iwasawa decomposition $GL_n(\R) = O(n) \cdot T^+$, where $T^+$ is the group of upper triangular matrices with positive diagonal.
Since $A^* A = R^* R$, the factor $R$ is the Cholesky factor of the [[positive definite matrix|0QQCG3JWJ4]] $A^* A$, and this links QR back to the normal equations.
