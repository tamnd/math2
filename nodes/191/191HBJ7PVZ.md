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

Let $F$ be a field, and let $A$ and $B$ be $n \times n$ matrices over $F$.
Assume that $B$ is [[similar|027KDW2K72]] to $A$, so $B = P^{-1} A P$ for an invertible matrix $P$.
Then:

1. $\rank B = \rank A$, for the [[rank|0EWQEYRVA8]];
2. $\tr B = \tr A$, for the [[trace|07PTPSZPME]];
3. $\det B = \det A$, for the [[determinant|0C3CFHDN6R]];
4. $A$ and $B$ have the same [[characteristic polynomial|039HF58KQ5]], and so the same eigenvalues with the same algebraic multiplicities;
5. $A$ and $B$ have the same [[minimal polynomial|0V58FPM3EQ]];
6. for every polynomial $q \in F[x]$, $q(B) = P^{-1} q(A) P$, so $q(B)$ is similar to $q(A)$ and $\rank q(B) = \rank q(A)$.

## Remarks

### Why each hypothesis is needed

- The same $P$ must appear on both sides. For [[equivalent matrices|0CMHSGTWXB]] $B = QAP$ with $Q \ne P^{-1}$, only the rank is preserved.
  For example, $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ are equivalent, with traces $1$ and $0$.
- Parts 2, 3 and 4 hold over any commutative ring, with the same proofs. Part 5 uses a field, where the minimal polynomial is defined.

### Consequences

- Each of these quantities is defined for an endomorphism $T$ of a finite-dimensional space, through any matrix $[T]_B$. The value does not depend on $B$.
- For an eigenvalue $\lambda$ and every $k \ge 1$, $\rank (B - \lambda I)^k = \rank (A - \lambda I)^k$, by part 6. These ranks count the Jordan blocks.
- A matrix with two different traces in two bases is impossible. So a quick trace check can rule out a proposed similarity.

### Converse

The converse is false: equal invariants do not imply similarity.
- $I_2$ and $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ have the same rank, trace, determinant and characteristic polynomial, but [[they are not similar|62XEH0NYE1]].
- The [[two $4 \times 4$ matrices|J4Q3B9ZNHF]] $J_2(1) \oplus J_2(1)$ and $J_2(1) \oplus I_2$ share all five invariants, but they are not similar.
For $n \le 3$, the characteristic and minimal polynomials together decide similarity.
A complete set of invariants in every size is given by the invariant factors.

### Generalizations

- If $q(A)$ and $q(B)$ have the same rank for every polynomial $q$, and $F$ is algebraically closed, then $A$ and $B$ have the same Jordan normal form, so they are similar.
- The trace and the determinant are, up to sign, coefficients of the characteristic polynomial: $\det(xI - A) = x^n - (\tr A) x^{n-1} + \dots + (-1)^n \det A$. So parts 2 and 3 also follow from part 4.

## History

These invariants are classical.
Their failure to classify matrices led to the Jordan normal form and the theory of invariant factors.

## Explanations

### L1 human

Similar matrices describe the same linear map in two bases.
So every number that belongs to the map is the same for both matrices.
The rank, trace and determinant are such numbers.

### L2 human

Each part follows from one rule.
The rank uses $\rank(XY) \le \min(\rank X, \rank Y)$, the trace uses $\tr(XY) = \tr(YX)$, and the determinant uses $\det(XY) = \det X \det Y$.
The minimal polynomial uses $q(P^{-1} A P) = P^{-1} q(A) P$.

### L3 human

The theorem says that these functions on $M_n(F)$ are constant on the orbits of the conjugation action of $GL_n(F)$.
Part 6 gives infinitely many more invariants, the ranks of $q(A)$.
Over an algebraically closed field, the ranks of $(A - \lambda I)^k$ already determine the Jordan form, and so the class.
