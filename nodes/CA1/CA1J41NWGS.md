---
tag: CA1J41NWGS
kind: definition
name: Schur complement
msc: [15A09, 15A15]
defines: 6HWFBXYPZP
topics: [P8J6QR66TJ]
audience: ug2
uses: [01AXG9KZQF, 0TWTS88TWN, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Schur_complement
  - book: isbn:9780521548236
    locator: Section 0.7
---

## Definition

Let $F$ be a field and let $p, q \ge 1$.
Let $M$ be a $(p + q) \times (p + q)$ [[block matrix|01AXG9KZQF]] over $F$,
$$M = \begin{pmatrix} A & B \\ C & D \end{pmatrix},$$
where $A$ is $p \times p$, $B$ is $p \times q$, $C$ is $q \times p$ and $D$ is $q \times q$.
If $A$ is [[invertible|0TWTS88TWN]], the *Schur complement of $A$ in $M$* is the $q \times q$ matrix
$$M/A = D - C A^{-1} B.$$
If $D$ is invertible, the *Schur complement of $D$ in $M$* is the $p \times p$ matrix
$$M/D = A - B D^{-1} C.$$
The products are [[matrix products|076JGP6R3T]] of blocks.

## Notation

The symbol $M/A$ is due to Haynsworth.
Other books write $S$, $S_A$ or $(M|A)$.
When the block is clear, one says simply "the Schur complement".

## Remarks

Example: let $M = \begin{pmatrix} 2 & 1 \\ 4 & 5 \end{pmatrix}$ with $p = q = 1$ and $A = (2)$.
Then $M/A = 5 - 4 \cdot \tfrac{1}{2} \cdot 1 = 3$, and indeed $\det M = 10 - 4 = 6 = 2 \cdot 3$.

Non-example: for $M = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ and $A = (0)$, the block $A$ is not invertible, so $M/A$ is not defined, although $M$ itself is invertible.
This case is worked in the [[exchange matrix non-example|~74c14e5a]].

The definition comes from the factorisation
$$M = \begin{pmatrix} I_p & 0 \\ C A^{-1} & I_q \end{pmatrix} \begin{pmatrix} A & 0 \\ 0 & M/A \end{pmatrix} \begin{pmatrix} I_p & A^{-1} B \\ 0 & I_q \end{pmatrix},$$
which is proved in the theorem on the [[block inverse formula|~801e2989]].
It gives $\det M = \det A \cdot \det(M/A)$; see [[determinant via the Schur complement|0KA7A4ENVJ]].
In particular, when $A$ is invertible, $M$ is invertible if and only if $M/A$ is invertible.
The same formulas hold over any commutative ring when $A$ is invertible.

The two complements are linked: if $A$, $D$ and $M$ are invertible, then $M/A$ and $M/D$ are invertible as well.
The reason is that $(M/A)^{-1}$ and $(M/D)^{-1}$ are the diagonal blocks of $M^{-1}$.

## Explanations

### L1 human

Split a big matrix into four blocks.
The Schur complement is the lower right block after you clear the lower left block by block elimination.
For a $2 \times 2$ matrix of numbers it is $d - cb/a$.

### L2 human

The order of the factors in $CA^{-1}B$ is forced by the sizes.
$C$ is $q \times p$, $A^{-1}$ is $p \times p$ and $B$ is $p \times q$, so $CA^{-1}B$ is $q \times q$, the size of $D$.
For $M = \begin{pmatrix} 1 & 2 & 0 \\ 3 & 4 & 1 \\ 0 & 1 & 2 \end{pmatrix}$ with $A = (1)$, we get $M/A = \begin{pmatrix} 4 & 1 \\ 1 & 2 \end{pmatrix} - \begin{pmatrix} 3 \\ 0 \end{pmatrix} (2, 0) = \begin{pmatrix} -2 & 1 \\ 1 & 2 \end{pmatrix}$.
Check: $\det M = 1 \cdot (8 - 1) - 2 \cdot (6 - 0) = -5$, and $\det(M/A) = -4 - 1 = -5$.

### L3 human

The definition makes sense over any ring, commutative or not, when $A$ is a unit of the matrix ring.
The Schur complement is the image of $M$ under one step of block Gaussian elimination.
So many identities about it are identities in the group of block triangular matrices.
