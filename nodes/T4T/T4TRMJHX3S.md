---
tag: T4TRMJHX3S
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

When the two lower blocks of a $2 \times 2$ block matrix commute, the rule $ad - bc$ holds with matrix products in place of number products, and the determinant is taken once, at the end.
Let $K$ be a commutative ring, let $n \ge 1$, and let $A$, $B$, $C$, $D$ be $n \times n$ matrices over $K$ with $CD = DC$.
Then the [[block matrix|01AXG9KZQF]] satisfies
$$\det \begin{pmatrix} A & B \\ C & D \end{pmatrix} = \det(AD - BC),$$
where $\det$ is the [[determinant|0C3CFHDN6R]].

## Remarks

### A worked case

Take
$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \quad B = I_2, \quad C = 2 I_2, \quad D = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}.$$
A multiple of the identity commutes with every matrix, so $CD = DC = 2D$.
Multiply and subtract:
$$AD = \begin{pmatrix} 1 & 3 \\ 3 & 7 \end{pmatrix}, \qquad AD - BC = \begin{pmatrix} 1 - 2 & 3 \\ 3 & 7 - 2 \end{pmatrix} = \begin{pmatrix} -1 & 3 \\ 3 & 5 \end{pmatrix}.$$
So the block matrix has determinant $\det(AD - BC) = -5 - 9 = -14$.

Check with the [[Schur complement formula|0KA7A4ENVJ]], since $A$ is invertible with $\det A = -2$ and $A^{-1} = \begin{pmatrix} -2 & 1 \\ 3/2 & -1/2 \end{pmatrix}$.
Then $C A^{-1} B = 2 A^{-1}$, and
$$D - 2A^{-1} = \begin{pmatrix} 1 + 4 & 1 - 2 \\ 0 - 3 & 1 + 1 \end{pmatrix} = \begin{pmatrix} 5 & -1 \\ -3 & 2 \end{pmatrix},$$
with determinant $10 - 3 = 7$.
So the determinant is $-2 \cdot 7 = -14$, which agrees.
The naive formula $\det A \det D - \det B \det C = -2 \cdot 1 - 1 \cdot 4 = -6$ is wrong here.

### Why the blocks must commute

The blocks must be square of one size, so that $AD - BC$ is defined and square.
The condition $CD = DC$ cannot be dropped.
Take
$$A = C = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \quad B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}, \quad D = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}.$$
Then $CD = D$ but $DC = 0$.
The block matrix is
$$\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix},$$
and its last row is zero, so its determinant is $0$.
But $AD = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $BC = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$, so $AD - BC = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, with determinant $1$.

### Where it comes from

When $D$ is invertible, multiply the block matrix on the right by $\begin{pmatrix} D & 0 \\ -C & I_n \end{pmatrix}$.
Because $CD = DC$, the lower left block of the product is $CD - DC = 0$, so the product is block triangular with diagonal blocks $AD - BC$ and $D$.
Taking determinants gives $\det M \cdot \det D = \det(AD - BC) \cdot \det D$, and we cancel $\det D$.
The [[proof|EFP0JATYWD]] removes the need for an invertible $D$ by replacing $D$ with $D + xI_n$ for a variable $x$.

### The converse and the other three cases

The converse is false: the formula can hold when $CD \ne DC$.
For $A = B = 0$, both sides are $0$ for all $C$ and $D$ of size $2$, since $AD - BC = 0$ and the block matrix has two zero rows.

Each pair of blocks in one row or one column gives its own version.
If $AC = CA$, the determinant is $\det(AD - CB)$.
If $BD = DB$, it is $\det(DA - BC)$, and if $AB = BA$, it is $\det(DA - CB)$.
The order of the factors in each product matters, and it follows the pair that commutes.
For $n = 1$ all four conditions hold, and every version is $ad - bc$.

### Try it

Let $A = 2I_2$, $B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, $C = I_2$ and $D = 3I_2$.
Here $AD - BC = 6I_2 - B = \begin{pmatrix} 6 & -1 \\ -1 & 6 \end{pmatrix}$, so the determinant of the block matrix is $36 - 1 = 35$.

## Explanations

### L1 human

Think of a $4 \times 4$ matrix cut into four $2 \times 2$ pieces.
If the two bottom pieces commute, you may compute "first piece times last piece minus second piece times third piece" as one $2 \times 2$ matrix.
The determinant of that single matrix is the determinant of the whole $4 \times 4$ matrix.
The order matters: you must multiply the pieces, not their determinants, and only then take one determinant.

### L2 human

Here is a typical use: matrices of the form $\begin{pmatrix} A & -B \\ B & A \end{pmatrix}$ with $AB = BA$, which turn up when a complex matrix $A + iB$ is written as a real matrix.
The lower blocks $B$ and $A$ commute, so the formula gives
$$\det \begin{pmatrix} A & -B \\ B & A \end{pmatrix} = \det(A^2 + B^2).$$
For $A = I_2$ and $B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ we have $B^2 = 0$, so the determinant is $\det(I_2) = 1$.
Check by the Leibniz formula on the $4 \times 4$ matrix
$$\begin{pmatrix} 1 & 0 & 0 & -1 \\ 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}.$$
Expanding along column 1 and then along the last row leaves $\det \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} = 1$, which agrees.
Watch out: the answer is $\det(A^2 + B^2)$ and not $(\det A)^2 + (\det B)^2$.
For $A = B = I_2$ the formula gives $\det(2 I_2) = 4$, while $(\det A)^2 + (\det B)^2 = 2$.

### L3 human

The general principle behind the formula is a theorem about commutative subrings.
Suppose that all blocks of a block matrix lie in one commutative ring $R$ of $n \times n$ matrices.
Then the block matrix is a matrix over $R$, and its determinant over $R$ is an element of $R$, that is, an $n \times n$ matrix.
The determinant of that matrix over $K$ equals the determinant of the block matrix over $K$.
The proposition is a sharper form for $2 \times 2$ block matrices, which needs only the two lower blocks to commute.
The [[proof|EFP0JATYWD]] shows a standard device of the sub-area: prove an identity when a determinant is cancellable, then reach the general case through a polynomial variable.
