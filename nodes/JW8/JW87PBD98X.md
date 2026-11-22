---
tag: JW87PBD98X
kind: example
name: The cell count does not decide the 4 by 4 board without two opposite corners
msc: ["00A35", "05B45"]
topics: [GB14W4SYPK]
audience: school
instance_of: [90Q4PK1CST]
not_instance_of:
  - target: H9JT1XNDKQ
    note: the region has 14 cells, an even number, so the parity of the cell count agrees with any domino tiling and gives no contradiction
uses: [H9JT1XNDKQ, 90Q4PK1CST, 83PJCPB9VA]
sources:
  - url: https://en.wikipedia.org/wiki/Mutilated_chessboard_problem
    locator: Solution
---

## Example

Let $R$ be the $4 \times 4$ board with the two opposite corner cells, top left and bottom right, removed.
We ask whether $R$ has a [[domino tiling|83PJCPB9VA]], and we first test the [[parity argument|H9JT1XNDKQ]] on the number of cells.

1. The board $R$ has $16 - 2 = 14$ cells.
2. A tiling by $k$ dominoes covers $2k$ cells, so a tiling needs an even number of cells, and $14 = 2 \cdot 7$ is even.
3. So the parity of the cell count allows a tiling by $7$ dominoes, and the parity argument gives no contradiction.
4. Still, $R$ has no tiling.
   To see why, color the cell in row $r$ and column $c$ black when $r + c$ is even and white when $r + c$ is odd, with rows and columns numbered $1$ to $4$.
5. The full board has $8$ black and $8$ white cells.
   The removed corners $(1, 1)$ and $(4, 4)$ have $r + c = 2$ and $r + c = 8$, so both are black.
6. So $R$ has $6$ black and $8$ white cells.
7. Each domino covers two neighboring cells, whose values of $r + c$ differ by $1$, so each domino covers one black and one white cell.
8. Then $7$ dominoes would cover $7$ black cells, but $R$ has only $6$, so $R$ has no domino tiling.

## Remarks

The example shows the limit of a parity argument: an even cell count is necessary for a tiling, and it is not sufficient.
The obstruction in $R$ is a difference of $2$ between the two color classes, and a count of all cells cannot see it.
The [[coloring proof|90Q4PK1CST]] of steps 4 to 8 refines the count by counting the cells of each color.
The same method decides the $8 \times 8$ case, in the [[coloring proof for the mutilated chessboard|TXNHA1AHYV]].

The answer changes when we remove two cells of different colors, for example $(1, 1)$ and $(1, 2)$.
Then the remaining $14$ cells form a $3 \times 4$ block and a $1 \times 2$ strip, which take $6$ dominoes and $1$ domino.

## Explanations

### L1 human

Cut two opposite corners off a $4 \times 4$ board, so $14$ squares are left.
Fourteen is even, so the count does not forbid a covering by $7$ dominoes.
Yet every attempt fails.
The reason appears only when we color the board like a chessboard: the two removed corners have the same color.
So one color has $6$ squares and the other has $8$, while each domino covers one square of each color.

### L2 human

We sort what each test can and cannot show for the region $R$.
The parity of the cell count passes, since $14$ is even, so it proves nothing.
The color count fails, since $6$ black and $8$ white cells are not equal, and a failed test proves that no tiling exists.
A test that passes never proves existence, and a test that fails proves impossibility.

So choose the coarsest invariant that still separates the target from what the pieces can cover.
Watch out: the wrong conclusion "the count is even, so a tiling exists" is the most common error with such boards.
