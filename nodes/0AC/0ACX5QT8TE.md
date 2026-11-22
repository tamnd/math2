---
tag: 0ACX5QT8TE
kind: concept
name: Invariant subspace
msc: ["15A04", "47A15"]
topics: [Z6S6PWMJPH]
audience: ug1
specializes: [00YC1D652K]
uses: [00YC1D652K, 0J7H0YBFDJ]
sources:
  - url: https://en.wikipedia.org/wiki/Invariant_subspace
    locator: For a single operator
  - book: isbn:9783031410253
    locator: Chapter 5
  - book: isbn:9780135367971
    locator: Section 6.4
same_as:
  wikidata: Q2706744
  wikipedia: Invariant subspace
inventory: [BMJM704BZX]
---

## Summary

An invariant subspace of a linear map is a subspace that the map never leaves.
Once you have one, you can study the map on that smaller piece, and this is how most of the theory of a single linear map is built.
Let $V$ be a [[vector space|000AYPA9AJ]] over a field $F$, and let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]].
A [[subspace|00YC1D652K]] $U$ of $V$ is *invariant* under $T$, or *$T$-invariant*, when
$$T(u) \in U \quad \text{for every } u \in U, \qquad \text{that is,} \qquad T(U) \subseteq U.$$
The [[definition|0EP59ESQ94]] states this formally.
When $V$ has finite dimension, $U$ is invariant exactly when the matrix of $T$ in a basis that starts with a basis of $U$ has a zero block in the lower left corner.

## Motivation

An [[eigenvector|0N6960W0BV]] $v$ is a vector that $T$ only stretches, so the line $Fv$ is an invariant subspace of dimension $1$.
Many maps have too few eigenvectors to describe them, and a rotation of the plane has none at all.
Invariant subspaces of higher dimension fill the gap: they are the pieces into which a map can still be cut when eigenvectors run out.
If $V$ is a [[direct sum|0XYYT5KNTX]] of invariant subspaces, then $T$ acts on each piece separately, and the matrix of $T$ splits into blocks.

The same idea shows up outside linear algebra.
For a system of differential equations $x' = Ax$, a solution that starts in an $A$-invariant subspace stays in it for all time.
Numerical eigenvalue methods split off an invariant subspace and then continue with the smaller matrix that remains, a step called deflation.
Inside linear algebra, invariant subspaces lead to [[triangularization|0363JMQ42Y]], to diagonalization, to the [[primary decomposition|49ZHBMYKVE]] and finally to the [[Jordan normal form|085HQ5G5TE]].

## Notation

Many books say that $U$ is *stable* under $T$, or *$T$-stable*, with the same meaning.
For a family of maps, $U$ is invariant under the family when it is invariant under each member.
In operator theory on infinite-dimensional spaces, "invariant subspace" usually means a *closed* invariant subspace.
In Mathlib, a submodule `U` is invariant under `T` when `U ≤ U.comap T`, and the restricted map is `LinearMap.restrict`.

## Remarks

### A first computation

Take the matrix
$$A = \begin{pmatrix} 1 & 2 & 5 \\ 2 & 1 & 7 \\ 0 & 0 & 4 \end{pmatrix}$$
acting on $\R^3$, and let $U$ be the plane $z = 0$.
A vector of $U$ has the form $(x, y, 0)$, and its image is
$$A (x, y, 0) = (x + 2y, \; 2x + y, \; 0).$$
The third entry is again $0$, so $U$ is invariant.
The line $\R e_3$ is not invariant, because $A e_3 = (5, 7, 4)$ is not a multiple of $e_3$.
Inside $U$, the line through $(1, 1, 0)$ is invariant, since $A(1, 1, 0) = (3, 3, 0)$, and so is the line through $(1, -1, 0)$, since $A(1, -1, 0) = (-1, 1, 0)$.
The [[restriction and quotient of this matrix|D59VWM8NX7]] continue the computation.

### Lines are eigenvectors

The last two lines above were invariant because they were spanned by eigenvectors, and that is the general rule.
For $v \ne 0$, the line $Fv$ is invariant exactly when $T(v) = \lambda v$ for some scalar $\lambda$, which is the definition of an eigenvector.
So invariant lines and eigenvectors are the same thing, and invariant subspaces are the natural extension of eigenvectors to higher dimension.

### Subspaces that every map keeps

Some invariant subspaces come for free.
The subspaces $\{0\}$ and $V$ are invariant under every $T$.
The [[kernel|0S23E6YE83]] is invariant, because $T(u) = 0$ gives $T(T(u)) = T(0) = 0$.
The [[image|0WSFKKT6FF]] is invariant, because $T(T(v))$ is again a value of $T$.
Each [[eigenspace|0G0RFPG8HR]] $E_\lambda$ is invariant, because $T(v) = \lambda v$ lies in $E_\lambda$ when $v$ does.

All of these are cases of one rule: for every polynomial $p$, the [[kernel and the image of $p(T)$ are invariant|8YNE1HTZEP]], and so are sums and intersections of invariant subspaces.
To test a subspace, it is enough to test the vectors of a spanning set, because $T$ is linear and $U$ is closed under linear combinations.

### Two complete lists

For a few maps you can list every invariant subspace.
The [[diagonal matrix with entries 1, 2 and 3|9GVFNZBNE7]] has exactly $8$ invariant subspaces, the spans of the subsets of the standard basis.
The [[derivative on polynomials of degree at most 3|7DGJWWZ8DW]] has exactly $5$, the polynomials of degree less than $k$ for $k = 0, 1, 2, 3, 4$.
Both lists are finite, but a map such as the identity on $\R^2$ has infinitely many, since it keeps every line.

### The matrix in an adapted basis

Let $V$ have dimension $n$ and let $U$ be invariant of dimension $k$.
Choose a basis $u_1, \dots, u_k$ of $U$ and extend it to a basis of $V$.
Each $T(u_i)$ lies in $U$, so it is a combination of $u_1, \dots, u_k$ alone, and the first $k$ columns of the matrix have zeros below row $k$:
$$[T] = \begin{pmatrix} A & B \\ 0 & C \end{pmatrix}.$$
The block $A$ is the matrix of the [[restriction|0KN7EPH7Z0]] of $T$ to $U$, and the [[block triangular form|ENVF51H5S3]] identifies $C$ as well.
When $V = U_1 \oplus \cdots \oplus U_r$ with every $U_i$ invariant, the matrix in a basis built from bases of the $U_i$ is [[block diagonal|001T5FJDC1]].

### What it is not

The [[rotation of the plane by a right angle|XS5H42KEP5]], $R(x, y) = (-y, x)$, has no invariant line over $\R$.
It sends $e_1$ to $e_2$, and more generally it turns every line through $0$ to the perpendicular line.
Over $\C$ the same matrix has the invariant line spanned by $(1, -i)$, since $R(1, -i) = (i, 1) = i\,(1, -i)$.
For the map $T(x, y) = (x, x + y)$, the line $\R e_1$ is not invariant, because $T(e_1) = (1, 1)$; the [[non-example|B448MTVVJW]] shows what breaks.

### Watch out

Invariance asks for $T(U) \subseteq U$, not $T(U) = U$.
For $T(x, y) = (y, 0)$, the line $\R e_1$ is invariant, but $T$ sends it to $\{0\}$.

Over $\R$, an invariant subspace need not contain an eigenvector.
The whole plane is invariant under the rotation $R$, yet no vector in it is a real eigenvector.

An invariant subspace need not have an invariant complement.
For the shear $S(x, y) = (x + y, y)$, the line $\R e_1$ is invariant.
A complement would be a line $\R(a, 1)$, but $S(a, 1) = (a + 1, 1)$ is not a multiple of $(a, 1)$, so no complement is invariant.

### History

For operators on finite-dimensional complex spaces, an invariant line always exists, because every operator has an eigenvector.
For bounded operators on an infinite-dimensional separable complex Hilbert space, the existence of a closed invariant subspace other than $\{0\}$ and the whole space is the [[invariant subspace problem|5RF055GK4N]].
Per Enflo constructed an operator on a Banach space with no such subspace, so the question is about Hilbert spaces.

### Try it

First, is the line through $(1, 2)$ invariant under $\begin{pmatrix} 1 & 1 \\ 4 & 1 \end{pmatrix}$?
Yes: the matrix sends $(1, 2)$ to $(3, 6) = 3\,(1, 2)$.

Second, is the plane $x + y + z = 0$ invariant under $T(x, y, z) = (z, x, y)$?
Yes: $T$ only permutes the entries, so the sum of the entries of $T(v)$ equals the sum for $v$, and that sum stays $0$.

## Explanations

### L1 human

A map moves the points of a space around.
A subspace is invariant when the map never moves one of its points out of it.
Think of the map of the plane that doubles every horizontal arrow and triples every vertical arrow.
The horizontal axis is invariant, since a horizontal arrow stays horizontal.
The line at 45 degrees is not invariant, since the arrow to $(1, 1)$ goes to $(2, 3)$, which is off that line.

### L2 human

Here is a typical problem: find every invariant subspace of $A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}$ on $\R^2$.
The subspaces $\{0\}$ and $\R^2$ are invariant, so only lines are in question, and invariant lines are spanned by eigenvectors.
The eigenvalues are the diagonal entries $2$ and $3$, because the matrix is triangular.
For $\lambda = 2$ the eigenvector is $e_1$, and for $\lambda = 3$ we solve $(A - 3I)v = 0$:
$$\begin{pmatrix} -1 & 1 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = 0 \quad \Longrightarrow \quad x = y.$$
Check: $A(1, 1) = (3, 3)$.
Each eigenspace is a single line, so the invariant subspaces are exactly $\{0\}$, $\R e_1$, $\R(1, 1)$ and $\R^2$.
In the basis $e_1, (1, 1)$ both basis lines are invariant, so the matrix becomes $\operatorname{diag}(2, 3)$.
This is the typical use: find invariant pieces, then choose a basis adapted to them so that the matrix becomes simple.

### L3 human

An endomorphism $T$ makes $V$ a module over the polynomial ring $F[x]$, with $x$ acting as $T$.
The $T$-invariant subspaces are exactly the $F[x]$-submodules, and the decomposition theorems of the sub-area become the structure theory of finitely generated torsion modules over a principal ideal domain, treated with the [[canonical forms|GEBYZKYV3D]].
For a family of maps, the common invariant subspaces are the submodules over the algebra that the family generates.
Burnside's theorem says that over an algebraically closed field, an algebra of $n \times n$ matrices with no common invariant subspace except $\{0\}$ and $F^n$ is the full matrix algebra.
In analysis, the [[invariant subspace problem|5RF055GK4N]] asks the same kind of question for bounded operators on Hilbert space.
