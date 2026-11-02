---
tag: S7MC88TW6W
kind: statement
role: theorem
name: Bidiagonalization
msc: [65F15, 65F25]
uses: [0W02QESPJQ, JDH0THTVGM, 09VMDSRXWJ, 000NPTMX6J]
about: [09VMDSRXWJ]
sources:
  - url: https://en.wikipedia.org/wiki/Bidiagonalization
same_as:
  wikidata: Q4904167
  wikipedia: Bidiagonalization
---

## Statement

Let $A \in \R^{m \times n}$ with $m \ge n$.
Then there are [[orthogonal matrices|0W02QESPJQ]] $U \in \R^{m \times m}$ and $V \in \R^{n \times n}$ such that
$$U^T A V = \begin{pmatrix} B \\ 0 \end{pmatrix},$$
where $B \in \R^{n \times n}$ is upper bidiagonal: $b_{ij} = 0$ unless $j = i$ or $j = i + 1$.
Moreover $U$ can be taken as a product of at most $n$ [[Householder reflections|JDH0THTVGM]], and $V$ as a product of at most $n - 2$ of them.
This is the Golub–Kahan bidiagonalization.
The matrices $A$ and $B$ have the same [[singular values|09VMDSRXWJ]].

## Remarks

The construction alternates sides.
A reflection from the left zeros column $1$ below the diagonal.
A reflection from the right acting on columns $2, \dots, n$ then zeros row $1$ to the right of the superdiagonal.
The right reflection does not touch column $1$, so the zeros there survive.
Repeating on the trailing submatrix gives $B$ after $n$ left and $n - 2$ right reflections.
Singular values are preserved because multiplying by orthogonal matrices does not change $A^T A$ up to similarity: $(U^T A V)^T (U^T A V) = V^T A^T A V$.

The cost with Householder reflections is about $4 m n^2 - \tfrac{4}{3} n^3$ floating point operations.
The matrix $B^T B$ is symmetric tridiagonal.
So bidiagonalization is the first phase of the standard [[singular value decomposition|000NPTMX6J]] algorithm, followed by an implicit QR iteration or a divide-and-conquer method on $B$.
One cannot go further to a diagonal matrix in finitely many steps in general, because the singular values are roots of polynomials of arbitrary degree.
Example: let $n = 2$.
One left reflection maps the first column to a multiple of $e_1$, and one more acts on rows $2, \dots, m$ of the second column.
This already gives an upper bidiagonal $2 \times 2$ block, with $V = I$.
When $m \gg n$, it is cheaper to compute a QR factorization first and bidiagonalize the triangular factor.

## Explanations

### L1 human

Bidiagonalization uses rotations and reflections to turn any rectangular matrix into one whose only nonzero entries are on the diagonal and just above it.
These operations keep the singular values, which measure how much the matrix stretches in its principal directions.
The simpler shape makes computing those singular values much faster.

### L2 human

It plays for the singular value decomposition the role that reduction to tridiagonal or Hessenberg form plays for eigenvalues.
A Lanczos-type variant, Golub–Kahan–Lanczos bidiagonalization, builds $B$ one column at a time using only products with $A$ and $A^T$.
It is the basis of the LSQR method for sparse least squares and of methods for a few singular values.
