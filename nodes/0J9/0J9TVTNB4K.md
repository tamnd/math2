---
tag: 0J9TVTNB4K
kind: statement
role: proposition
name: Determinant of a block triangular matrix
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
about: [00KDZRW4C0]
uses: [0C3CFHDN6R, 01AXG9KZQF]
sources:
  - url: https://en.wikipedia.org/wiki/Block_matrix
    locator: Determinant
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Block matrices
---

## Statement

When a square matrix has a block of zeros below its two square diagonal blocks, its determinant is the product of the determinants of those blocks.
Let $K$ be a commutative ring, and let $m, n \ge 1$.
Let $A$ be an $m \times m$ matrix, $B$ an $m \times n$ matrix and $D$ an $n \times n$ matrix over $K$.
Then the [[block matrix|01AXG9KZQF]] satisfies
$$\det \begin{pmatrix} A & B \\ 0 & D \end{pmatrix} = \det A \cdot \det D,$$
where $0$ is the $n \times m$ zero matrix and $\det$ is the [[determinant|0C3CFHDN6R]].
The same holds for the lower block triangular matrix $\begin{pmatrix} A & 0 \\ C & D \end{pmatrix}$, for every $n \times m$ matrix $C$.

## Remarks

### A first computation

Take the $4 \times 4$ matrix
$$M = \begin{pmatrix} 1 & 2 & 5 & 6 \\ 3 & 4 & 7 & 8 \\ 0 & 0 & 2 & 1 \\ 0 & 0 & 1 & 3 \end{pmatrix}, \qquad A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \qquad D = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}.$$
The two diagonal blocks have $\det A = 4 - 6 = -2$ and $\det D = 6 - 1 = 5$, so the rule gives
$$\det M = (-2) \cdot 5 = -10.$$
The block $B$ in the upper right corner plays no part.
Check by row reduction: subtracting $3$ times row 1 from row 2 gives the pivots $1$ and $-2$ in the first two columns.
Subtracting $\tfrac12$ of row 3 from row 4 gives the pivots $2$ and $\tfrac52$ in the last two columns.
The product of the pivots is $1 \cdot (-2) \cdot 2 \cdot \tfrac52 = -10$.

### Where the rule comes from

The [[determinant of a triangular matrix|0K1KKMFHYH]] is the product of its diagonal entries.
The block rule is the same statement with the entries replaced by square blocks.
In the [[proof by the Leibniz formula|92GVP9180G]], the zero block kills every term whose permutation sends a lower row to a left column.
The surviving permutations split into a permutation of the first $m$ indices and one of the last $n$, and the sum factors.
The lower block triangular case follows from the upper one by the [[determinant of the transpose|0ZZQ2E1MTE]].

### Why the blocks must be square and the zero block off the diagonal

The rule speaks of $\det A$ and $\det D$, so the diagonal blocks must be square.
The zero block must also sit in a corner off the diagonal.
For square blocks $B$ and $C$ of size $n$, the matrix $\begin{pmatrix} 0 & B \\ C & 0 \end{pmatrix}$ has zero diagonal blocks.
Moving each of the last $n$ columns past the first $n$ columns takes $n^2$ column swaps and turns it into $\begin{pmatrix} B & 0 \\ 0 & C \end{pmatrix}$.
So its determinant is $(-1)^{n^2} \det B \det C = (-1)^n \det B \det C$, and not $\det A \det D = 0$.

### What it gives you

Repeated use gives the rule for many blocks: a matrix with square diagonal blocks $A_1, \dots, A_k$ and zeros below them has determinant $\det A_1 \cdots \det A_k$.
With blocks of size $1$ this is the rule for triangular matrices again.
Since $\det M$ is a unit exactly when $\det A$ and $\det D$ are both units, a block triangular matrix is invertible if and only if each diagonal block is invertible.
When the corner block $C$ is not zero but $A$ is invertible, the [[Schur complement formula|0KA7A4ENVJ]] reduces the general case to this one.

### The converse is false

The equation $\det M = \det A \det D$ does not force a corner block to be zero.
Take $A = D = I_2$, $B = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$ and $C = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$.
Then $CB = 0$, so the Schur complement formula gives
$$\det M = \det I_2 \cdot \det(I_2 - C B) = \det I_2 = 1 = \det A \det D,$$
although $B \ne 0$ and $C \ne 0$.

### Watch out

It is tempting to treat the four blocks like the four entries of a $2 \times 2$ matrix and write $\det A \det D - \det B \det C$.
That formula is false for blocks of size at least $2$.
For $A = D = 0$ and $B = C = I_2$ it gives $-1$, while the [[non-example|4WK6BCJF6D]] shows that the true value is $1$.
The block triangular rule is safe only because one corner block is zero.

### Try it

Compute $\det \begin{pmatrix} 3 & 1 & 4 \\ 0 & 2 & 1 \\ 0 & 5 & 3 \end{pmatrix}$ with blocks of sizes $1$ and $2$.
The answer is $3 \cdot (2 \cdot 3 - 1 \cdot 5) = 3 \cdot 1 = 3$.

Is $\begin{pmatrix} 1 & 2 & 0 \\ 2 & 4 & 0 \\ 7 & 8 & 9 \end{pmatrix}$ invertible?
It is lower block triangular with $\det \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} = 0$, so its determinant is $0 \cdot 9 = 0$ and it is not invertible.

## Explanations

### L1 human

Some matrices fall apart into two smaller square pieces on the diagonal, with only zeros in one of the other corners.
Then the determinant of the whole matrix is the product of the determinants of the two pieces.
The numbers in the remaining corner do not matter at all.
For example, if the pieces have determinants $-2$ and $5$, the whole matrix has determinant $-10$.

### L2 human

Here is a typical use: the matrix
$$M = \begin{pmatrix} 2 & 0 & 1 & 0 \\ 0 & 3 & 0 & 1 \\ 1 & 0 & 1 & 0 \\ 0 & 0 & 0 & 4 \end{pmatrix}$$
is not block triangular as it stands.
Swap columns 2 and 3, and then swap rows 2 and 3.
Each swap changes the sign, so two swaps keep the determinant, and the result is
$$M' = \begin{pmatrix} 2 & 1 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 0 & 0 & 3 & 1 \\ 0 & 0 & 0 & 4 \end{pmatrix}.$$
Now the lower left $2 \times 2$ block is zero, and the rule gives
$$\det M = \det M' = (2 - 1) \cdot (12 - 0) = 12.$$
Check by expansion of $M$ along row 4, which has the single entry $4$ in position $(4, 4)$:
$$\det M = 4 \det \begin{pmatrix} 2 & 0 & 1 \\ 0 & 3 & 0 \\ 1 & 0 & 1 \end{pmatrix} = 4 \cdot 3 \cdot (2 - 1) = 12.$$
So the rule often applies after a reordering of rows and columns that groups the indices that interact.

### L3 human

The rule is a statement about [[invariant subspaces|0ACX5QT8TE]].
If a linear map $T$ on a finite-dimensional space $V$ maps a subspace $W$ into itself, choose a basis of $V$ that extends a basis of $W$.
In that basis the matrix of $T$ is block triangular, with the matrix of $T|_W$ and the matrix of the induced map on the [[quotient space|0SVR29SV1V]] $V/W$ on the diagonal.
So the [[determinant of the linear map|0X0HQYSZ0K]] satisfies $\det T = \det(T|_W) \cdot \det(T_{V/W})$.
Applied to $xI - T$, the same rule shows that the [[characteristic polynomial|0VSSPAFM2C]] of $T$ is the product of those of $T|_W$ and $T_{V/W}$.
