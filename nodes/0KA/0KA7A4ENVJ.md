---
tag: 0KA7A4ENVJ
kind: statement
role: theorem
name: Determinant via the Schur complement
aliases: [block-determinant-by-the-schur-complement]
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
about: [00KDZRW4C0]
uses: [0C3CFHDN6R, 01AXG9KZQF, 0TWTS88TWN]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.det_fromBlocks₁₁
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Schur_complement
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Block matrices
---

## Statement

When the upper left block of a block matrix is invertible, block elimination reduces the determinant of the whole matrix to two smaller determinants.
Let $K$ be a commutative ring, let $p, q \ge 1$, and let $A$ be an [[invertible|0TWTS88TWN]] $p \times p$ matrix over $K$.
Let $B$, $C$ and $D$ be matrices over $K$ of sizes $p \times q$, $q \times p$ and $q \times q$.
Then
$$\det \begin{pmatrix} A & B \\ C & D \end{pmatrix} = \det A \cdot \det(D - C A^{-1} B),$$
where $\det$ is the [[determinant|0C3CFHDN6R]].
The $q \times q$ matrix $D - C A^{-1} B$ is the *Schur complement* of $A$ in the [[block matrix|01AXG9KZQF]].

## Remarks

### A first computation

Take $p = q = 2$ over $\mathbb{Q}$, with
$$A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}, \quad B = C = I_2, \quad D = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}, \quad M = \begin{pmatrix} 2 & 1 & 1 & 0 \\ 1 & 1 & 0 & 1 \\ 1 & 0 & 3 & 1 \\ 0 & 1 & 1 & 2 \end{pmatrix}.$$
Here $\det A = 2 - 1 = 1$ and $A^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$.
Since $B = C = I_2$, the Schur complement is
$$S = D - A^{-1} = \begin{pmatrix} 3 - 1 & 1 + 1 \\ 1 + 1 & 2 - 2 \end{pmatrix} = \begin{pmatrix} 2 & 2 \\ 2 & 0 \end{pmatrix}, \qquad \det S = 0 - 4 = -4.$$
So $\det M = 1 \cdot (-4) = -4$.

Check by elimination.
Subtract $\tfrac12$ of row 1 from rows 2 and 3, then add the new row 2 to row 3 and subtract twice the new row 2 from row 4.
The first two pivots are $2$ and $\tfrac12$, and the lower right block that remains is exactly $S$.
Its pivots are $2$ and $-2$, so $\det M = 2 \cdot \tfrac12 \cdot 2 \cdot (-2) = -4$.
This is the idea of the [[proof by block factorization|3T0706APQT]]: elimination of the first $p$ columns leaves the Schur complement in the corner.

### Why the corner must be invertible

The formula uses $A^{-1}$, so it says nothing when $A$ is singular.
Then the other corner may help: if $D$ is invertible, the same argument gives
$$\det \begin{pmatrix} A & B \\ C & D \end{pmatrix} = \det D \cdot \det(A - B D^{-1} C).$$
If neither corner is invertible, neither formula applies.
For example, $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ with $1 \times 1$ blocks has $A = D = 0$, and the [[Leibniz formula|016PE4VZ8Q]] still gives its determinant $-1$.

### What it gives you

For $p = q = 1$ and a unit $a$, the formula reads
$$\det \begin{pmatrix} a & b \\ c & d \end{pmatrix} = a \Bigl(d - \frac{cb}{a}\Bigr) = ad - bc,$$
the [[determinant of a 2 × 2 matrix|0ZN2J42SK7]].
For $C = 0$ the Schur complement is $D$, and the formula becomes the [[block triangular rule|0J9TVTNB4K]].
It also gives a test for invertibility: since $\det A$ is a unit, the block matrix is invertible if and only if its Schur complement is invertible.

For an $m \times n$ matrix $X$ and an $n \times m$ matrix $Y$, computing $\det \begin{pmatrix} I_m & -X \\ Y & I_n \end{pmatrix}$ with both corners gives $\det(I_n + YX) = \det(I_m + XY)$, the [[Weinstein-Aronszajn identity|0G24VQ1088]].
The [[matrix determinant lemma|0BC3Q6K92H]] is the case of a rank one update.
When all four blocks are square of the same size and $CD = DC$, the [[formula for commuting blocks|T4TRMJHX3S]] gives $\det(AD - BC)$, even when no block is invertible.

### Watch out

The order of the factors in $C A^{-1} B$ matters.
The product $B A^{-1} C$ is not even defined unless $p = q$, and when it is defined it is usually a different matrix.
For example, with $A = I_2$, $B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $C = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, we get $CB = B$ but $BC = 0$.
The safe rule is to read the blocks along a path: from row block 2 through column block 1 ($C$), the inverse of the pivot block ($A^{-1}$), and then column block 2 ($B$).

The naive formula $\det A \det D - \det B \det C$ is false for blocks of size at least $2$, as the [[non-example|4WK6BCJF6D]] shows.

### Try it

Compute $\det \begin{pmatrix} 1 & 2 & 1 \\ 3 & 4 & 0 \\ 0 & 1 & 2 \end{pmatrix}$ with $p = 1$.
Here $C A^{-1} B = \begin{pmatrix} 3 \\ 0 \end{pmatrix} \begin{pmatrix} 2 & 1 \end{pmatrix} = \begin{pmatrix} 6 & 3 \\ 0 & 0 \end{pmatrix}$, so $S = \begin{pmatrix} -2 & -3 \\ 1 & 2 \end{pmatrix}$ and the determinant is $1 \cdot (-4 + 3) = -1$.

Let $u = (1, 1)^{\mathsf{T}}$, and compute $\det \begin{pmatrix} I_2 & u \\ u^{\mathsf{T}} & 1 \end{pmatrix}$.
The Schur complement of $I_2$ is $1 - u^{\mathsf{T}} u = 1 - 2 = -1$, so the determinant is $-1$.

## Explanations

### L1 human

Gaussian elimination clears the entries below a pivot by subtracting multiples of the pivot row.
Block elimination does the same with a whole invertible block as the pivot.
After the lower left block is cleared, a new block remains in the lower right corner, and that block is the Schur complement.
The determinant of the big matrix is then the determinant of the pivot block times the determinant of the Schur complement.

### L2 human

Here is a typical use: a matrix with an identity block, which is the easiest pivot.
Take
$$M = \begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & 3 \\ 4 & 5 & 6 \end{pmatrix}, \qquad A = I_2, \quad B = \begin{pmatrix} 2 \\ 3 \end{pmatrix}, \quad C = \begin{pmatrix} 4 & 5 \end{pmatrix}, \quad D = (6).$$
With $A = I_2$ the Schur complement needs no inverse:
$$D - CB = 6 - (4 \cdot 2 + 5 \cdot 3) = 6 - 23 = -17.$$
So $\det M = 1 \cdot (-17) = -17$.
Check by expansion along the first row:
$$\det M = 1 \cdot (6 - 15) + 2 \cdot (0 - 4) = -9 - 8 = -17.$$
The Schur complement turned a $3 \times 3$ determinant into one dot product.
In the same way, an $n \times n$ matrix with a large identity block costs only a small determinant.

### L3 human

The Schur complement is what Gaussian elimination leaves behind.
If the first $p$ steps of elimination need no row swaps, the trailing $q \times q$ block is exactly $D - C A^{-1} B$, so the pivots of $M$ are the pivots of $A$ followed by those of the Schur complement.
The same block factorization gives the inverse of $M$ when $S = D - C A^{-1} B$ is invertible:
$$M^{-1} = \begin{pmatrix} A^{-1} + A^{-1} B S^{-1} C A^{-1} & -A^{-1} B S^{-1} \\ -S^{-1} C A^{-1} & S^{-1} \end{pmatrix}.$$
Let $M$ be real symmetric, so that $C = B^{\mathsf{T}}$, and let $A$ be [[positive definite|0KX66CZMBB]].
Then $M$ is positive definite if and only if its Schur complement is.
More generally, when $A$ is only invertible, the inertia of $M$ is the sum of the inertias of $A$ and of the Schur complement.
In statistics, the covariance of one part of a [[multivariate normal|0XN3K7RSZY]] vector given the other part is a Schur complement of the covariance matrix.
