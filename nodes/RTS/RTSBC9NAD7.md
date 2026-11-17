---
tag: RTSBC9NAD7
kind: example
name: The 15 puzzle with 14 and 15 swapped cannot be solved
msc: ["00A35", "05A05", "20B30"]
topics: [GB14W4SYPK]
audience: school
instance_of: [8NQ190278Y]
uses: [8NQ190278Y, 02DKV69ZH0, 02DTRYKGE8, 05RWFKVTJ7]
sources:
  - url: https://en.wikipedia.org/wiki/15_puzzle
    locator: Solvability
  - url: https://en.wikipedia.org/wiki/Parity_of_a_permutation
    locator: lead section
---

## Example

The 15 puzzle has a board of $4 \times 4$ cells, $15$ tiles numbered $1$ to $15$, and one empty cell, the blank.
A move slides a tile that is next to the blank, in the same row or the same column, into the blank.
The home position has the tiles $1$ to $15$ in reading order and the blank in the bottom right cell.
Loyd's position is the home position with the tiles $14$ and $15$ swapped.
We show with an [[invariant|8NQ190278Y]] that no sequence of moves changes Loyd's position into the home position.

1. We number the cells $1$ to $16$ in reading order, so that cell $16$ is the bottom right cell. We treat the blank as a tile with the number $16$.
2. An arrangement is then a [[permutation|05RWFKVTJ7]] $\sigma$ of $\set{1, \dots, 16}$, where $\sigma(c)$ is the number of the tile in cell $c$.
3. A move exchanges the blank with one tile in a neighbouring cell. So the new arrangement is $\sigma$ followed by a [[transposition|02DTRYKGE8]] of two numbers, and the [[sign|02DKV69ZH0]] of $\sigma$ changes.
4. Let $d$ be the number of rows plus the number of columns from the cell of the blank to cell $16$. A move changes the row or the column of the blank by exactly $1$, so it changes $d$ by $1$ or $-1$.
5. Let $I$ be the parity of $\sigma$ plus the parity of $d$, modulo $2$. By steps 3 and 4, each move changes both parities. So each move keeps $I$, and $I$ is an invariant.
6. In the home position, $\sigma$ is the identity, which is even, and $d = 0$. So $I = 0 + 0 = 0$.
7. In Loyd's position, $\sigma$ is the transposition of the numbers $14$ and $15$, which is odd, and $d = 0$. So $I = 1 + 0 = 1$.
8. The values in steps 6 and 7 differ. So no sequence of moves leads from Loyd's position to the home position, and the puzzle cannot be solved.

## Remarks

The example shows the typical shape of an invariant proof: one computation at the start and one at the target rule out every sequence of moves.
Each of the two parts of $I$ changes at each move, so neither part alone is an invariant.
The sum of the two parts is the invariant.

The invariant splits the $16!$ arrangements into two classes of equal size, $10461394944000$ each.
Swapping the tiles $1$ and $2$ changes $I$ and is a bijection between the two classes.
The converse also holds: each arrangement with $I = 0$ can be solved.
This converse needs a separate proof by construction, and the invariant alone does not give it.

A change of the position changes the answer.
If the tiles $14$ and $15$ are swapped and the blank is moved to a cell with odd $d$, for example the cell above cell $16$, then $I = 1 + 1 = 0$.
This position can be solved, by the converse.
For the $3 \times 3$ board with $8$ tiles, the same invariant works, and a computer search finds exactly $9!/2 = 181440$ arrangements that can be reached from the home position.

## Explanations

### L1 human

The 15 puzzle is a box of sliding tiles with one empty space.
In a famous version, the tiles $14$ and $15$ are in the wrong order, and every other tile is in its place.
Each slide moves the empty space by one step, and it also swaps the empty space with one tile.
A careful count shows that two "even or odd" labels both flip at each slide, so together they never change.
The solved puzzle and the famous version have different labels.
So no amount of sliding can solve the famous version.

### L2 human

We decide whether two arrangements can be solved.
We use the fact that the parity of a permutation equals the parity of its number of inversions, that is, of the pairs of positions in the wrong order.

1. Arrangement A: the tiles $15, 14, \dots, 1$ fill cells $1$ to $15$, and the blank is in cell $16$.
2. The sequence $15, 14, \dots, 1, 16$ has $15 \cdot 14 / 2 = 105$ inversions, since each pair of the first $15$ entries is in the wrong order. So $\sigma$ is odd.
3. The blank is in cell $16$, so $d = 0$. Then $I = 1 + 0 = 1$, and arrangement A cannot be solved.
4. Arrangement B: the blank is in cell $1$, and the tiles $15, 14, \dots, 1$ fill cells $2$ to $16$.
5. The sequence $16, 15, \dots, 1$ has $16 \cdot 15 / 2 = 120$ inversions. So $\sigma$ is even.
6. The blank is $3$ rows and $3$ columns away from cell $16$, so $d = 6$, which is even. Then $I = 0 + 0 = 0$.
7. The invariant does not rule out arrangement B, and by the converse of the remarks it can be solved.

The typical use is a quick test of a position before any search for a solution.
A trap is to count only the parity of the tiles and to forget the position of the blank.
That count alone changes at each move, so it decides nothing.
