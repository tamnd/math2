---
tag: H817ES7NHH
kind: example
name: Counting the squares on a chessboard by the four steps
msc: ["00A35", "05A15"]
topics: [X1NSTVGDNQ]
audience: school
instance_of: [DYD57G2Y5Z]
uses: [DYD57G2Y5Z]
sources:
  - url: https://en.wikipedia.org/wiki/Square_pyramidal_number
    locator: lead section
---

## Example

Problem: how many squares of all sizes can be drawn along the grid lines of an $8 \times 8$ chessboard?
We use [[Pólya's four steps|DYD57G2Y5Z]].

Phase 1: understand the problem.

1. The unknown is a number of squares.
2. The data: the board has $8$ rows and $8$ columns of unit cells.
3. The condition: a square counts when its sides lie on grid lines. So squares of side $1, 2, \ldots, 8$ all count, not only the $64$ cells.
4. A small case shows the meaning: a $2 \times 2$ board has $4$ unit squares and $1$ square of side $2$, so $5$ squares.

Phase 2: devise a plan.

1. Split by size: count the squares of side $k$ for each $k$ from $1$ to $8$, and add.
2. A square of side $k$ is fixed by the position of its top left corner.

Phase 3: carry out the plan.

1. For a square of side $k$, the top left corner can be in any of the first $9 - k$ columns, since the square needs $k$ columns to its right, including its own.
2. In the same way, the corner can be in any of the first $9 - k$ rows.
3. So there are $(9 - k)^2$ squares of side $k$.
4. The total is $8^2 + 7^2 + \cdots + 1^2 = 64 + 49 + 36 + 25 + 16 + 9 + 4 + 1 = 204$.

Phase 4: look back.

1. Check by the small case: for a $2 \times 2$ board the method gives $2^2 + 1^2 = 5$, as counted in phase 1.
2. Check by the largest size: the formula gives $(9 - 8)^2 = 1$ square of side $8$, the whole board.
3. Generalize the result: an $n \times n$ board has $1^2 + 2^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6}$ squares. For $n = 8$ this is $\frac{8 \cdot 9 \cdot 17}{6} = 204$.
4. A new problem: how many rectangles does the board have? The page [[problem posing|Y896GWYF8A]] continues with it.

## Remarks

Phase 1 decided the problem: a solver who skips it may answer $64$, the number of cells.
Phase 2 used the heuristic "split the problem into cases", which is [[decomposing and recombining|KEZPDNM2NH]].
For an $m \times n$ board with $m \le n$, the same plan gives $\sum_{k=1}^{m} (m - k + 1)(n - k + 1)$ squares.

## Explanations

### L1 human

A chessboard has $64$ small squares, but it also has bigger squares made of several small ones.
There are $49$ squares of side $2$, because such a square can start in $7$ places across and $7$ places down.
In the same way there are $36$ squares of side $3$, and so on, down to $1$ square of side $8$.
Adding $64 + 49 + 36 + 25 + 16 + 9 + 4 + 1$ gives $204$.

### L2 human

We use the general formula of phase 4 for a $3 \times 5$ board.

1. Sizes: the side $k$ can be $1$, $2$ or $3$.
2. Side $1$: $3 \cdot 5 = 15$ squares. Side $2$: $2 \cdot 4 = 8$ squares. Side $3$: $1 \cdot 3 = 3$ squares.
3. Total: $15 + 8 + 3 = 26$.

The typical use: the four steps turn a counting puzzle into a formula that answers a family of puzzles.

A trap: the count of positions in phase 3, step 1, is $9 - k$, not $8 - k$; a check with $k = 8$, where there is exactly one position, catches the error.
