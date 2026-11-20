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

Let $V$ be a [[vector space|000AYPA9AJ]] over a field $F$, and let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]].
A [[subspace|00YC1D652K]] $U$ of $V$ is *invariant* under $T$, or *$T$-invariant*, when $T(u) \in U$ for every $u \in U$, that is, when $T(U) \subseteq U$.
Invariant subspaces are the pieces into which a linear map can be cut, so they reduce the study of $T$ to the study of smaller maps.

## Motivation

A linear map on a large space is hard to understand as a whole.
If $T$ keeps a subspace $U$ inside itself, then $T$ is also a map from $U$ to $U$, and we can study this smaller map first.
The simplest case is a line $Fv$: it is invariant exactly when $v$ is an [[eigenvector|0N6960W0BV]].
So invariant subspaces generalize eigenvectors from dimension $1$ to any dimension.
When $V$ is a [[direct sum|0XYYT5KNTX]] of invariant subspaces, the map $T$ is the sum of independent maps on the pieces.
This idea leads to diagonalization, triangularization and the canonical forms of later sub-areas.

## Notation

Some books write "$U$ is stable under $T$" or "$U$ is $T$-stable" for the same notion.
In operator theory, "invariant subspace" often means a closed invariant subspace of a Banach or Hilbert space.
In Mathlib, a submodule `U` is invariant under `T` when `U ≤ U.comap T`, and the restriction is `LinearMap.restrict`.

## Remarks

### Examples

- The subspaces $\{0\}$ and $V$ are invariant under every $T$, since $T(0) = 0$ and $T(V) \subseteq V$.
- The [[kernel|0S23E6YE83]] and the [[image|0WSFKKT6FF]] of $T$ are invariant: if $T(u) = 0$, then $T(T(u)) = 0$, and $T(T(v))$ lies in $\im T$.
- Each [[eigenspace|0G0RFPG8HR]] $E_\lambda = \ker(T - \lambda \id_V)$ is invariant, since $T(v) = \lambda v$ lies in $E_\lambda$ for $v \in E_\lambda$.
- For the [[derivative on polynomials|7DGJWWZ8DW]], the polynomials of degree less than $k$ form an invariant subspace, since the derivative lowers the degree.
- For a [[diagonal matrix with distinct entries|9GVFNZBNE7]], the invariant subspaces are exactly the spans of sets of standard basis vectors.

### Non-examples

- For the [[rotation of the plane by a right angle|XS5H42KEP5]], no line through $0$ is invariant over $\R$. The line $\R e_1$ is sent to the line $\R e_2$.
- For the shear $T(x, y) = (x + y, y)$, the line $\R e_2$ is not invariant, since $T(e_2) = e_1 + e_2$ does not lie on it.

### Basic properties

- The [[kernel and the image of each polynomial in $T$ are invariant|8YNE1HTZEP]], and so are sums and intersections of invariant subspaces.
- If $U$ is invariant and $V$ is finite-dimensional, then in a basis of $V$ that extends a basis of $U$, the [[matrix|0YQSGNYE3K]] of $T$ is block upper triangular, see [[restriction and quotient operators|0KN7EPH7Z0]].
- If $V = U_1 \oplus \cdots \oplus U_k$ with each $U_i$ invariant, then the matrix of $T$ in an adapted basis is [[block diagonal|001T5FJDC1]].
- A line $Fv$ with $v \ne 0$ is invariant if and only if $v$ is an eigenvector of $T$.
- If $ST = TS$, then each eigenspace and each kernel of $S$ is invariant under $T$, because $S(T(v)) = T(S(v))$.

### History

Invariant subspaces appear implicitly in the nineteenth century work of Jordan and Frobenius on the reduction of matrices.
In the abstract form, they became central in the module theory of the 1920s, where an invariant subspace of $T$ is a submodule over $F[x]$.
The [[invariant subspace problem|5RF055GK4N]] for bounded operators on Hilbert space is still open.

### Common errors

- Confusing $T(U) \subseteq U$ with $T(U) = U$. The kernel of a nonzero nilpotent map is invariant, but $T$ sends it to $\{0\}$.
- Thinking that each vector of an invariant subspace is an eigenvector. A plane can be invariant while it contains no eigenvector, as for a rotation of $\R^2$.
- Assuming that an invariant subspace has an invariant complement. For the shear $T(x, y) = (x + y, y)$, the line $\R e_1$ is invariant and has no invariant complement.

## Explanations

### L1 human

A map moves the points of a space around.
A subspace is invariant when the map never moves a point of it out of it.
Think of a stretch of the plane that doubles every horizontal arrow and triples every vertical arrow.
The horizontal axis is invariant, since a horizontal arrow stays horizontal.
The line at 45 degrees is not invariant, since the arrow from $0$ to $(1, 1)$ goes to $(2, 3)$.

### L2 human

Let $A = \begin{pmatrix} 1 & 2 & 5 \\ 2 & 1 & 7 \\ 0 & 0 & 4 \end{pmatrix}$ act on $\R^3$, and let $U$ be the plane $z = 0$.

1. A vector of $U$ is $(x, y, 0)$.
2. Its image is $A(x, y, 0) = (x + 2y, 2x + y, 0)$.
3. The third coordinate is $0$, so the image lies in $U$, and $U$ is invariant.
4. The line $\R e_3$ is not invariant, since $A e_3 = (5, 7, 4)$.

The typical use is to choose a basis that starts with a basis of $U$, so that the matrix becomes block triangular.
The trap is to read invariance from the matrix in a basis that is not adapted to $U$, where the zero block is not visible.

### L3 human

An endomorphism $T$ of $V$ makes $V$ a module over the polynomial ring $F[x]$, with $x$ acting as $T$.
The $T$-invariant subspaces are exactly the $F[x]$-submodules of this module.
Under this dictionary, the decomposition theorems of this sub-area are the structure theory of finitely generated torsion modules over a principal ideal domain, treated in the sub-area on canonical forms.
For a family of operators, the common invariant subspaces are the submodules over the algebra that the family generates.
Burnside's theorem says that an algebra of matrices over an algebraically closed field with no common invariant subspace other than $0$ and $V$ is the full matrix algebra.
In operator theory, the existence of nontrivial closed invariant subspaces for every bounded operator on a Hilbert space is the open [[invariant subspace problem|5RF055GK4N]].
