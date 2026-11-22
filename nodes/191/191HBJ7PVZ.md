---
tag: 191HBJ7PVZ
kind: statement
role: theorem
name: Similar matrices have the same rank, trace, determinant and characteristic and minimal polynomials
aliases: [similarity-invariants]
msc: ["15A21"]
topics: [S6559D61BP]
audience: ug1
about: [0E89HQATM8]
uses: [027KDW2K72, 0EWQEYRVA8, 07PTPSZPME, 0C3CFHDN6R, 039HF58KQ5, 0V58FPM3EQ]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_similarity
    locator: Properties
  - book: isbn:9780134860244
    locator: Section 2.5
---

## Statement

Every number or polynomial that belongs to the map, and not to the basis, is the same for similar matrices.
Let $F$ be a field, and let $A$ and $B$ be $n \times n$ matrices over $F$.
Assume that $B$ is [[similar|027KDW2K72]] to $A$, so that $B = P^{-1}AP$ for an invertible matrix $P$.
Then the following hold.

1. $\operatorname{rank} B = \operatorname{rank} A$, for the [[rank|0EWQEYRVA8]].
2. $\operatorname{tr} B = \operatorname{tr} A$, for the [[trace|07PTPSZPME]].
3. $\det B = \det A$, for the [[determinant|0C3CFHDN6R]].
4. $A$ and $B$ have the same [[characteristic polynomial|039HF58KQ5]], and so the same eigenvalues with the same algebraic multiplicities.
5. $A$ and $B$ have the same [[minimal polynomial|0V58FPM3EQ]].
6. For every polynomial $q \in F[x]$, $q(B) = P^{-1}q(A)P$, so $q(B)$ is similar to $q(A)$ and $\operatorname{rank} q(B) = \operatorname{rank} q(A)$.

## Remarks

### What it gives you

The first use is negative: one differing invariant proves that two matrices are not similar.
Are $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $\begin{pmatrix} 5 & 0 \\ 0 & 0 \end{pmatrix}$ similar?
Both traces are $5$, but the determinants are $1 \cdot 4 - 2 \cdot 3 = -2$ and $0$, so they are not.

The second use is to define invariants of a map.
For an endomorphism $T$ of a finite-dimensional space, the rank, trace, determinant and characteristic and minimal polynomials of $[T]_B$ do not depend on the basis $B$, by the [[change of basis formula|0MQXVZEBMT]].
So they are invariants of $T$, and the [[trace of a linear map|0WCPH5Z7FA]] is defined in exactly this way.

Part 6 gives many more invariants.
For an eigenvalue $\lambda$ and every $k \ge 1$, it gives $\operatorname{rank}(B - \lambda I)^k = \operatorname{rank}(A - \lambda I)^k$, and these ranks count the Jordan blocks of each size.

### Why each hypothesis is needed

The same $P$ must appear on both sides.
For [[equivalent matrices|0CMHSGTWXB]], $B = QAP$ with $Q$ unrelated to $P$, only the rank survives.
For example, $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ are equivalent, since both have rank $1$, but their traces are $1$ and $0$.

The field matters only for the rank and the minimal polynomial.
Parts 2, 3 and 4, and the identity $q(B) = P^{-1}q(A)P$ in part 6, hold over any commutative ring, with the same proofs.
The rank in parts 1 and 6 and the minimal polynomial in part 5 need a field, where they are defined in the usual way.

### The converse

The converse is false: equal invariants do not imply similarity.
The matrices $I_2$ and $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ have the same rank, trace, determinant and characteristic polynomial, but [[they are not similar|62XEH0NYE1]]; only the minimal polynomial tells them apart.
In size $4$, the [[two matrices|J4Q3B9ZNHF]] $J_2(1) \oplus J_2(1)$ and $J_2(1) \oplus I_2$ share all five invariants and are still not similar.
In sizes up to $3$, the characteristic and minimal polynomials together do decide similarity.
In every size, a complete set of invariants is given by the invariant factors, which the rational canonical form records.

### Generalizations

The trace and the determinant are, up to sign, coefficients of the characteristic polynomial:
$$\det(xI - A) = x^n - (\operatorname{tr} A)\, x^{n-1} + \dots + (-1)^n \det A.$$
So parts 2 and 3 also follow from part 4.
Over an algebraically closed field, if $\operatorname{rank} q(A) = \operatorname{rank} q(B)$ for every polynomial $q$, then $A$ and $B$ have the same Jordan normal form, so they are similar.
The [[proof|3C6C60TSQD]] moves the factors $P$ and $P^{-1}$ next to each other in each case.

## Explanations

### L1 human

Similar matrices describe the same linear map in two bases.
So every number that belongs to the map is the same for both matrices.
The rank, the trace and the determinant are such numbers.
For example, $\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$ and $\operatorname{diag}(1, 2)$ are similar, and both have trace $3$ and determinant $2$.

### L2 human

Here is a typical use.
Is $A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$ similar to its transpose $A^{\mathsf{T}} = \begin{pmatrix} 2 & 0 \\ 1 & 2 \end{pmatrix}$?
The invariants agree: both traces are $4$, both determinants are $4$, and both characteristic polynomials are $(x - 2)^2$.
This does not prove similarity, so we look for $P$.
The swap matrix $P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ is its own inverse, and conjugating by it swaps both the rows and the columns:
$$P^{-1}AP = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 2 & 0 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 1 & 2 \end{pmatrix} = A^{\mathsf{T}}.$$
So the answer is yes.
The trap is to stop after the invariants: they can rule out similarity, but they cannot prove it.

### L3 human

The theorem says that these functions on $M_n(F)$ are constant on the orbits of the conjugation action of $GL_n(F)$.
The characteristic polynomial packages $n$ such functions, its coefficients, and over $\mathbb{C}$ they are the elementary symmetric functions of the eigenvalues.
Part 6 gives infinitely many more invariants, the ranks of the matrices $q(A)$.
Over an algebraically closed field, the ranks of $(A - \lambda I)^k$ already determine the Jordan form, and so the similarity class.
