---
tag: 390WNM7BSA
kind: example
name: The chessboard coloring does not decide the 10 by 10 board with 1 by 4 bars
aliases: [the-chessboard-colouring-does-not-decide-the-10-by-10-board-with-1-by-4-bars]
msc: ["00A35", "05B45"]
topics: [GB14W4SYPK]
audience: school
not_instance_of:
  - target: 90Q4PK1CST
    note: each bar covers 2 black and 2 white cells and the board has 50 of each, so the chessboard coloring gives no contradiction
uses: [90Q4PK1CST, Q0MSCB94MD]
sources:
  - url: https://en.wikipedia.org/wiki/Mutilated_chessboard_problem
    locator: Solution
---

## Example

We ask whether the $10 \times 10$ board has a tiling by $1 \times 4$ bars, and we try the chessboard coloring.
Call the cell $(i, j)$ black when $i + j$ is even and white when $i + j$ is odd.

1. A bar covers four cells in a line, and the colors alternate along a line.
   So each bar covers $2$ black and $2$ white cells, in every position.
2. A tiling would use $25$ bars, which cover $50$ black and $50$ white cells.
3. Each row of the board has $5$ black and $5$ white cells, so the board has $50$ black and $50$ white cells.
4. The counts of steps 2 and 3 agree.
   So the chessboard coloring gives no contradiction, and it does not prove that the tiling is impossible.
5. It does not prove that a tiling exists either.
   In fact no tiling exists, as the [[coloring with four colors|Q0MSCB94MD]] shows.

## Remarks

The example shows the limit of a single coloring in a [[coloring proof|90Q4PK1CST]].
A coloring gives only a necessary condition, and the chessboard coloring is too coarse for bars of length $4$, because it repeats every $2$ cells.
The coloring $(i + j) \bmod 4$ gives the four cells of a bar four different colors and finds the obstruction.

The situation changes when the pieces or the board change.
For $1 \times 2$ dominoes on the same board, the chessboard coloring is the natural choice, and a tiling exists, with $5$ horizontal dominoes in each row.
For $1 \times 4$ bars on the $10 \times 12$ board, the chessboard counts also agree, and here a tiling exists, with $3$ horizontal bars in each row.
So equal counts can come with a tiling or without one.

## Explanations

### L1 human

Color the board like a chessboard and lay a bar of four cells on it.
The bar always covers two black and two white squares.
The board has $50$ black and $50$ white squares, so the colors balance.
This test finds no problem, but the tiling is still impossible.
A finer coloring with four colors is needed to see why.

### L2 human

We compare three tests on the $10 \times 10$ board with $1 \times 4$ bars.
The count of cells is $100$, a multiple of $4$, so it finds no obstruction.
The chessboard coloring gives $50$ and $50$, with $2$ and $2$ per bar, so it finds none either.
The coloring by $(i + j) \bmod 4$ gives the counts $25$, $24$, $25$ and $26$, with one cell of each color per bar, and that finds the obstruction.

So the period of the coloring should match the length of the piece.
Watch out: a test that finds nothing is not a proof that a tiling exists, and the second test here passes although no tiling exists.
