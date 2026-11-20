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

Let $K$ be a commutative ring, let $A$ be an $m \times m$ matrix, $B$ an $m \times n$ matrix and $D$ an $n \times n$ matrix over $K$, with $m, n \ge 1$.
Then the [[block matrix|01AXG9KZQF]] satisfies
$$\det \begin{pmatrix} A & B \\ 0 & D \end{pmatrix} = \det A \cdot \det D,$$
where $0$ is the $n \times m$ zero matrix and $\det$ is the [[determinant|0C3CFHDN6R]].
The same holds for the lower block triangular matrix $\begin{pmatrix} A & 0 \\ C & D \end{pmatrix}$, with $C$ of size $n \times m$.

## Remarks

### Why each hypothesis is needed

The diagonal blocks must be square, or their determinants have no meaning.
The zero block must be in a corner below or above the diagonal blocks.
For $\begin{pmatrix} 0 & B \\ C & 0 \end{pmatrix}$ with square $B$ and $C$ of size $n$, the determinant is $(-1)^{n} \det B \det C$, not $\det B \det C$.

### Consequences

- With blocks of size $1$, repeated use gives the rule for [[triangular matrices|0K1KKMFHYH]].
- By induction, a matrix with square diagonal blocks $A_1, \dots, A_k$ and zeros below them has determinant $\det A_1 \cdots \det A_k$.
- A block triangular matrix is invertible if and only if each diagonal block is invertible.

### Converse

The converse is false: $\det M = \det A \det D$ does not force a corner block to be zero.
Take $A = D = I_2$, $B = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$ and $C = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$.
Then $CB = 0$, so the [[Schur complement formula|0KA7A4ENVJ]] gives $\det M = \det(I_2 - CB) = 1 = \det A \det D$, although $B \ne 0$ and $C \ne 0$.

### Generalizations

- When $A$ is invertible, the [[Schur complement formula|0KA7A4ENVJ]] handles a general block matrix.
- For a general block matrix, $\det \begin{pmatrix} A & B \\ C & D \end{pmatrix} = \det A \det D - \det B \det C$ is false; the [[non-example|4WK6BCJF6D]] shows a $4 \times 4$ case.

The [[proof by the Leibniz formula|92GVP9180G]] works over every commutative ring.
A second argument factors $\begin{pmatrix} A & B \\ 0 & D \end{pmatrix} = \begin{pmatrix} I_m & 0 \\ 0 & D \end{pmatrix} \begin{pmatrix} A & B \\ 0 & I_n \end{pmatrix}$ and expands each factor by Laplace.

## Explanations

### L1 human

When a matrix has a block of zeros in its lower left corner, its determinant splits.
It is the product of the determinants of the two diagonal blocks.
The block $B$ does not matter, just like the entries above the diagonal of a triangular matrix.

### L2 human

Take $M = \begin{pmatrix} 1 & 2 & 5 & 6 \\ 3 & 4 & 7 & 8 \\ 0 & 0 & 2 & 1 \\ 0 & 0 & 1 & 3 \end{pmatrix}$, with $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $D = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$.

1. $\det A = 4 - 6 = -2$ and $\det D = 6 - 1 = 5$.
2. The formula gives $\det M = -2 \cdot 5 = -10$.
3. Check by the [[generalized Laplace expansion|541X51GQTV]] along rows 1 and 2: only the columns $\{1, 2\}$ give a nonzero lower minor, so $\det M = \det A \cdot \det D = -10$.
4. Check by row operations: subtract $3$ times row 1 from row 2 to get the pivots $1, -2$, then $D$ reduces to the pivots $2, 5/2$; the product is $1 \cdot (-2) \cdot 2 \cdot 5/2 = -10$.
The typical use is a matrix that becomes block triangular after a reordering of rows and columns.
A trap: the zero block must be off the diagonal.
If instead $A = 0$ and all blocks are $n \times n$, then $\det M = (-1)^n \det B \det C$, which is not $\det A \det D = 0$ in general.

### L3 human

The rule says that $\det$ is multiplicative along a filtration: if a linear map $T$ on $V$ keeps a subspace $W$ invariant, then $\det T = \det(T|_W) \cdot \det(T_{V/W})$.
This is the block triangular form in a basis of $V$ that extends a basis of $W$.
