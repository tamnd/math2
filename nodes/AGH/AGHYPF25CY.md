---
tag: AGHYPF25CY
kind: example
name: A basis of the column space of a 3 × 4 matrix from its pivot columns
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
instance_of: [03AJKXH1AV]
illustrates: [11CSKXQNG3]
uses: [0F0RPPJ2TT, 0NNR68BFRY, 0BCMGDHZGR]
sources:
  - url: https://en.wikipedia.org/wiki/Row_and_column_spaces
    locator: Basis
  - book: isbn:9780321982384
    locator: Section 4.3
---

## Example

Row reduction finds the pivot columns, and the matching columns of the original matrix are a basis of the column space.
Let
$$A = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 4 \\ 3 & 6 & 1 & 5 \end{pmatrix}$$
over $\mathbb{R}$, with columns $a_1 = (1, 2, 3)$, $a_2 = (2, 4, 6)$, $a_3 = (0, 1, 1)$ and $a_4 = (1, 4, 5)$.

1. Subtract $2$ times row 1 from row 2, and $3$ times row 1 from row 3; the rows become $(1, 2, 0, 1)$, $(0, 0, 1, 2)$ and $(0, 0, 1, 2)$.
2. Subtract row 2 from row 3; the result is the [[reduced row echelon form|0NNR68BFRY]]
$$R = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{pmatrix}.$$
3. The [[pivots|0BCMGDHZGR]] are in columns 1 and 3, so $a_1 = (1, 2, 3)$ and $a_3 = (0, 1, 1)$ form a basis of the [[column space|0F0RPPJ2TT]], and $\operatorname{rank} A = 2$.
4. Column 2 of $R$ is $2$ times column 1, so $a_2 = 2a_1$; check: $2(1, 2, 3) = (2, 4, 6)$.
5. Column 4 of $R$ is column 1 plus $2$ times column 3, so $a_4 = a_1 + 2a_3$; check: $(1, 2, 3) + (0, 2, 2) = (1, 4, 5)$.
6. The vectors $a_1$ and $a_3$ are independent, since $a_3$ has first entry $0$ and $a_1$ does not, so neither is a multiple of the other.
7. A general combination is $s a_1 + t a_3 = (s, 2s + t, 3s + t)$, and its third entry is the sum of the first two.

So the column space is the plane
$$\operatorname{Col}(A) = \{(u, v, w) \in \mathbb{R}^3 : w = u + v\}.$$

## Remarks

The example shows how row reduction gives more than a basis.
The non-pivot columns of $R$ record the relations $a_2 = 2a_1$ and $a_4 = a_1 + 2a_3$, and these relations hold in $A$ because row operations keep the null space.
The equation $w = u + v$ is a consistency test: $Ax = (1, 1, 1)$ has no solution, since $1 \ne 1 + 1$, while $Ax = (1, 4, 5)$ has the solution $x = (0, 0, 0, 1)$.

Watch out: the pivot columns of $R$ are $(1, 0, 0)$ and $(0, 1, 0)$, and neither lies in $\operatorname{Col}(A)$, since $0 \ne 1 + 0$ for both.
This is the trap of the [[example on the reduced form|K21W7FA8MQ]].
If we change the entry $5$ in the corner to $6$, then column 4 is no longer $a_1 + 2a_3$, a third pivot appears, and the column space becomes all of $\mathbb{R}^3$.

## Explanations

### L1 human

The column space of this matrix is a plane, spanned by the first and the third columns.
The second column is twice the first, and the fourth is the first plus twice the third.
So the second and fourth columns add nothing new.

### L2 human

The method has three moves: row reduce, read the pivot positions, and go back to $A$ for the vectors.
Here the pivots sit in columns 1 and 3, so the basis is $(1, 2, 3), (0, 1, 1)$.
The typical use is to describe the image of the map $x \mapsto Ax$ with as few vectors as possible.
Watch out: taking the columns of $R$ gives a basis of a different plane, the plane $w = 0$.
