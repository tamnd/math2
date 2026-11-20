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
In one week, shop $S_1$ sells $4$, $0$ and $7$ units, and shop $S_2$ sells $2$, $5$ and $1$ units.
We record the data as a [[matrix|0VD9ZSWWJG]] $A$ with one row for each shop and one column for each product.

1. The table has 2 rows and 3 columns, so $A$ is a $2 \times 3$ matrix:
$$A = \begin{pmatrix} 4 & 0 & 7 \\ 2 & 5 & 1 \end{pmatrix}.$$
2. The entry $a_{ij}$ is the number of units of $P_j$ sold in $S_i$. For example, $a_{13} = 7$ and $a_{22} = 5$.
3. Row 1 is $(4, 0, 7)$, the sales of shop $S_1$. Column 2 is $(0, 5)$, the sales of product $P_2$.
4. The entry $a_{31}$ does not exist, because $A$ has only 2 rows.
5. If we use one row for each product, we get the $3 \times 2$ matrix $\begin{pmatrix} 4 & 2 \\ 0 & 5 \\ 7 & 1 \end{pmatrix}$. This is a different matrix, the [[transpose|09DXWYRD43]] of $A$.

## Remarks

The data of next week give a second $2 \times 3$ matrix $B$, and the sales of the two weeks together are the sum $A + B$.
If the prices of the products are $p = (p_1, p_2, p_3)$, the revenue of the shops is the [[matrix-vector product|0PDVQEP0ZC]] $Ap$.

## Explanations

### L1 human

A matrix is a way to store a table of numbers.
Here each row is a shop and each column is a product.
To read the number of units of product 3 in shop 1, we look in row 1 and column 3.

### L2 human

The choice of what the rows mean is a convention, and the other choice gives the transpose.
The size $2 \times 3$ says that there are 2 shops and 3 products.
