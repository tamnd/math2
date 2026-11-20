---
tag: ~fab8b33f
kind: statement
role: proposition
name: The columns of a square matrix form a basis iff the matrix is invertible
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
about: [0KCQ9Y3QKA]
uses: [0VTQTPQGAV, 0EB9N0S33C, 76GG9B25A1]
proofs: [~b6ad4244]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: The invertible matrix theorem
  - book: isbn:9780321982384
    locator: Section 2.3
---

## Statement

Let $F$ be a field, and let $A$ be an $n \times n$ matrix over $F$ with columns $v_1, \dots, v_n \in F^n$.
Then $(v_1, \dots, v_n)$ is a [[basis|0VTQTPQGAV]] of $F^n$ if and only if $A$ is [[invertible|0EB9N0S33C]].
So the ordered bases of $F^n$ are exactly the column lists of the invertible $n \times n$ matrices.

## Remarks

### Why each hypothesis is needed

The matrix must be square: the $2 \times 3$ matrix with columns $e_1, e_2, e_1 + e_2$ has columns that span $F^2$, but they are not a basis and the matrix has no two-sided inverse.

### Consequences

The number of ordered bases of $\mathbb{F}_q^n$ equals the [[order of $GL_n(\mathbb{F}_q)$|0JQ1KNQW2K]]; see [[vector spaces over finite fields|~3bc74888]].
To test whether $n$ vectors form a basis of $F^n$, compute a [[determinant|0C3CFHDN6R]] or row reduce; see also [[the row-reduction form|JXTGZPZP47]].

### Converse

The statement is an equivalence.

### Generalizations

For a commutative ring $R$, the columns of a square matrix form a basis of $R^n$ exactly when the matrix is invertible, exactly when its determinant is a unit.

## Explanations

### L1 human

A basis of $F^n$ is the same as an invertible matrix, read column by column.
The inverse matrix computes coordinates: $[x]_B = A^{-1} x$.

### L2 human

Example: $A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ has inverse $\begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$.
So $(2, 1), (1, 1)$ is a basis of $\R^2$, and the coordinates of $(3, 2)$ are $A^{-1}(3, 2) = (1, 1)$.
Check: $(2, 1) + (1, 1) = (3, 2)$.
