---
tag: 90Q4PK1CST
kind: concept
name: Coloring proofs
aliases: [coloring-proofs, colouring-proofs]
msc: ["00A35", "05B45"]
topics: [G9JFJGY4TQ, GB14W4SYPK]
audience: school
uses: [83PJCPB9VA, H9JT1XNDKQ, 0WAY5WX8NY]
sources:
  - url: https://en.wikipedia.org/wiki/Mutilated_chessboard_problem
    locator: Solution
  - url: https://en.wikipedia.org/wiki/Mutilated_chessboard_problem
    locator: History
  - url: https://en.wikipedia.org/wiki/Tetromino
    locator: Filling a rectangle
  - url: https://en.wikipedia.org/wiki/De_Bruijn%27s_theorem
    locator: Example
---

## Summary

A coloring proof paints the cells of a region so that every piece covers the same colors wherever you put it.
Then a count of colors shows that the pieces cannot fill the region.

The standard first problem is the mutilated chessboard.
Remove two opposite corners from an $8 \times 8$ chessboard; can $31$ dominoes cover the remaining $62$ cells?
The two removed corners have the same color, so the board keeps $32$ cells of one color and $30$ of the other.
A domino always covers two neighboring cells, one of each color, so $31$ dominoes cover $31$ cells of each color.
The counts do not match, so no tiling exists, and the [[full proof|TXNHA1AHYV]] writes out every step.

In general, a coloring of a region $R$ with $k$ colors is a function $c : R \to \{0, 1, \dots, k - 1\}$.
It suits a set of pieces when every piece, in every position and orientation that the problem allows, covers a fixed number of cells of each color.
Then the color counts of any tiling are sums of these fixed counts.
If the color counts of $R$ are not such a sum, no tiling exists.

## Motivation

A region of $62$ cells may have no tiling by $31$ dominoes, and the number $62$ does not show why.
A search over all placements of $31$ dominoes is far too long by hand.
A [[parity argument|H9JT1XNDKQ]] on the number of cells sees only the total, while a coloring sees how the total splits.
That finer count decides many problems that the total cannot decide.

The coloring defines an [[invariant|8NQ190278Y]]: placing a piece adds the same color counts whatever the position, so the counts of a tiling depend only on the number of pieces.
It is the standard tool for the impossibility of [[domino tilings|83PJCPB9VA]] and of tilings by larger polyominoes.
The same counting rules out paths: a walk on the grid that changes color at each step must alternate colors.

## Notation

The cell in row $i$ and column $j$ is written $(i, j)$, with rows and columns numbered from $1$.
The chessboard coloring is $c(i, j) = (i + j) \bmod 2$; we call the value $0$ black and the value $1$ white.
The diagonal coloring with $k$ colors is $c(i, j) = (i + j) \bmod k$, which uses [[congruence modulo n|0WAY5WX8NY]].
Books also write "checkerboard coloring" for the chessboard coloring.

## Remarks

### How to choose the coloring

The coloring must make every piece look the same.
For a domino, the chessboard coloring works, because two cells that share a side have values of $i + j$ that differ by $1$.
For a bar of length $k$, the diagonal coloring $(i + j) \bmod k$ works, because the $k$ cells of a bar have $k$ consecutive values of $i + j$, one of each remainder.
So the rule of thumb is to match the period of the coloring to the length of the piece.

The $10 \times 10$ board shows why the period matters.
With $1 \times 4$ bars, the chessboard coloring gives $50$ black and $50$ white cells, and each bar covers $2$ and $2$, so it finds nothing, as [[the chessboard attempt|390WNM7BSA]] shows.
The coloring $(i + j) \bmod 4$ gives one cell of each color per bar and the counts $25$, $24$, $25$ and $26$ for the colors $0$ to $3$, so $25$ bars cannot fit; the [[full proof|Q0MSCB94MD]] gives the counts.

### More colorings at work

The five tetrominoes, straight, square, T, S and L, each used once, do not tile a $4 \times 5$ rectangle.
In the chessboard coloring, the T covers $3$ cells of one color and $1$ of the other, and each other piece covers $2$ and $2$.
So the five pieces cover $11$ cells of one color and $9$ of the other, while the rectangle has $10$ and $10$; the L2 explanation gives the details.

A piece that moves one cell up, down, left or right cannot visit all $64$ cells of a chessboard exactly once, starting at one corner and ending at the opposite corner.
Each move changes the color, and the path makes $63$ moves, so the last cell has the other color from the first.
Opposite corners have the same color, so such a [[Hamiltonian path|AT8GWPWQWT]] does not exist.

The idea also works in three dimensions.
A $6 \times 6 \times 6$ box cannot be filled with $1 \times 2 \times 4$ bricks, and the proof colors the unit cubes in a pattern chosen for the brick.

### What a coloring cannot do

Equal color counts do not prove that a tiling exists.
The six cells $(1, 2)$, $(2, 1)$, $(2, 2)$, $(2, 3)$, $(2, 4)$ and $(3, 3)$ form a region with $3$ black and $3$ white cells.
It has no domino tiling, because $(1, 2)$ and $(2, 1)$ both have $(2, 2)$ as their only neighbor in the region, and one domino cannot cover all three.

A coloring in which a piece covers different counts in different positions gives no direct argument.
If you color each cell by the parity of its row, a vertical domino covers one cell of each color, but a horizontal domino covers two cells of one color.

### The graph behind the chessboard

The chessboard coloring is a proper coloring of the grid graph with $2$ colors, so the grid graph is a [[bipartite graph|0ZVQKTRKVQ]] with [[chromatic number|0C5M7AM6FH]] $2$.
A domino tiling of a region is a [[perfect matching|0NHK9MFFW9]] of its graph, and a bipartite graph with a perfect matching has two classes of equal size.
For the $8 \times 8$ board with two cells removed, that count is the only obstruction.
Gomory's theorem says that the board without any black cell and any white cell always has a domino tiling.

### The steps

1. Fix the region and the pieces, with the positions and orientations that the problem allows.
2. Choose a coloring, often $(i + j) \bmod k$ or a pattern of blocks, so that each piece covers a fixed number of cells of each color.
3. Count the cells of each color in the region.
4. Show that the counts of step 3 are not a sum of the counts of the pieces.
   Then no tiling exists.

### Watch out

The first common error is to forget an orientation.
A coloring by $(i + j) \bmod 4$ suits a straight bar in both directions, but it does not suit an L tetromino, whose cells take the values $s, s + 1, s + 2, s + 3$ of $i + j$ in one orientation and $s, s + 1, s + 1, s + 2$ in another.
So check every position and every orientation before you count.

The second error is to read equal counts as a proof that a tiling exists; the six-cell region above has equal counts and no tiling.
The third error is to use the chessboard coloring for every problem, as the $1 \times 4$ bars on the $10 \times 10$ board show.

### History

The philosopher Max Black posed the mutilated chessboard problem in his book "Critical Thinking" (1946).
Solomon Golomb discussed it in 1954, and Martin Gardner wrote about it in his "Mathematical Games" column in Scientific American.
Ralph Gomory proved that the removal of any two cells of different colors from the chessboard leaves a region that dominoes can tile.

### Try it

Can a $5 \times 5$ board with its center cell removed be tiled by dominoes?
In the chessboard coloring the board has $13$ cells with $i + j$ even and $12$ with $i + j$ odd, and the center $(3, 3)$ has an even sum, so the rest has $12$ and $12$.
The coloring does not forbid a tiling, and one exists: the rest splits into four $2 \times 3$ blocks around the center, and each block takes three dominoes.

Which single cell of the $5 \times 5$ board can you remove so that the rest might have a domino tiling?
Only a cell with $i + j$ even: removing a cell with $i + j$ odd leaves $13$ cells of one color and $11$ of the other.

## Explanations

### L1 human

Paint a chessboard in its usual black and white pattern.
A domino always covers two squares side by side, so it always covers one black square and one white square.
So any set of dominoes covers as many black squares as white squares.
Now cut off two opposite corners of the board, which have the same color, say white.
The rest has $32$ black and $30$ white squares, and no set of dominoes can cover it exactly.
The colors turn a hard puzzle into a quick count.

### L2 human

We show that the $4 \times 5$ rectangle cannot be tiled by the five tetrominoes, each used once.
Color the cell $(i, j)$ black when $i + j$ is even and white otherwise.
The rectangle has $4$ rows of $5$ cells, and the rows have $3, 2, 3, 2$ black cells, so it has $10$ black and $10$ white cells.

Two cells side by side have different colors, so a domino covers one black and one white cell.
The straight, square, S and L tetrominoes each split into two dominoes, in every orientation, so each covers $2$ black and $2$ white cells.
The T tetromino has a center cell that shares a side with each of the other three cells, so those three cells have the color opposite to the center.
So the T covers $3$ cells of one color and $1$ of the other, and the five pieces together cover
$$2 + 2 + 2 + 2 + 3 = 11$$
cells of one color and $9$ of the other.
That differs from $10$ and $10$, so no tiling exists.

The method gives a quick impossibility proof before any search.
Watch out: you must check each piece in every orientation, and the T is the one piece that cannot split into two dominoes, which is why it breaks the balance.

### L3 human

A coloring with $k$ colors sends each cell to a basis vector of $\mathbb{Z}^k$, and a region to the sum of the vectors of its cells.
A tiling is impossible when the vector of the region is not a sum of vectors of placed pieces.
More general weights give stronger invariants.
The coloring $(i + j) \bmod k$ is a shadow of the weight $x^i y^j$, with $x$ and $y$ complex roots of unity.
That weight proves that an $m \times n$ rectangle has a tiling by $1 \times k$ bars only when $k$ divides $m$ or $k$ divides $n$.
Conway and Lagarias, and later Thurston, replaced colors by elements of a group given by generators and relations, the tiling group of a set of pieces.

In graph theory, the two-color count is the simplest obstruction to a perfect matching in a bipartite graph, and [[Hall's marriage theorem|08WCB90WND]] lists all the obstructions, one for each set of vertices with too few neighbors.
The [[domino tiling|83PJCPB9VA]] concept and the topic on [[polyominoes and combinatorial tilings|CQJPRK86KN]] treat the counting and the structure of tilings, and the topic on [[chessboard problems|WPGRNSZ1ZN]] lists related puzzles.
Coloring proofs are a special case of [[invariants|8NQ190278Y]], and the two-color case is close to a [[parity argument|H9JT1XNDKQ]].
