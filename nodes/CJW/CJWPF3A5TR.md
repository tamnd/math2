---
tag: CJWPF3A5TR
kind: example
name: The CR factorization of a 3 × 4 matrix
msc: ["15A03", "15A23"]
topics: [S6559D61BP]
audience: ug1
illustrates: [5JGAG62VN8]
uses: [0NNR68BFRY, 0BCMGDHZGR, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_factorization
    locator: Rank factorization from reduced row echelon forms
---

## Example

A $3 \times 4$ matrix of rank $2$ is a $3 \times 2$ matrix times a $2 \times 4$ matrix, and so it is a sum of two rank-one matrices.
Let
$$A = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 4 \\ 3 & 6 & 1 & 5 \end{pmatrix}.$$

1. Subtract twice row 1 from row 2 and three times row 1 from row 3; both new rows are $(0, 0, 1, 2)$.
Subtracting the new row 2 from the new row 3 leaves a zero row.
So the [[reduced row echelon form|0NNR68BFRY]] has the nonzero rows $(1, 2, 0, 1)$ and $(0, 0, 1, 2)$, as in the [[column space example|AGHYPF25CY]].
2. The [[pivot columns|0BCMGDHZGR]] are columns 1 and 3, so $r = 2$.
3. Take for $C$ columns 1 and 3 of $A$, and for $R$ the nonzero rows of the reduced form:
$$C = \begin{pmatrix} 1 & 0 \\ 2 & 1 \\ 3 & 1 \end{pmatrix}, \qquad R = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 0 & 0 & 1 & 2 \end{pmatrix}.$$
4. By the [[matrix product|076JGP6R3T]], row $i$ of $CR$ is $C_{i1}$ times row 1 of $R$ plus $C_{i2}$ times row 2 of $R$:
$$\begin{aligned} 1 \cdot (1, 2, 0, 1) + 0 \cdot (0, 0, 1, 2) &= (1, 2, 0, 1), \\ 2 \cdot (1, 2, 0, 1) + 1 \cdot (0, 0, 1, 2) &= (2, 4, 1, 4), \\ 3 \cdot (1, 2, 0, 1) + 1 \cdot (0, 0, 1, 2) &= (3, 6, 1, 5). \end{aligned}$$
These are the rows of $A$, so $CR = A$.
5. The columns $(1, 2, 3)$ and $(0, 1, 1)$ of $C$ are not proportional, so $\rank C = 2$.
The rows of $R$ have their leading entries in different columns, so $\rank R = 2$.
6. Expanding the product column by row gives two rank-one matrices:
$$\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} \begin{pmatrix} 1 & 2 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 0 & 2 \\ 3 & 6 & 0 & 3 \end{pmatrix}, \qquad \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} \begin{pmatrix} 0 & 0 & 1 & 2 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 1 & 2 \end{pmatrix}.$$
Check: their sum has rows $(1, 2, 0, 1)$, $(2, 4, 1, 4)$ and $(3, 6, 1, 5)$, which is $A$.

## Remarks

### What the columns of R say

Column $k$ of $R$ holds the coordinates of column $k$ of $A$ in the basis $a_1, a_3$.
Column 4 of $R$ is $(1, 2)$, so $a_4 = a_1 + 2a_3 = (1, 2, 3) + 2(0, 1, 1) = (1, 4, 5)$, which is column 4 of $A$.
Column 2 of $R$ is $(2, 0)$, so $a_2 = 2a_1$.

### Another factorization

Another basis of the column space gives another factorization.
For $G = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, the matrix $CG$ has columns $(1, 2, 3)$ and $(1, 3, 4)$, and $G^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$ gives
$$G^{-1} R = \begin{pmatrix} 1 & 2 & -1 & -1 \\ 0 & 0 & 1 & 2 \end{pmatrix}, \qquad A = (CG)(G^{-1} R).$$
Check: the first row of $CG$ is $(1, 1)$, and $(1, 2, -1, -1) + (0, 0, 1, 2) = (1, 2, 0, 1)$ is the first row of $A$.

### Try it

Write $B = \begin{pmatrix} 3 & -1 & 0 \\ 6 & -2 & 0 \end{pmatrix}$ as $uv^{\mathsf{T}}$.
Row 2 is twice row 1, so $\rank B = 1$, and $u = (1, 2)$ with $v = (3, -1, 0)$ works.

## Explanations

### L1 human

The matrix $A$ has $12$ entries, but two columns and two rows fix it.
The two columns are the pivot columns $(1, 2, 3)$ and $(0, 1, 1)$, and the two rows come from the reduced form.
Every column of $A$ is a mix of the two pivot columns, and the matching column of $R$ gives the recipe.

### L2 human

The computation has three stages: reduce $A$, read off the pivot columns, and copy the nonzero rows of the reduced form into $R$.
Watch out: the columns of $C$ come from $A$, and not from the reduced form, whose pivot columns $(1, 0, 0)$ and $(0, 1, 0)$ do not even lie in $\operatorname{Col}(A)$.
Indeed, every column of $A$ has third entry equal to the sum of its first two entries, and $(1, 0, 0)$ does not.
Expanding $CR$ column by row then gives $A$ as a sum of two rank-one matrices, the smallest possible number for a matrix of rank $2$.
