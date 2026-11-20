---
tag: ~f4c12cfe
kind: statement
role: proposition
name: Block determinant with commuting blocks
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug2
about: [00KDZRW4C0]
uses: [0C3CFHDN6R, 01AXG9KZQF]
sources:
  - url: https://en.wikipedia.org/wiki/Block_matrix
    locator: Determinant
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Block matrices
---

## Statement

Let $K$ be a commutative ring, and let $A$, $B$, $C$, $D$ be $n \times n$ matrices over $K$ with $CD = DC$.
Then the [[block matrix|01AXG9KZQF]] satisfies
$$\det \begin{pmatrix} A & B \\ C & D \end{pmatrix} = \det(AD - BC),$$
where $\det$ is the [[determinant|0C3CFHDN6R]].

## Remarks

### Why each hypothesis is needed

The blocks must all be square of the same size, so that $AD - BC$ is defined and square.
The condition $CD = DC$ is needed.
Take $A = C = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, $B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ and $D = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.
Then $CD = D$ but $DC = 0$, so the blocks do not commute.
The block matrix is $\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix}$, and its last row is zero, so its determinant is $0$.
But $AD - BC = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, with determinant $1$.

### Consequences

For $n = 1$ the condition always holds, and the formula is $ad - bc$.
When $D$ is invertible, the [[Schur complement formula|0KA7A4ENVJ]] gives the result directly.
The [[proof|~ce003c8e]] removes the invertibility of $D$ with a polynomial variable.

### Converse

The converse is false: the formula can hold when $CD \ne DC$.
For $A = B = 0$, both sides are $0$ for any $C$ and $D$ of size $2$, since $AD - BC = 0$ and the block matrix has two zero rows.

### Generalizations

If $AC = CA$, then the determinant is $\det(AD - CB)$.
If $BD = DB$, it is $\det(DA - BC)$, and if $AB = BA$, it is $\det(DA - CB)$.
The order of the factors in each product matters.

## Explanations

### L1 human

When two blocks commute, the $2 \times 2$ rule $ad - bc$ holds with matrices in place of numbers.
But the determinant is taken at the end, of the matrix $AD - BC$, and not of each block.

### L2 human

Take $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, $B = I_2$, $C = 2 I_2$ and $D = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$; then $CD = DC = 2D$.

1. $AD = \begin{pmatrix} 1 & 3 \\ 3 & 7 \end{pmatrix}$ and $BC = 2 I_2$, so $AD - BC = \begin{pmatrix} -1 & 3 \\ 3 & 5 \end{pmatrix}$.
2. The formula gives $\det M = -5 - 9 = -14$.
3. Check by the Schur complement: $\det A = -2$ and $A^{-1} = \begin{pmatrix} -2 & 1 \\ 3/2 & -1/2 \end{pmatrix}$.
4. $C A^{-1} B = 2 A^{-1} = \begin{pmatrix} -4 & 2 \\ 3 & -1 \end{pmatrix}$, so $D - C A^{-1} B = \begin{pmatrix} 5 & -1 \\ -3 & 2 \end{pmatrix}$, with determinant $7$.
5. So $\det M = -2 \cdot 7 = -14$, which agrees.

The false formula $\det A \det D - \det B \det C = -2 - 4 = -6$ gives a wrong value.

### L3 human

The blocks $C$ and $D$ lie in the commutative ring $R = K[C, D]$ of matrices, so $M$ is a $2 \times 2$ matrix over $R$ when $A$ and $B$ lie in $R$ too.
The formula then says that taking $\det$ over $R$ first and over $K$ second gives $\det M$.
