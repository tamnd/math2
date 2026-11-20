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

Let $K$ be a commutative ring and let $A$ be an [[invertible|0TWTS88TWN]] $p \times p$ matrix over $K$.
Let $B$, $C$ and $D$ be matrices over $K$ of sizes $p \times q$, $q \times p$ and $q \times q$, with $p, q \ge 1$.
Then
$$\det \begin{pmatrix} A & B \\ C & D \end{pmatrix} = \det A \cdot \det(D - C A^{-1} B),$$
where $\det$ is the [[determinant|0C3CFHDN6R]].
The matrix $D - C A^{-1} B$ is the *Schur complement* of $A$ in the [[block matrix|01AXG9KZQF]].

## Remarks

### Why each hypothesis is needed

The formula needs $A^{-1}$; when $A$ is singular, use the other corner instead.
If $D$ is invertible, the same argument gives $\det \begin{pmatrix} A & B \\ C & D \end{pmatrix} = \det D \cdot \det(A - B D^{-1} C)$.
If neither corner is invertible, then neither formula applies, but the [[Leibniz formula|016PE4VZ8Q]] still does.

### Consequences

- For $p = q = 1$ and $a$ a unit, it gives $\det \begin{pmatrix} a & b \\ c & d \end{pmatrix} = a(d - cb/a) = ad - bc$.
- For $C = 0$ it gives the [[block triangular rule|0J9TVTNB4K]].
- If $A, B, C, D$ are square of the same size and $CD = DC$, then the determinant is $\det(AD - BC)$; see [[commuting blocks|T4TRMJHX3S]].
- The [[Weinstein-Aronszajn identity|0G24VQ1088]] follows by computing $\det \begin{pmatrix} I_m & -A \\ B & I_n \end{pmatrix}$ with both corners.

### Converse

The formula is an identity, so a converse in the usual sense does not apply.
A related equivalence holds: when $A$ is invertible, the block matrix is invertible if and only if the Schur complement $D - C A^{-1} B$ is invertible.

### Generalizations

- The same method gives the inverse of a block matrix in terms of $A^{-1}$ and the inverse of the Schur complement.
- A trap: the naive formula $\det A \det D - \det B \det C$ is false for blocks of size at least $2$; see the [[non-example|4WK6BCJF6D]].

## Explanations

### L1 human

Block elimination removes the block $C$, in the same way as Gaussian elimination removes an entry.
What remains in the lower right corner is the Schur complement.
The determinant is then the product of two smaller determinants.

### L2 human

Take $A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$, $B = C = I_2$ and $D = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}$ over $\mathbb{Q}$.

1. $\det A = 1$ and $A^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$.
2. $C A^{-1} B = A^{-1}$, so $S = D - A^{-1} = \begin{pmatrix} 2 & 2 \\ 2 & 0 \end{pmatrix}$, with $\det S = -4$.
3. The formula gives $\det M = 1 \cdot (-4) = -4$ for $M = \begin{pmatrix} 2 & 1 & 1 & 0 \\ 1 & 1 & 0 & 1 \\ 1 & 0 & 3 & 1 \\ 0 & 1 & 1 & 2 \end{pmatrix}$.
4. Check by elimination: $R_2 - \tfrac12 R_1$, $R_3 - \tfrac12 R_1$ give pivots $2$ and $\tfrac12$.
5. Then $R_3 + R_2$ and $R_4 - 2R_2$ leave the block $\begin{pmatrix} 2 & 2 \\ 2 & 0 \end{pmatrix}$, which is $S$.
6. Its pivots are $2$ and $-2$, so $\det M = 2 \cdot \tfrac12 \cdot 2 \cdot (-2) = -4$.

Step 5 shows the idea of the proof: block elimination leaves the Schur complement in the corner.
The typical use is a matrix with an easy corner block, such as a diagonal or an identity block.
A trap: the order in $C A^{-1} B$ matters, and $B A^{-1} C$ has the wrong size in general.

### L3 human

The Schur complement is the matrix of the quotient form after a partial Gaussian elimination.
It gives the inertia rule for symmetric matrices and the formula for the inverse of a block matrix.
