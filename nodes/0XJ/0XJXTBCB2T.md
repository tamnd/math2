---
tag: 0XJXTBCB2T
kind: concept
name: Orthogonal complement
msc: [15A63, 46C05]
topics: [8GQVME4SZZ]
audience: ug1
specializes: [00YC1D652K]
uses: [0NB0AWGJBW, 0Y2X7P2WB7, 00YC1D652K]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_complement
    locator: Inner product spaces
  - book: isbn:9783031410253
    locator: Section 6C
  - book: isbn:9780134860244
    locator: Section 6.2
  - book: isbn:9780321982384
    locator: Section 6.1
same_as:
  wikidata: Q1780921
  wikipedia: Orthogonal complement
inventory: [G20Z36F7VP]
---

## Summary

Let $V$ be an [[inner product space|0QVNCJXRY3]] over $\R$ or $\C$, and let $S$ be a subset of $V$.
The *orthogonal complement* of $S$ is the set $S^\perp$ of all $v \in V$ with $\ip{v}{s} = 0$ for every $s \in S$.
So $S^\perp$ holds exactly the vectors that are [[orthogonal|0Y2X7P2WB7]] to each vector of $S$.
The set $S^\perp$ is always a [[linear subspace|00YC1D652K]], even when $S$ is not, and the precise statement is in the [[definition|079D68S3AW]].
Orthogonal complements turn the geometry of right angles into linear algebra: the normal line of a plane, the null space of a matrix and the error of a best approximation are all orthogonal complements.

## Motivation

In $\R^3$ a plane through $0$ is fixed by its normal vector $n$, because the plane is the set of $x$ with $n \cdot x = 0$.
Conversely, the normal line is the set of vectors at right angles to every vector of the plane.
So a plane and its normal line determine each other.
The orthogonal complement makes this relation exact in every inner product space and for subspaces of every dimension.
It also explains a fact about matrices: the solutions of $Ax = 0$ are the vectors orthogonal to every row of $A$.
Projections, [[least squares|0BYTQ4X1HC]] and the [[best approximation theorem|0MCDDSCB9Z]] all start from the splitting of a space into a subspace and its orthogonal complement.

## Notation

We write $U^\perp$ and read it "$U$ perp".
For a single vector we write $v^\perp$ for $\set{v}^\perp$.
Some books write $U^\circ$ or $U^0$, but this site keeps $U^0$ for the [[annihilator|0ASHNYF7AG]] in the dual space $V^*$.
In Mathlib the orthogonal complement of `U : Submodule 𝕜 E` is `Uᗮ`, defined as `Submodule.orthogonal`.

## Remarks

### Examples

1. [[The orthogonal complement of a plane in R3|~f9f46f63]]: the plane spanned by $(1, 1, 0)$ and $(0, 1, 1)$ has the complement $\R(1, -1, 1)$, found as a null space.
2. [[The sum rule for two lines in R3|~5f8ab60c]]: for $U = \R(1, 1, 0)$ and $W = \R(0, 1, 1)$, the intersection $U^\perp \cap W^\perp$ is the line $(U + W)^\perp = \R(1, -1, 1)$.
3. In $\R^n$ with the [[dot product|0S52TNNTH9]], the complement of the span of $e_1, \dots, e_k$ is the span of $e_{k+1}, \dots, e_n$, since $x \cdot e_i = x_i$.
4. For a real $m \times n$ matrix $A$, the [[null space|0PHDYNR24D]] of $A$ is the complement of its [[row space|069MCGX635]], because entry $i$ of $Ax$ is the dot product of row $i$ with $x$.
5. In the space of real polynomials of degree at most $2$ with $\ip{f}{g} = \int_{-1}^{1} f g \, dx$, the complement of the constants is the set of $p$ with $\int_{-1}^{1} p \, dx = 0$. It contains $x$ and $3x^2 - 1$.

### Non-examples

1. [[A complement that is not orthogonal|~08979893]]: in $\R^2$, the line $\R(1, 1)$ is a complement of the $x$-axis in the sense of direct sums, but its vectors are not orthogonal to $(1, 0)$.
2. The set difference $\R^3 \setminus U$ of a plane $U$ is not $U^\perp$: it does not contain $0$, so it is not a subspace.
3. The [[annihilator|0ASHNYF7AG]] $U^0$ lives in the dual space $V^*$ and needs no inner product, so it is not a subset of $V$; [[the example in the duality sub-area|ENNMQ30X9F]] compares the two.

### Basic properties

The [[basic properties of the orthogonal complement|~2c397fab]] hold for every subset $S$ and all subspaces $U$, $W$ of any inner product space:

- $S^\perp$ is a subspace, and $S^\perp = (\operatorname{span} S)^\perp$.
- $U \cap U^\perp = \set{0}$.
- $S \subseteq T$ implies $T^\perp \subseteq S^\perp$.
- $(U + W)^\perp = U^\perp \cap W^\perp$, the sum rule.
- $\set{0}^\perp = V$ and $V^\perp = \set{0}$.

For a finite-dimensional $U$, the [[orthogonal decomposition|0SP7P0G7KQ]] gives $V = U \oplus U^\perp$.
In a finite-dimensional $V$, it gives $\dim U^\perp = \dim V - \dim U$, and the [[double orthogonal complement|0PXN9G4MX1]] satisfies $(U^\perp)^\perp = U$.
For matrices, the [[orthogonality of the fundamental subspaces|~b3a6e0d4]] gives $\operatorname{Row}(A) = \operatorname{Nul}(A)^\perp$ and $\operatorname{Col}(A) = \operatorname{Nul}(A^{\mathsf{T}})^\perp$.

### History

The term "orthogonal complement" and the symbol $\perp$ are standard in the textbooks of Axler, Friedberg, Insel and Spence, and Lay that we cite.
The notion grew with the theory of Hilbert spaces, where complements of closed subspaces give the projection theorem.

### Common errors

- Confusing the orthogonal complement with a complementary subspace. A subspace has many complements, but only one orthogonal complement.
- Testing $v \in U^\perp$ against a few vectors of $U$ that do not span $U$. It is enough to test a spanning set, but the spanning set must span all of $U$.
- Assuming $(U^\perp)^\perp = U$ in every space. It fails for [[non-closed subspaces of an infinite-dimensional space|~52588f49]].

## Explanations

### L1 human

Take a flat sheet of paper through a point, and a pencil standing straight up from it.
Every direction in the sheet is at a right angle to the pencil.
The orthogonal complement of the sheet is the line of the pencil.
In the same way, the orthogonal complement of the pencil line is the whole sheet.
For the floor $z = 0$ in space, the orthogonal complement is the vertical axis.

### L2 human

We find the orthogonal complement of $U = \operatorname{span}\set{(1, 1, 0), (0, 1, 1)}$ in $\R^3$.

1. A vector $x$ is in $U^\perp$ exactly when it is orthogonal to both spanning vectors, by the property $S^\perp = (\operatorname{span} S)^\perp$.
2. This gives the linear system $x_1 + x_2 = 0$ and $x_2 + x_3 = 0$.
3. So $U^\perp$ is the null space of $A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$, the matrix with the spanning vectors as rows.
4. With $x_3 = t$ free, we get $x_2 = -t$ and $x_1 = t$.
5. Hence $U^\perp = \R(1, -1, 1)$, and $\dim U + \dim U^\perp = 2 + 1 = 3$.

This method computes every orthogonal complement in $\R^n$: put a spanning set of $U$ into the rows of a matrix and solve $Ax = 0$.
The trap is to put the spanning vectors into the columns, which computes the left null space instead.

### L3 human

Over any field, the bilinear pairing $x^{\mathsf{T}} y$ on $F^n$ gives a set $\set{x : x^{\mathsf{T}} u = 0 \text{ for all } u \in U}$, and it is the image of the annihilator $U^0$ under the identification of $F^n$ with its dual.
An inner product is needed for this set to be a complement: positivity gives $U \cap U^\perp = \set{0}$.
For an indefinite form, such as the Minkowski form, a nonzero vector can be orthogonal to itself, and $U \cap U^\perp$ can be nonzero; this is the start of the theory of [[bilinear forms|0SQZMXB6GP]].
In a Hilbert space, $U^\perp$ is always closed, and $(U^\perp)^\perp$ is the closure of $U$.
The later sub-areas use the complement for the kernel and image of the [[adjoint|0R9NMSM1ZP]], $\ker T^* = (\im T)^\perp$, and for the invariant subspaces of normal operators in the spectral theorem.
