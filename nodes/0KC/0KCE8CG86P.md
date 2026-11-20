---
tag: 0KCE8CG86P
kind: concept
name: Idempotent matrix
aliases: [projection-matrix]
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
specializes: [0JXZKX526R]
uses: [0JXZKX526R, 032Q9FB8MT]
sources:
  - url: https://en.wikipedia.org/wiki/Idempotent_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Idempotent_matrix
    locator: Properties
same_as:
  wikidata: Q3751720
  wikipedia: Idempotent matrix
inventory: [DMB0JAP9ZR]
---

## Summary

An idempotent matrix is a [[square matrix|0JXZKX526R]] $P$ with $P^2 = P$; the [[formal definition|0K7TD9BV2D]] states it over any ring.
Over a field, the idempotent matrices are exactly the matrices of [[projections|033DA1WE8Y]]: $P$ maps onto its image and kills its kernel, and $V = \operatorname{im} P \oplus \ker P$.
Their eigenvalues lie in $\{0, 1\}$, and over a field of characteristic $0$ their trace equals their rank.

## Motivation

Projections are the first tool for splitting a space into two parts.
Least squares, orthogonal decompositions and the spectral theorem all use idempotent matrices.
In the [[matrix ring|~de637a64]], idempotents play the role that $0$ and $1$ play in a field: $P$ and $I - P$ split $I$ into two parts with $P(I - P) = 0$.

## Notation

- An idempotent matrix is also called a *projection matrix*. Some books reserve this name for the [[symmetric|0VR671PHE5]] idempotents, the orthogonal projections.
- In Mathlib the condition is written `IsIdempotentElem P`, which means `P * P = P`.

## Remarks

### Examples

- [[An oblique projection of the plane onto a line|~67b706ca]].
- [[The orthogonal projection onto the line spanned by (1, 1)|~682250bb]].
- [[The matrix E₁₁, whose powers never reach the identity|5VEW97EQR6]].
- $0$ and $I$ are idempotent, and so is every diagonal matrix with entries in $\{0, 1\}$.

### Non-examples

- [[A matrix with eigenvalues in {0, 1} that is not idempotent|~49c9a6f7]].
- $2I$ is not idempotent, because $(2I)^2 = 4I$.

### Basic properties

Let $P$ be an idempotent $n \times n$ matrix.

- $I - P$ is idempotent, because $(I - P)^2 = I - 2P + P^2 = I - P$.
- $P(I - P) = (I - P)P = 0$.
- $P^k = P$ for each $k \ge 1$.
- If $P$ is [[invertible|0EB9N0S33C]], then $P = P^{-1} P^2 = P^{-1} P = I$. So $I$ is the only invertible idempotent.
- Over a field, every eigenvalue $\lambda$ of $P$ is $0$ or $1$. If $Pv = \lambda v$ with $v \neq 0$, then $\lambda v = P v = P^2 v = \lambda^2 v$, so $\lambda^2 = \lambda$.
- Over a field, $\operatorname{im} P$ is the set of vectors with $Pv = v$, and $V = \operatorname{im} P \oplus \ker P$, because $v = Pv + (v - Pv)$.
- Over a field, $\operatorname{tr} P = \operatorname{rank} P \cdot 1$. The proof uses a basis adapted to $\operatorname{im} P \oplus \ker P$, in which $P = \operatorname{diag}(I_r, 0)$; see [[projection|033DA1WE8Y]] and [[rank|0ZC9YTXZRY]].
- Outside characteristic $2$, $P$ is idempotent if and only if $2P - I$ is [[involutory|~c8443172]].

### Common errors

- Assuming that an idempotent matrix is symmetric. That holds only for orthogonal projections.
- Taking eigenvalues in $\{0, 1\}$ as enough. The matrix must also be diagonalizable.

## Explanations

### L1 human

An idempotent matrix does nothing new when we apply it twice.
A projection onto a line is the main example: once a point is on the line, projecting again keeps it there.

### L2 human

The equation $P^2 = P$ says that $P$ is the identity on its own image.
So $P$ splits each vector into a part in the image, which it keeps, and a part in the kernel, which it kills.
The choice of the kernel decides whether the projection is orthogonal or oblique.

### L3 human

Over a field, $P$ is idempotent if and only if its minimal polynomial divides $x^2 - x$, which has distinct roots.
So $P$ is diagonalizable, and $P$ is similar to $\operatorname{diag}(I_r, 0)$ with $r = \operatorname{rank} P$.
In ring theory, idempotents correspond to decompositions of a module into direct summands.
