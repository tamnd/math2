---
tag: MGMET02ZZS
kind: example
name: Sorting by swaps of neighbors stops after at most n(n - 1)/2 swaps
aliases: [sorting-by-swaps-of-neighbours-stops-after-at-most-n-n-1-2-swaps]
msc: ["00A35", "68P10"]
topics: [GB14W4SYPK]
audience: school
instance_of: [TP3GC5J08D]
uses: [TP3GC5J08D, MGKDQAM7K3]
sources:
  - url: https://en.wikipedia.org/wiki/Bubble_sort
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Inversion_(discrete_mathematics)
    locator: lead section
---

## Example

Let $a_1, a_2, \dots, a_n$ be a list of real numbers.
A move chooses a position $i$ with $a_i > a_{i+1}$ and swaps the entries at the positions $i$ and $i + 1$.
The moves may be made in any order.
We show with a [[monovariant|TP3GC5J08D]] that every sequence of moves stops after at most $n(n - 1)/2$ moves, and that the final list is sorted.

1. An inversion of the list is a pair of positions $(j, k)$ with $j < k$ and $a_j > a_k$.
   Let $M$ be the number of inversions.
2. There are $\binom{n}{2} = n(n - 1)/2$ pairs of positions, so $M$ is a natural number with $0 \le M \le n(n - 1)/2$.
3. Consider a move at position $i$.
   A pair of positions that contains neither $i$ nor $i + 1$ keeps its two entries, so it is an inversion after the move exactly when it was one before.
4. Let $k$ be a position other than $i$ and $i + 1$.
   The pairs that join $k$ to $i$ and to $i + 1$ compare $a_k$ with $a_i$ and with $a_{i+1}$, from the same side, before and after the move.
   The move only exchanges the roles of these two pairs, so the number of inversions among them does not change.
5. The pair $(i, i + 1)$ was an inversion, since $a_i > a_{i+1}$.
   After the move it holds $a_{i+1}, a_i$ in this order, so it is no longer an inversion.
6. By steps 3 to 5, each move lowers $M$ by exactly $1$.
   So after $k$ moves, $M = M_0 - k$, where $M_0$ is the value at the start.
7. Since $M \ge 0$, we get $k \le M_0 \le n(n - 1)/2$, so every sequence of moves stops.
8. The process stops only when no position $i$ has $a_i > a_{i+1}$.
   Then $a_1 \le a_2 \le \dots \le a_n$, so the final list is sorted.

Check: the list $3, 1, 4, 2$ has the inversions $(3, 1)$, $(3, 2)$ and $(4, 2)$, so $M_0 = 3$.
The moves give $1, 3, 4, 2$, then $1, 3, 2, 4$, then $1, 2, 3, 4$, with $M = 2$, $1$ and $0$.

## Remarks

Here the monovariant falls by exactly $1$, so it counts the moves and does not only bound them.
Every sequence of moves from the same list has exactly $M_0$ moves, whatever order of moves we choose.
The reversed list $n, n - 1, \dots, 1$ has every pair out of order, so $M_0 = n(n - 1)/2$, and the bound of step 7 is attained.
For $n = 4$, the list $4, 3, 2, 1$ needs exactly $6$ swaps.

Bubble sort and insertion sort are [[sorting algorithms|MGKDQAM7K3]] that make only such swaps, so each of them makes exactly $M_0$ swaps on a list with $M_0$ inversions.
If a move could swap two entries that are far apart, one swap could remove several inversions at once.
The bound of step 7 would still hold, but $M$ would no longer count the moves.

## Explanations

### L1 human

Take a row of cards with numbers, and allow a swap of two neighboring cards when the left one is bigger.
Count the pairs of cards, near or far, that are in the wrong order.
Each swap fixes exactly one such pair and does not spoil any other pair.
So the count goes down by $1$ at each swap, and it cannot go below $0$.
For the row $3, 1, 4, 2$ the count is $3$, so exactly $3$ swaps sort it.

### L2 human

We sort the list $5, 1, 4, 2, 3$ and track the monovariant.
The inversions are $(5, 1)$, $(5, 4)$, $(5, 2)$, $(5, 3)$, $(4, 2)$ and $(4, 3)$, so $M_0 = 6$, and the run must take exactly $6$ swaps.

1. Swap $5$ and $1$: the list is $1, 5, 4, 2, 3$, and $M = 5$.
2. Swap $5$ and $4$: the list is $1, 4, 5, 2, 3$, and $M = 4$.
3. Swap $5$ and $2$: the list is $1, 4, 2, 5, 3$, and $M = 3$.
4. Swap $5$ and $3$: the list is $1, 4, 2, 3, 5$, and $M = 2$.
5. Swap $4$ and $2$: the list is $1, 2, 4, 3, 5$, and $M = 1$.
6. Swap $4$ and $3$: the list is $1, 2, 3, 4, 5$, and $M = 0$.

No move is possible, and the list is sorted.
The same pattern proves that a local repair process ends: each repair fixes one defect and creates none.
Watch out: the count of neighboring pairs out of order is not a monovariant, because swapping $4$ and $1$ in $2, 4, 1, 3$ gives $2, 1, 4, 3$, and that count rises from $1$ to $2$.
