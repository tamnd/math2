---
tag: 0MQXVZEBMT
kind: statement
role: theorem
name: Change of basis formula
msc: ["15A04"]
topics: [S6559D61BP]
audience: ug1
about: [0YQSGNYE3K, 0MKRHZB3WS]
uses: [0KWXYZPJKN, 0YYMY95FWS]
sources:
  - url: https://en.wikipedia.org/wiki/Change_of_basis
    locator: Endomorphisms
  - book: isbn:9780134860244
    locator: Section 2.5
---

## Statement

When the bases change, coordinates change by the inverse of the change of basis matrix, and the matrix of a linear map is multiplied by change of basis matrices on both sides.
Let $F$ be a field and let $V$ and $W$ be finite-dimensional vector spaces over $F$.
Let $B$ and $B'$ be ordered bases of $V$, and let $C$ and $C'$ be ordered bases of $W$.
Let $P$ be the [[change of basis matrix|0MKRHZB3WS]] from $B$ to $B'$, and let $Q$ be the change of basis matrix from $C$ to $C'$.

1. For each $v \in V$, $[v]_B = P[v]_{B'}$; the matrix $P$ is invertible, and $[v]_{B'} = P^{-1}[v]_B$.
2. For each linear map $T \colon V \to W$, the [[matrices of T|0YQSGNYE3K]] in the two pairs of bases satisfy
   $$[T]_{C',B'} = Q^{-1}\, [T]_{C,B}\, P.$$
3. For each linear map $T \colon V \to V$, with $C = B$ and $C' = B'$,
   $$[T]_{B'} = P^{-1}\, [T]_B\, P.$$

## Remarks

### How to read the formula

Read $Q^{-1}[T]_{C,B}P$ from right to left, as a path for coordinates.
The factor $P$ turns $B'$-coordinates of the input into $B$-coordinates.
The factor $[T]_{C,B}$ applies $T$ in the old bases and returns $C$-coordinates.
The factor $Q^{-1}$ turns those into $C'$-coordinates.
So the product takes new coordinates of $v$ to new coordinates of $T(v)$, which is the job of $[T]_{C',B'}$.

### A worked use

Let $T(x, y) = (2x + y, x + 2y)$ on $\mathbb{R}^2$, with the standard basis $E$ and the new basis $B' = ((1, 1), (1, -1))$.
Here $[T]_E = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, $P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ and $P^{-1} = \tfrac12 P$.
Multiply first by $P$ on the right, then by $P^{-1}$ on the left:
$$[T]_E P = \begin{pmatrix} 3 & 1 \\ 3 & -1 \end{pmatrix}, \qquad P^{-1}[T]_E P = \frac12 \begin{pmatrix} 6 & 0 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}.$$
Check: $T(1, 1) = (3, 3) = 3(1, 1)$ and $T(1, -1) = (1, -1)$, so the [[direct computation|7HRGTM3RKJ]] gives the same diagonal matrix.
For a map between two different spaces, the [[derivative on quadratic polynomials|ZB8X1EHNJW]] uses both $P$ and $Q$.

### Why each hypothesis is needed

The spaces must be finite-dimensional so that finite bases exist and the matrices are defined.
The bases must be ordered, because a reordering permutes the rows or the columns of every matrix in the formula.
In part 2 the changes in the domain and in the target are independent, so two matrices $P$ and $Q$ appear.
Part 3 is the special case of one space with one change of basis, where $Q = P$.
If you change the basis only on one side, keep only that factor: with $B'$ and $C$, the matrix is $[T]_{C,B}P$.

### What it gives you

For endomorphisms, part 3 says that the matrices of one map in two bases are [[similar|0E89HQATM8]].
So every quantity that similar matrices share, such as the trace and the determinant, is a property of the map itself; the [[trace of a linear map|0WCPH5Z7FA]] uses exactly this.
For maps between two spaces, part 2 says that the two matrices are [[equivalent|0CMHSGTWXB]].
Part 1 says that coordinates move by $P^{-1}$ while basis vectors move by $P$, which is why coordinates are called contravariant.

### The converse

The converse holds.
For each invertible $n \times n$ matrix $P$, the vectors $b'_j = \sum_i p_{ij} b_i$ form a basis $B'$, and its change of basis matrix is $P$.
So every matrix similar to $[T]_B$ is the matrix of $T$ in some basis, and every matrix $Q^{-1}[T]_{C,B}P$ with $P$ and $Q$ invertible is the matrix of $T$ in some pair of bases.

### Watch out

Books define the change of basis matrix in two opposite directions.
With the other convention, the matrix that the book calls $P$ is our $P^{-1}$, and part 3 reads $[T]_{B'} = P[T]_B P^{-1}$.
Both forms are correct for their own convention, and mixing them gives a wrong answer.
In the worked use, $P[T]_E P^{-1}$ happens to give the same diagonal matrix because $P^{-1} = \tfrac12 P$, so test a convention on an example where $P^{-1}$ is not a multiple of $P$.
Mathlib's `LinearMap.toMatrix` puts the coordinates of the images of the domain basis in the columns, as we do.

### Generalizations

The formula is the theorem on the [[matrix of a composition|05Q1B7MH0M]] applied to $T = \mathrm{id}_W \circ T \circ \mathrm{id}_V$, since $P = [\mathrm{id}_V]_{B, B'}$ and $Q^{-1} = [\mathrm{id}_W]_{C', C}$.
A bilinear form changes by a different rule, $P^{\mathsf{T}} M P$, as the [[change of basis for a bilinear form|0SPYAGE7T0]] shows.
The two rules agree when $P$ is orthogonal, since then $P^{\mathsf{T}} = P^{-1}$.

## History

The formula has no single author.
It follows in one line from the product rule for matrices of compositions, and textbooks such as Friedberg, Insel and Spence present it together with the change of coordinate matrix.

## Explanations

### L1 human

When you change the bases, the matrix of a linear map changes in a fixed way.
Translate the input from the new to the old coordinates, apply the old matrix, and translate the result back to the new coordinates.
Those three steps are the three factors of $Q^{-1}AP$.
For the map $(x, y) \mapsto (2x + y, x + 2y)$, the basis $(1, 1)$, $(1, -1)$ turns the matrix into $\operatorname{diag}(3, 1)$.

### L2 human

Here is a typical check of the coordinate rule in part 1.
In $\mathbb{R}^2$ with $B' = ((1, 2), (1, 3))$ we have $P = \begin{pmatrix} 1 & 1 \\ 2 & 3 \end{pmatrix}$ and $P^{-1} = \begin{pmatrix} 3 & -1 \\ -2 & 1 \end{pmatrix}$.
The vector $v = (4, 9)$ has new coordinates
$$P^{-1}\begin{pmatrix} 4 \\ 9 \end{pmatrix} = \begin{pmatrix} 3 \\ 1 \end{pmatrix},$$
and indeed $3(1, 2) + (1, 3) = (4, 9)$.
The typical use of part 3 is to choose $B'$ so that $P^{-1}AP$ is diagonal, which the sub-area on [[eigenvalues|6R1D6QPY3S]] does in general.
The trap is the direction: new coordinates come from old ones through $P^{-1}$, not through $P$.

### L3 human

The formula says that $T \mapsto [T]_{C,B}$ is equivariant for the action of $GL_m(F) \times GL_n(F)$, which acts on pairs of bases and on $m \times n$ matrices by $(Q, P) \cdot A = Q^{-1}AP$.
The orbits of this action on matrices are the rank classes, and the orbits of the conjugation action $A \mapsto P^{-1}AP$ on square matrices are the similarity classes.
So classifying linear maps up to a choice of bases is the same as classifying matrices up to these actions, and the rational and Jordan canonical forms solve the problem for endomorphisms.
