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

How many squares of all sizes can be drawn along the grid lines of an $8 \times 8$ chessboard?
We follow [[Pólya's four steps|DYD57G2Y5Z]].

In phase 1 we understand the problem.

1. The unknown is a number of squares.
2. The data are the $8$ rows and $8$ columns of unit cells.
3. A square counts when its sides lie on grid lines, so squares of side $1, 2, \dots, 8$ all count, not only the $64$ cells.
4. A small case shows what this means: a $2 \times 2$ board has $4$ unit squares and $1$ square of side $2$, so $5$ squares in all.

In phase 2 we devise a plan.

1. We split by size: count the squares of side $k$ for each $k$ from $1$ to $8$, and add.
2. A square of side $k$ is fixed by the position of its top left corner, so we count corners.

In phase 3 we carry out the plan.

1. The top left corner of a square of side $k$ can be in any of the first $9 - k$ columns, since the square needs $k$ columns, counting its own.
2. In the same way, the corner can be in any of the first $9 - k$ rows.
3. So there are $(9 - k)^2$ squares of side $k$.
4. The total is
   $$8^2 + 7^2 + \dots + 1^2 = 64 + 49 + 36 + 25 + 16 + 9 + 4 + 1 = 204.$$

In phase 4 we look back.

1. The small case checks out: for a $2 \times 2$ board the same method gives $2^2 + 1^2 = 5$.
2. The largest size checks out: there is $(9 - 8)^2 = 1$ square of side $8$, the whole board.
3. An $n \times n$ board has
   $$1^2 + 2^2 + \dots + n^2 = \frac{n(n+1)(2n+1)}{6}$$
   squares, and for $n = 8$ this is $\frac{8 \cdot 9 \cdot 17}{6} = 204$.
4. A new question comes up: how many rectangles does the board have?
   [[Problem posing|Y896GWYF8A]] continues with it.

## Remarks

Phase 1 decided the problem, because a solver who skips it answers $64$, the number of cells.
Phase 2 split the problem into cases by size, which is the heuristic of [[decomposing and recombining|KEZPDNM2NH]].
The same plan works for a board that is not square.
For an $m \times n$ board with $m \le n$, a square of side $k$ has $(m - k + 1)(n - k + 1)$ positions, and the total is the sum of these numbers for $k = 1, \dots, m$.

## Explanations

### L1 human

A chessboard has $64$ small squares, and it also has bigger squares made of several small ones.
There are $49$ squares of side $2$, because such a square can start in $7$ places across and $7$ places down.
In the same way there are $36$ squares of side $3$, and so on, down to $1$ square of side $8$.
Adding $64 + 49 + 36 + 25 + 16 + 9 + 4 + 1$ gives $204$.

### L2 human

We use the formula for an $m \times n$ board on a $3 \times 5$ board.
The side $k$ can be $1$, $2$ or $3$.
Side $1$ gives $3 \cdot 5 = 15$ squares, side $2$ gives $2 \cdot 4 = 8$, and side $3$ gives $1 \cdot 3 = 3$.
So the board has
$$15 + 8 + 3 = 26$$
squares.
The four phases turned one puzzle into a formula for a family of puzzles.
Watch out: the number of positions in phase 3 is $9 - k$, not $8 - k$, and the check with $k = 8$, which has exactly one position, catches that error.
