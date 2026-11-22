---
tag: TP3GC5J08D
kind: concept
name: Monovariants
aliases: [monovariant-method]
msc: ["00A35", "05A99"]
topics: [G9JFJGY4TQ, GB14W4SYPK]
audience: school
uses: [8NQ190278Y, 01BX15HSRR, 0ASJVEFA9J, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Invariant_(mathematics)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Chip-firing_game
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Euclidean_algorithm
    locator: lead section
---

## Summary

A monovariant is a quantity that moves in one direction at every step of a process.
If it is a natural number that falls at each step, the process must stop, and the state where it stops often answers the problem.

Here is a problem that the method solves.
Take a list of numbers, and as long as two neighbors are in the wrong order, swap them, in any order you like.
Does this always stop, and how soon?
Count the inversions: the pairs of entries, near or far, that are in the wrong order.
A swap of two neighbors fixes their own pair and leaves every other pair as it was, so the count falls by exactly $1$.
A list of $n$ entries has at most $n(n - 1)/2$ inversions, so every run stops after at most $n(n - 1)/2$ swaps, and it stops only when the list is sorted; the [[full example|MGMET02ZZS]] gives the details.

In general, a monovariant of a process is a function $M$ on the states, with values in an ordered set, such that
$$M(t) < M(s) \quad \text{whenever a move changes } s \text{ into } t.$$
If the values lie in the natural numbers, or in any [[well-ordered|01CGSJ0GNQ]] set, then every sequence of moves is finite.
The same holds when each move raises an integer-valued $M$ and $M$ is bounded above.

## Motivation

An [[invariant|8NQ190278Y]] never changes, so it shows that a target is unreachable.
Many questions ask something else: does a process always stop, or does it always reach a state of a given kind?
A process that runs for a long time does not show that it never stops, and a computer run of a few cases proves nothing about all cases.
We need a quantity that moves one way at each step and cannot move that way for ever.
The natural numbers give such a quantity, because a strictly decreasing sequence of natural numbers is finite by the [[well-ordering principle|01BX15HSRR]].

The idea is everywhere in computing and analysis.
A proof that a loop or a recursive program ends names a ranking function that falls at each pass.
The [[Euclidean algorithm|0TRNT4X7J0]] ends because the remainders fall.
A local search ends at a local optimum because the cost falls at each improvement.
The [[extremal principle|MD3MRG90W4]] is the static form of the same idea: instead of running the process, you start at a state where $M$ is smallest.

## Notation

There is no standard symbol.
The words "monovariant", "semi-invariant" and "potential function" are used for the same idea.
In the theory of algorithms the quantity is a "variant" or a "ranking function", and in dynamical systems it is a [[Lyapunov function|01REYCJ371]].

## Remarks

### Why the method works

Suppose that $M$ has values in the natural numbers and each move lowers $M$ by at least $1$.
After $k$ moves from a state $s$ the value is at most $M(s) - k$, and it is not negative, so
$$k \le M(s).$$
For a general well-ordered set of values, an infinite sequence of moves would give an infinite strictly decreasing sequence of values, and the set of those values would have no least element.
When the set of states is finite, any strict monovariant works, because no state can repeat, so the process stops after fewer moves than there are states.
At the end no move is possible, and that is the extra fact you read off about the final state.

### More monovariants at work

In [[chip-firing on a path with two sinks|NPRJDRA177]], a site with two chips may send one chip to each neighbor.
The weight $x(m + 1 - x)$ on site $x$, summed over all chips, falls by exactly $2$ at each firing, so the game stops.

The [[Euclidean algorithm|0TRNT4X7J0]] replaces a pair $(a, b)$ with $b > 0$ by $(b, r)$, where $r$ is the remainder of $a$ on division by $b$.
The second entry falls, since $0 \le r < b$, so the algorithm stops.

A table of real numbers allows a move that changes the sign of every entry of a row or a column whose sum is negative.
If the line has sum $s < 0$, its sum becomes $-s$, so the total of the table rises by $-2s > 0$.
Only signs change, so there are finitely many reachable tables, and the process stops with every row sum and every column sum at least $0$; the L2 explanation runs it on a table.

[[Proof by infinite descent|0EFYCFHYFG]] is a monovariant argument on solutions: each solution gives a smaller one in the natural numbers, which cannot go on for ever.

### How to find a monovariant

The search follows a short routine.

1. Describe the states and the moves exactly.
2. Look for a quantity that each move changes in one direction: a sum, a count of bad pairs, a sum of squares, a weighted count, a distance.
3. Prove that the change is strict, for each kind of move.
4. Prove that the change cannot go on for ever: the values are natural numbers, or the states are finite.
5. Conclude that the process stops, and read off the property of the final state from "no move is possible".

The weight in chip-firing shows how to design the quantity: give the value $0$ where the process loses material, and large values far from it.

### What a monovariant cannot do

A monovariant proves that every order of moves stops.
It does not say that all orders end in the same state; chip-firing has that property, but it needs a separate exchange argument.

A quantity that falls is not enough when its values can fall for ever.
The map $x \mapsto x/2$ on the positive real numbers lowers $x$ at each step and never stops, as [[the halving example|J1HQ8MMQ8C]] shows.
When a process can loop, no strict monovariant exists at all.
Chip-firing on a cycle of $3$ vertices with $2, 1, 1$ chips gives $(0, 2, 2)$, then $(1, 0, 3)$, then $(2, 1, 1)$ again, so it runs for ever.
In the 15 puzzle, the number of tiles in their home cells goes up at some moves and down at others, so it is neither an invariant nor a monovariant.

### Watch out

The first common error is to show that the quantity falls and to forget that it must be bounded below by a value it cannot pass.
Positive real numbers can fall for ever, so check that the values are integers, or that the states are finite.

The second error is to check only some moves.
In the sorting problem, the number of neighboring pairs out of order looks like a natural choice, but it is not a monovariant: swapping $4$ and $1$ in $2, 4, 1, 3$ gives $2, 1, 4, 3$, and the count rises from $1$ to $2$.
The full count of inversions is the right quantity.

### History

The Euclidean algorithm, in Book VII of Euclid's "Elements", stops because the remainders fall.
Pierre de Fermat used infinite descent, a monovariant argument on solutions of equations, in the seventeenth century.
Per Bak, Chao Tang and Kurt Wiesenfeld introduced the sandpile model in 1987, and Anders Björner, László Lovász and Peter Shor studied chip-firing games on graphs in 1991.

### Try it

Several positive integers stand on a board.
A move picks two numbers $a > b$ and replaces them by $a - b$ and $b$.
Why must the process stop?
Each move lowers the sum of the numbers by $b \ge 1$, and the sum stays a positive integer, so the number of moves is less than the starting sum.

People are split between two rooms, and a person who has more enemies in their own room than in the other room may move to the other room.
Why do the moves end?
A move by a person with $e$ enemies in their room and $e' < e$ in the other room changes the number of enemy pairs in the same room by $e' - e \le -1$, and that number is a natural number.

## Explanations

### L1 human

Some processes look as if they could go on for ever.
To show that one must stop, find a whole number that goes down at every step and never goes below $0$.
A whole number that drops by at least $1$ each time cannot keep dropping, so the steps must end.
For example, take the list $3, 1, 2$ and swap two neighbors whenever they are in the wrong order.
The pairs in the wrong order are $(3, 1)$ and $(3, 2)$, so the count is $2$, and each swap lowers it by $1$.
So after at most $2$ swaps the list is sorted.

### L2 human

We show that the sign-change process on a table stops, and we run it on one table.
A move picks a row or a column with a negative sum and changes the sign of each of its entries.
Let $S$ be the sum of all entries.
If the move changes a line with sum $s < 0$, that line now has sum $-s$, so
$$S_{\text{new}} = S - s + (-s) = S - 2s > S.$$
Each reachable table has the same absolute values as the start, so a table with $mn$ entries has at most $2^{mn}$ reachable versions.
Since $S$ rises strictly, no table repeats, and the process stops after fewer than $2^{mn}$ moves.

Now run it on the table with rows $(1, -2, 3)$ and $(-4, 1, -1)$.
The row sums are $2$ and $-4$, the column sums are $-3$, $-1$ and $2$, and $S = -2$.
Change the second row: the rows become $(1, -2, 3)$ and $(4, -1, 1)$, and $S = -2 + 8 = 6$.
The column sums are now $5$, $-3$ and $4$, so change the second column: the rows become $(1, 2, 3)$ and $(4, 1, 1)$, and $S = 6 + 6 = 12$.
The row sums are $6$ and $6$, the column sums are $5$, $3$ and $4$, and no move is possible.

So the process proves that every table can be made, by sign changes, into one with no negative line sum.
Watch out: $S$ is a real number, and a rising real number can rise for ever, so the count of $2^{mn}$ states is needed.

### L3 human

A monovariant is a map from the states to a well-founded order that strictly decreases along each move.
Then the move relation is a [[well-founded relation|0DQPNJNPYK]], and every sequence of moves is finite.
Values in the ordinals give stronger tools: the proof of [[Goodstein's theorem|XQMNJF241J]] uses a decreasing ordinal below $\varepsilon_0$, and the theorem cannot be proved in Peano arithmetic.
In the theory of programs, ranking functions play the same role, and term rewriting systems are proved to terminate by orders on terms.

In dynamical systems a [[Lyapunov function|01REYCJ371]] decreases along the trajectories and proves the stability of an equilibrium.
In optimization, the objective value is a monovariant of a local search, and the final state is a local optimum.
In algebraic combinatorics, the [[abelian sandpile model|N33S3095R5]] uses a monovariant to prove that stabilization ends, and an exchange argument proves that the final state does not depend on the order of the firings.
Many proofs combine the method with an [[invariant|8NQ190278Y]]: the invariant fixes what stays, and the monovariant shows that the process ends.
