---
tag: B2YDT3YNCW
kind: example
name: The first minors and leading principal minors of a 3 × 3 matrix
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
instance_of: [0BT9BYWVRY]
uses: [0SD528P0EK, 0ZN2J42SK7, 0C08BQ3M05]
sources:
  - url: https://en.wikipedia.org/wiki/Minor_(linear_algebra)
    locator: First minors
---

## Example

We compute the first minors of one row and the leading principal minors of the matrix
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 10 \end{pmatrix}$$
over $\mathbb{Q}$, and then use them to find $\det A$.
Each [[minor|0SD528P0EK]] of order $2$ comes from the [[2 by 2 formula|0ZN2J42SK7]] $ad - bc$.

1. The first minor $M_{11}$ deletes row $1$ and column $1$:
$$M_{11} = \det \begin{pmatrix} 5 & 6 \\ 8 & 10 \end{pmatrix} = 50 - 48 = 2.$$
2. The first minor $M_{12}$ deletes row $1$ and column $2$:
$$M_{12} = \det \begin{pmatrix} 4 & 6 \\ 7 & 10 \end{pmatrix} = 40 - 42 = -2.$$
3. The first minor $M_{13}$ deletes row $1$ and column $3$:
$$M_{13} = \det \begin{pmatrix} 4 & 5 \\ 7 & 8 \end{pmatrix} = 32 - 35 = -3.$$
4. The leading principal minors use the top left corners of sizes $1$, $2$ and $3$.
   They are $\det(1) = 1$, then $\det \begin{pmatrix} 1 & 2 \\ 4 & 5 \end{pmatrix} = 5 - 8 = -3$, and finally $\det A$.
5. The [[Laplace expansion|0C08BQ3M05]] along row $1$ attaches the signs $+, -, +$:
$$\det A = 1 \cdot M_{11} - 2 \cdot M_{12} + 3 \cdot M_{13} = 2 + 4 - 9 = -3.$$
6. Check by row reduction.
   The operations $R_2 - 4R_1$ and $R_3 - 7R_1$ do not change the determinant, and they give the rows $(0, -3, -6)$ and $(0, -6, -11)$.
   Expanding along the first column,
$$\det A = 1 \cdot \big( (-3)(-11) - (-6)(-6) \big) = 33 - 36 = -3.$$

So the leading principal minors are $1$, $-3$ and $-3$.

## Remarks

For a $3 \times 3$ matrix, the $9$ first minors and the $\binom{3}{2}^2 = 9$ minors of order $2$ are the same numbers, because deleting one row and one column is the same as keeping two rows and two columns.
For a $4 \times 4$ matrix the two notions part: the first minors have order $3$, and there are $\binom{4}{2}^2 = 36$ minors of order $2$.

The second leading principal minor is negative.
For a symmetric matrix, [[Sylvester's criterion|0WKEF78PMV]] would then say that the matrix is not positive definite, but $A$ is not symmetric, so the criterion does not apply here.
If the last entry $10$ is changed to $9$, then $M_{13}$ stays the same, $M_{11}$ becomes $45 - 48 = -3$ and $M_{12}$ becomes $36 - 42 = -6$.
The expansion then gives $1 \cdot (-3) - 2 \cdot (-6) + 3 \cdot (-3) = 0$, so that matrix is singular.

## Explanations

### L1 human

Each entry of a $3 \times 3$ table has a minor.
Cover the row and the column of the entry, and take the $2 \times 2$ determinant of the four numbers left.
Here the three minors of the first row are $2$, $-2$ and $-3$.
Combined with the entries $1, 2, 3$ and the signs plus, minus, plus, they give the determinant $-3$.

### L2 human

The point of the example is that two methods agree.
The expansion by minors of row $1$ gives $-3$, and row reduction gives $-3$, so the three minors are right.
Watch out for the middle sign: without it the expansion gives $2 - 4 - 9 = -11$, which is wrong.
The same minors with their signs, $C_{11} = 2$, $C_{12} = 2$ and $C_{13} = -3$, form the first row of the cofactor matrix, and they reappear in the adjugate and the inverse of $A$.
