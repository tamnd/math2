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
A move slides a tile that shares a side with the blank into the blank.
The home position has the tiles $1$ to $15$ in reading order and the blank in the bottom right cell.
Loyd's position is the home position with the tiles $14$ and $15$ swapped.
We show with an [[invariant|8NQ190278Y]] that no sequence of moves changes Loyd's position into the home position.

1. We number the cells $1$ to $16$ in reading order, so that cell $16$ is the bottom right cell.
   We treat the blank as a tile with the number $16$.
2. An arrangement is then a [[permutation|05RWFKVTJ7]] $\sigma$ of $\{1, \dots, 16\}$, where $\sigma(c)$ is the number of the tile in cell $c$.
3. A move exchanges the blank with one tile in a neighboring cell.
   So the new arrangement is the old one composed with a [[transposition|02DTRYKGE8]], and the [[sign|02DKV69ZH0]] of $\sigma$ changes.
4. Let $d$ be the taxicab distance from the cell of the blank to cell $16$: the number of rows plus the number of columns between them.
   A move changes the row or the column of the blank by exactly $1$, so it changes $d$ by $1$ or by $-1$, and the parity of $d$ changes.
5. Let $I$ be the parity of $\sigma$ plus the parity of $d$, modulo $2$.
   By steps 3 and 4, each move changes both parities, so each move keeps $I$, and $I$ is an invariant.
6. In the home position, $\sigma$ is the identity, which is even, and $d = 0$, so $I = 0 + 0 = 0$.
7. In Loyd's position, $\sigma$ is the transposition of $14$ and $15$, which is odd, and $d = 0$, so $I = 1 + 0 = 1$.
8. The values in steps 6 and 7 differ, so no sequence of moves leads from Loyd's position to the home position.

Check: one slide from the home position moves tile $15$ into cell $16$; then $\sigma$ is the transposition of $15$ and $16$, which is odd, and $d = 1$, so $I = 1 + 1 = 0$, as the invariant demands.

## Remarks

The example shows the shape of every invariant proof: one computation at the start and one at the target rule out all sequences of moves.
Neither part of $I$ is an invariant by itself, because each part changes at every move.
Only their sum stays fixed, and the trick is to pair two quantities that always change together.

The invariant splits the $16! = 20922789888000$ arrangements into two classes of $10461394944000$ each.
Swapping the tiles $1$ and $2$ changes $I$, and it is a bijection between the two classes.
The converse also holds: every arrangement with $I = 0$ can be solved.
That needs a separate proof by construction, and the invariant alone does not give it.

Every position that you can reach from Loyd's position has $I = 1$, wherever the blank is.
To get a position that can be solved, you must change the parity of $\sigma$ without moving the blank.
For example, swap $14$ and $15$ and also swap $12$ and $13$: then $\sigma$ is a product of two transpositions, which is even, $d = 0$, and $I = 0$.
On the $3 \times 3$ board with $8$ tiles the same invariant works, and exactly $9!/2 = 181440$ arrangements can be reached from the home position.

## Explanations

### L1 human

The 15 puzzle is a box of sliding tiles with one empty space.
In a famous version, the tiles $14$ and $15$ are in the wrong order, and every other tile is in its place.
Each slide moves the empty space by one step, and it also swaps the empty space with one tile.
Two "even or odd" labels both flip at each slide, so their combination never changes.
The solved puzzle and the famous version have different combinations.
So no amount of sliding can solve the famous version.

### L2 human

We decide whether two arrangements can be solved.
We use the fact that the parity of a permutation equals the parity of its number of inversions, the pairs of entries in the wrong order.

In arrangement A the tiles $15, 14, \dots, 1$ fill cells $1$ to $15$, and the blank is in cell $16$.
Each pair of the first $15$ entries is in the wrong order, and the final $16$ is in order with all of them, so the number of inversions is
$$\binom{15}{2} = \frac{15 \cdot 14}{2} = 105,$$
which is odd.
The blank is home, so $d = 0$, and $I = 1 + 0 = 1$; arrangement A cannot be solved.

In arrangement B the blank is in cell $1$, and the tiles $15, 14, \dots, 1$ fill cells $2$ to $16$.
The sequence $16, 15, \dots, 1$ has
$$\binom{16}{2} = \frac{16 \cdot 15}{2} = 120$$
inversions, which is even.
The blank is $3$ rows and $3$ columns from cell $16$, so $d = 6$, and $I = 0 + 0 = 0$.
The invariant does not rule out arrangement B, and by the converse in the remarks it can be solved.

So a quick count tests a position before any search for a solution.
Watch out: the parity of the tiles alone changes at every move, so a test that forgets the blank decides nothing.
