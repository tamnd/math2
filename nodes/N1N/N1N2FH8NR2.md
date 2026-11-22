---
tag: N1N2FH8NR2
kind: example
name: A table of sales as a 2 × 3 matrix
msc: ["15A99", "97H60"]
topics: [Y1ESNQ2V52]
audience: school
instance_of: [0VD9ZSWWJG]
uses: [0VD9ZSWWJG, 0N1MY1T0W9]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_(mathematics)
    locator: Definition
---

## Example

A company sells three products $P_1$, $P_2$ and $P_3$ in two shops $S_1$ and $S_2$.
In one week, shop $S_1$ sells $4$, $0$ and $7$ units of the three products, and shop $S_2$ sells $2$, $5$ and $1$ units.
We record the data as a [[matrix|0VD9ZSWWJG]] $A$ with one row for each shop and one column for each product.

1. The table has 2 rows and 3 columns, so $A$ is a $2 \times 3$ matrix:
$$A = \begin{pmatrix} 4 & 0 & 7 \\ 2 & 5 & 1 \end{pmatrix}.$$
2. The entry $a_{ij}$ is the number of units of $P_j$ sold in $S_i$. For example, $a_{13} = 7$ and $a_{22} = 5$.
3. Row 1 is $(4, 0, 7)$, the sales of shop $S_1$. Column 2 has the entries $0$ and $5$, the sales of product $P_2$.
4. The entry $0$ in position $(1, 2)$ must be written, because every position of a matrix needs an entry by the [[definition|0N1MY1T0W9]].
5. The entry $a_{31}$ does not exist, because $A$ has only 2 rows.

## Remarks

The meaning of the rows is our choice.
With one row for each product we get the $3 \times 2$ matrix
$$\begin{pmatrix} 4 & 2 \\ 0 & 5 \\ 7 & 1 \end{pmatrix},$$
which holds the same data but is a different matrix, the [[transpose|09DXWYRD43]] of $A$.

The table also shows why the matrix operations are useful.
If $B$ is the $2 \times 3$ matrix of next week, the sales of both weeks together are the sum $A + B$, computed entry by entry.
If the prices of the products are $2$, $3$ and $1$, the revenue of each shop is a [[matrix-vector product|0PDVQEP0ZC]]:
$$\begin{pmatrix} 4 & 0 & 7 \\ 2 & 5 & 1 \end{pmatrix} \begin{pmatrix} 2 \\ 3 \\ 1 \end{pmatrix} = \begin{pmatrix} 8 + 0 + 7 \\ 4 + 15 + 1 \end{pmatrix} = \begin{pmatrix} 15 \\ 20 \end{pmatrix}.$$
Check: shop $S_2$ sells $2$ units at $2$, $5$ units at $3$ and $1$ unit at $1$, which is $4 + 15 + 1 = 20$.

## Explanations

### L1 human

A matrix is a neat way to store a table of numbers.
Here each row is a shop and each column is a product.
To read how many units of product 3 shop 1 sold, look in row 1 and column 3, and you find $7$.

### L2 human

The size $2 \times 3$ says that there are 2 shops and 3 products, rows first.
The column sums $6$, $5$ and $8$ give the total sales of each product, and the row sums $11$ and $8$ give the total sales of each shop.
Watch out: if you swap the roles of rows and columns, you get the transpose, and then the row sums answer the other question.
