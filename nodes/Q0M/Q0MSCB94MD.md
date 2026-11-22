---
tag: Q0MSCB94MD
kind: example
name: Coloring proof that the 10 by 10 board has no tiling by 1 by 4 bars
aliases: [colouring-proof-that-the-10-by-10-board-has-no-tiling-by-1-by-4-bars]
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
Number the rows and columns $1$ to $10$, and give the cell $(i, j)$ the color $(i + j) \bmod 4$, one of $0, 1, 2, 3$.

1. A horizontal bar covers the cells $(i, j), (i, j + 1), (i, j + 2), (i, j + 3)$.
   Their values of $i + j$ are four consecutive integers, so they have four different remainders modulo $4$, and the bar covers one cell of each color.
2. A vertical bar covers $(i, j), (i + 1, j), (i + 2, j), (i + 3, j)$, and the same reason gives one cell of each color.
3. A tiling would use $100 / 4 = 25$ bars, and by steps 1 and 2 it would cover exactly $25$ cells of each color.
4. Among $1, \dots, 10$, the remainders $0, 1, 2, 3$ modulo $4$ occur $2, 3, 3, 2$ times: remainder $0$ for $4, 8$, remainder $1$ for $1, 5, 9$, remainder $2$ for $2, 6, 10$, and remainder $3$ for $3, 7$.
5. The sum $i + j$ has remainder $3$ when the remainders of $i$ and $j$ are $(0, 3)$, $(1, 2)$, $(2, 1)$ or $(3, 0)$, so the number of cells of color $3$ is
   $$2 \cdot 2 + 3 \cdot 3 + 3 \cdot 3 + 2 \cdot 2 = 26.$$
6. The board has $26$ cells of color $3$, not $25$, so no tiling exists.

The same count gives $25$, $24$ and $25$ cells of the colors $0$, $1$ and $2$.
Check: $25 + 24 + 25 + 26 = 100$.

## Remarks

The example shows a [[coloring proof|90Q4PK1CST]] with more than two colors.
The diagonal coloring by [[congruence modulo 4|0WAY5WX8NY]] fits the bar: any four cells in a line get four different colors.
The number of cells, $100$, is a multiple of $4$, and the chessboard coloring gives $50$ and $50$, so both of these coarser counts find no obstruction.

The labels of the colors depend on where you start the numbering.
With rows and columns numbered $0$ to $9$, the same coloring gives $25$, $26$, $25$ and $24$ cells of the colors $0$ to $3$; the four counts are the same multiset, and the proof does not change.

The answer changes with the size of the board.
The $8 \times 8$ and $10 \times 12$ boards have tilings by $1 \times 4$ bars, laid along a side whose length is a multiple of $4$.
In general, an $m \times n$ board has a tiling by $1 \times k$ bars exactly when $k$ divides $m$ or $k$ divides $n$.

## Explanations

### L1 human

Paint the board with four colors along the diagonals, in the repeating order $0, 1, 2, 3$.
Any bar of four cells in a row or a column then covers each color exactly once.
So $25$ bars would cover $25$ cells of each color.
A count shows that the board has $26$ cells of one color.
So the bars can never fit exactly.

### L2 human

We check the count for color $1$.
The sum $i + j$ has remainder $1$ when the remainders of $i$ and $j$ are $(0, 1)$, $(1, 0)$, $(2, 3)$ or $(3, 2)$.
With the counts $2, 3, 3, 2$ of step 4, the number of cells of color $1$ is
$$2 \cdot 3 + 3 \cdot 2 + 3 \cdot 2 + 2 \cdot 3 = 24.$$
So the board also has too few cells of color $1$, which confirms the result.

The lesson is to choose a coloring whose period equals the length of the piece.
Watch out: the chessboard coloring gives equal counts here and proves nothing, so a student who stops there may wrongly think that a tiling exists.
