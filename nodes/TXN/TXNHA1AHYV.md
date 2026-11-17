---
tag: TXNHA1AHYV
kind: example
name: Coloring proof for the mutilated chessboard
msc: ["00A35", "05B45"]
topics: [GB14W4SYPK]
audience: school
instance_of: [90Q4PK1CST]
uses: [90Q4PK1CST, 83PJCPB9VA]
sources:
  - url: https://en.wikipedia.org/wiki/Mutilated_chessboard_problem
    locator: Solution
---

## Example

Let $R$ be the $8 \times 8$ chessboard with two opposite corner cells removed.
We show that $R$ has no [[domino tiling|83PJCPB9VA]].
Number the rows and columns $1$ to $8$, and call the cell $(i, j)$ black when $i + j$ is even and white when $i + j$ is odd.

1. The full board has $64$ cells. Each row has $4$ black and $4$ white cells, so the board has $32$ black and $32$ white cells.
2. The removed corners are $(1, 1)$ and $(8, 8)$. Their sums are $2$ and $16$, both even, so both corners are black.
3. So $R$ has $32 - 2 = 30$ black cells and $32$ white cells, $62$ cells in all.
4. A domino covers two cells that share a side. Their values of $i + j$ differ by $1$, so one cell is black and the other is white.
5. A tiling of $R$ would use $62 / 2 = 31$ dominoes, which cover $31$ black and $31$ white cells.
6. But $R$ has $30$ black cells, not $31$. So no tiling exists.

The other pair of opposite corners, $(1, 8)$ and $(8, 1)$, has the sums $9$ and $9$, so both are white, and the same steps give $32$ black and $30$ white cells.

## Remarks

The example shows the [[coloring proof|90Q4PK1CST]] in its simplest form: one coloring, two counts, and one comparison.
The number of cells, $62$, is even, so a count of all cells finds no obstruction.
The coloring finds one at once, and no case analysis of the $31$ dominoes is needed.

The answer changes when the two removed cells have different colors.
For example, remove $(1, 1)$ and $(1, 2)$.
Then rows $2$ to $8$ and the rest of row $1$ have tilings by horizontal dominoes, so a tiling exists.
Gomory's theorem says that the removal of any black cell and any white cell leaves a region with a domino tiling.
The same steps work for every board of size $2n \times 2n$, since its corners $(1, 1)$ and $(2n, 2n)$ have even sums $2$ and $4n$.

## Explanations

### L1 human

A chessboard has $32$ black and $32$ white squares.
Two opposite corners have the same color, so cutting them off leaves $30$ squares of one color and $32$ of the other.
Every domino lies on one black and one white square.
So $31$ dominoes would need $31$ squares of each color.
One color has only $30$ squares, so the covering is impossible.

### L2 human

We test the same steps on the $6 \times 6$ board without the corners $(1, 1)$ and $(6, 6)$.

1. The full board has $18$ black and $18$ white cells.
2. The corners have sums $2$ and $12$, both even, so both are black.
3. The region has $16$ black and $18$ white cells, $34$ in all.
4. A tiling would use $17$ dominoes, covering $17$ cells of each color, but only $16$ black cells exist. So no tiling exists.

The typical use is a fast check before any attempt to place dominoes.
The trap is to stop at the total: $34$ is even, and the total alone shows nothing.
