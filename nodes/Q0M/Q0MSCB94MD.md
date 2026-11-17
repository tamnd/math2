---
tag: Q0MSCB94MD
kind: example
name: Colouring proof that the 10 by 10 board has no tiling by 1 by 4 bars
msc: ["00A35", "05B45"]
topics: [GB14W4SYPK]
audience: school
instance_of: [90Q4PK1CST]
uses: [90Q4PK1CST, 0WAY5WX8NY]
sources:
  - url: https://en.wikipedia.org/wiki/De_Bruijn%27s_theorem
    locator: A generalization
---

## Example

We show that the $10 \times 10$ board cannot be tiled by bars of size $1 \times 4$, placed horizontally or vertically.
Number the rows and columns $1$ to $10$, and give the cell $(i, j)$ the colour $(i + j) \bmod 4$, one of $0, 1, 2, 3$.

1. A horizontal bar covers the cells $(i, j), (i, j + 1), (i, j + 2), (i, j + 3)$. Their values of $i + j$ are four consecutive integers, so they have four different remainders modulo $4$. So the bar covers one cell of each colour.
2. A vertical bar covers $(i, j), (i + 1, j), (i + 2, j), (i + 3, j)$, and the same reason gives one cell of each colour.
3. A tiling would use $100 / 4 = 25$ bars. By steps 1 and 2 it would cover exactly $25$ cells of each colour.
4. We count the cells of colour $3$. Among $1, \ldots, 10$, the remainders $0, 1, 2, 3$ modulo $4$ occur $2, 3, 3, 2$ times.
5. The sum $i + j$ has remainder $3$ when the remainders of $(i, j)$ are $(0, 3)$, $(1, 2)$, $(2, 1)$ or $(3, 0)$. This gives $2 \cdot 2 + 3 \cdot 3 + 3 \cdot 3 + 2 \cdot 2 = 26$ cells.
6. The board has $26$ cells of colour $3$, not $25$. So no tiling exists.

The same count gives $25$, $24$ and $25$ cells of the colours $0$, $1$ and $2$.

## Remarks

The example shows a [[colouring proof|90Q4PK1CST]] with more than two colours.
The diagonal colouring by [[congruence modulo 4|0WAY5WX8NY]] fits the bar: any four cells in a line get four different colours.
The number of cells, $100$, is a multiple of $4$, and the chessboard colouring gives $50$ and $50$, so both of these coarser counts find no obstruction.

The answer changes with the size of the board.
The $8 \times 8$ and $10 \times 12$ boards have tilings, by rows of $1 \times 4$ bars along a side whose length is a multiple of $4$.
In general, an $m \times n$ board has a tiling by $1 \times k$ bars exactly when $k$ divides $m$ or $k$ divides $n$.
A computer search confirms this for $k = 3$ and $k = 4$ and all boards up to $8 \times 8$.

## Explanations

### L1 human

Paint the board with four colours along the diagonals, in the repeating order $0, 1, 2, 3$.
Any bar of four cells in a row or a column then covers each colour exactly once.
So $25$ bars would cover $25$ cells of each colour.
A count shows that the board has $26$ cells of one colour.
So the bars can never fit exactly.

### L2 human

We check the counts of step 5 for colour $1$.

1. The sum $i + j$ has remainder $1$ when the remainders of $(i, j)$ are $(0, 1)$, $(1, 0)$, $(2, 3)$ or $(3, 2)$.
2. The counts are $2 \cdot 3 + 3 \cdot 2 + 3 \cdot 2 + 2 \cdot 3 = 24$.
3. So the board also has too few cells of colour $1$, which confirms the result.
4. The four counts $25 + 24 + 25 + 26 = 100$ add up to the number of cells, as they must.

The typical use is a colouring whose period equals the length of the piece.
The trap is to stop at the chessboard colouring, which gives equal counts here and proves nothing.
