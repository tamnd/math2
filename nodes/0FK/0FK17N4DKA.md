---
tag: 0FK17N4DKA
kind: statement
role: theorem
name: Simultaneous diagonalization
msc: ["15A20", "15A27"]
topics: [Z6S6PWMJPH]
audience: ug2
about: [07SQCNV233]
uses: [0Y17PEKF24, 0Q9PGXD9E4, MX26N71ZD3]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonalizable_matrix
    locator: Simultaneous diagonalization
  - book: isbn:9780135367971
    locator: Section 6.5
  - book: isbn:9783031410253
    locator: Chapter 5
---

## Statement

Several diagonalizable maps can be made diagonal by one and the same basis exactly when they commute with each other.
Let $F$ be a field, let $V$ be a vector space over $F$ of finite dimension $n$, and let $\mathcal{F}$ be a set of [[diagonalizable|07SQCNV233]] endomorphisms of $V$, finite or infinite.
Then the following conditions are equivalent.

1. There is a basis of $V$ in which the matrix of every $T \in \mathcal{F}$ is [[diagonal|044JNC7ZAA]].
2. $S T = T S$ for all $S, T \in \mathcal{F}$.

In matrix form: a set of diagonalizable $n \times n$ matrices over $F$ has one invertible matrix $P$ with $P^{-1} A P$ diagonal for every $A$ in the set if and only if its members [[commute|8G3X8MPG7E]] pairwise.

## Remarks

### Why each hypothesis is needed

Each member must be diagonalizable.
The [[shear|SBDF8APDF7]] $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ commutes with the identity $I$, but no basis makes the shear diagonal, so the pair $\{I, \text{shear}\}$ has no common diagonalizing basis.

The members must commute.
Take $A = \operatorname{diag}(1, 2)$ and $B = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$.
Both are diagonalizable, $B$ because its eigenvalues $1$ and $2$ are distinct.
Multiply in both orders:
$$A B = \begin{pmatrix} 1 & 1 \\ 0 & 4 \end{pmatrix}, \qquad B A = \begin{pmatrix} 1 & 2 \\ 0 & 4 \end{pmatrix}.$$
They differ, so by the theorem no basis makes both diagonal.
Directly: the eigenvectors of $A$ lie on the two axes, and $B e_2 = (1, 2)$ is not on the line of $e_2$.

Finite dimension enters the proof in one place.
It lets us replace an infinite family by finitely many members that span the same space of maps, since that span has dimension at most $n^2$.

### What it gives you

If $S$ and $T$ are commuting diagonalizable maps, then $S + T$, $S T$ and every polynomial in $S$ and $T$ are diagonalizable, because they are diagonal in the common basis.
For example, the difference $S - S'$ of two commuting diagonalizable maps is diagonalizable.
This is the step that proves the uniqueness in the [[Jordan-Chevalley decomposition|011K11VPJN]].
The theorem also says that $V$ is the direct sum of the common eigenspaces
$$V_\alpha = \{ v \in V : T v = \alpha(T) v \text{ for all } T \in \mathcal{F} \},$$
one for each function $\alpha \colon \mathcal{F} \to F$ that occurs.

### The converse and the triangular case

Both directions of the equivalence hold, so the converse is part of the statement: maps that are diagonal in one basis commute, because diagonal matrices commute.
If we drop the hypothesis that each member is diagonalizable, commuting matrices over $\C$ still have something in common.
They can be put in upper triangular form together, by [[simultaneous triangularization|42PG67Q5YN]].

### Generalizations

A commuting family of normal matrices over $\C$ can be diagonalized by one unitary matrix, a form of the spectral theorem.
For a commuting family of semisimple elements of a Lie algebra of matrices over $\C$, the space $V$ splits into [[weight spaces|6FMKG1AB6W]], and this is the starting point of the theory of [[Cartan subalgebras|2TH613KKT5]].
Over a [[perfect field|VWBVKT794W]], the sum of two commuting [[semisimple|08VRX3Q4PB]] maps is semisimple, since both become diagonalizable over the algebraic closure and the theorem applies there.

## History

The theorem is a standard part of a first course in linear algebra.
Hoffman and Kunze, for example, prove it in Section 6.5 together with simultaneous triangularization.

## Explanations

### L1 human

Two matrices can be made diagonal by the same change of axes exactly when they commute.
Then they share the same special directions, and each one only stretches those directions.
For example, a stretch by $2$ along the horizontal axis and a stretch by $5$ along the vertical axis commute, and both are diagonal in the usual axes.
In quantum mechanics, two quantities whose matrices commute share a basis of states in which both have definite values.

### L2 human

Let $A = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$ over $\R$.
First check that they commute:
$$A B = \begin{pmatrix} 3 + 2 & 1 + 6 \\ 6 + 1 & 2 + 3 \end{pmatrix} = \begin{pmatrix} 5 & 7 \\ 7 & 5 \end{pmatrix}, \qquad B A = \begin{pmatrix} 3 + 2 & 6 + 1 \\ 1 + 6 & 2 + 3 \end{pmatrix} = \begin{pmatrix} 5 & 7 \\ 7 & 5 \end{pmatrix}.$$
Now diagonalize the first matrix.
$A$ has the eigenvalues $3$ and $-1$, with the eigenvectors $(1, 1)$ and $(1, -1)$.
Its eigenspaces are lines, and $B$ maps each of them into itself: $B(1, 1) = (4, 4)$ and $B(1, -1) = (2, -2)$.
So with $P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ we get $P^{-1} A P = \operatorname{diag}(3, -1)$ and $P^{-1} B P = \operatorname{diag}(4, 2)$.
The method is to diagonalize one matrix, and then to diagonalize the others inside each of its eigenspaces.
Watch out for repeated eigenvalues: if $A = I$, every basis diagonalizes $A$, and only $B$ can tell you which basis to take.

### L3 human

The theorem says that a commutative subalgebra of $\operatorname{End}(V)$ generated by diagonalizable elements is conjugate to a subalgebra of the diagonal matrices.
For groups, a commuting family of diagonalizable invertible matrices over $F$ lies in a conjugate of the group of invertible diagonal matrices, a split torus.
In analysis, commuting self-adjoint operators on a Hilbert space have a joint spectral decomposition.
The common eigenspaces $V_\alpha$ return as weight spaces in the representation theory of Lie algebras.
