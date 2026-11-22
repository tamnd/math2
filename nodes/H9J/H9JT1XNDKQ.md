---
tag: H9JT1XNDKQ
kind: concept
name: Parity arguments
aliases: [parity-argument]
msc: ["00A35", "05A99"]
topics: [G9JFJGY4TQ, GB14W4SYPK]
audience: school
uses: [0WAY5WX8NY, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Parity_(mathematics)
    locator: Additional applications
  - url: https://en.wikipedia.org/wiki/Handshaking_lemma
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Seven_Bridges_of_K%C3%B6nigsberg
    locator: Euler's analysis
  - url: https://en.wikipedia.org/wiki/15_puzzle
    locator: Solvability
---

## Summary

A parity argument proves that something is impossible by asking only whether a certain integer is even or odd.
It is the simplest [[invariant|8NQ190278Y]], and it is often the first tool to try when a problem asks "is it possible?".

Here is a problem that it solves.
Can nine people at a party each shake hands with exactly three of the others?
Add up the handshakes from each person's side: $9 \cdot 3 = 27$.
Every handshake has two people in it, so this sum counts each handshake twice and must be even.
Since $27$ is odd, the plan is impossible, and the [[full example|XWY34NHQ58]] states it for graphs.

In general, a parity argument has three parts: an integer quantity $Q$, a fact that fixes the parity of $Q$, and a target that needs the other parity.
The fact comes from a second way to compute $Q$, or from the rule that each allowed move keeps the parity of $Q$.
Since no integer is both even and odd, the target is impossible.
In the language of [[congruences|0WAY5WX8NY]], the argument computes $Q$ modulo $2$.

## Motivation

Many questions ask whether a configuration can exist or whether a target can be reached.
A search through all cases is often too long, and for an infinite family of cases it is not possible at all.
A parity argument replaces the search by one computation in the two-element set $\{\text{even}, \text{odd}\}$.
For example, a board with $25$ cells has no tiling by dominoes, because each domino covers $2$ cells and $25$ is odd.
No case analysis of the positions of the dominoes is needed.

Parity runs through all of mathematics.
The sign of a permutation is a parity, and determinants are built on it.
A parity bit in a computer word detects a single error in transmission.
[[Coloring proofs|90Q4PK1CST]] refine the idea by counting the cells of each color, and the [[15 puzzle|RTSBC9NAD7]] combines two parities into one invariant.

## Notation

We write $n \equiv 0 \pmod 2$ for "$n$ is even" and $n \equiv 1 \pmod 2$ for "$n$ is odd".
The rules of parity are the rules of addition and multiplication modulo $2$: even plus odd is odd, odd plus odd is even, and a product is odd only when both factors are odd.
Some books write $(-1)^n$, which is $1$ for even $n$ and $-1$ for odd $n$, and this is the form used for the [[sign of a permutation|02DKV69ZH0]].

## Remarks

### Why parity works so often

The map $n \mapsto n \bmod 2$ from $\mathbb{Z}$ to $\{0, 1\}$ turns sums into sums modulo $2$ and products into products modulo $2$.
So you can compute the parity of a big expression from the parities of its parts, without knowing the parts.
A sum of integers is odd exactly when it has an odd number of odd terms, and that one rule gives the [[number of odd-degree vertices is even|0QQQQCPZA8]].
Many proofs also need the fact that $0$ is even, as the [[parity of zero|HFFN6YCTAB]] explains, because the start or the target is often an empty count.

### Parity in graphs and walks

The [[handshaking lemma|0XAP8WHNES]] says that the degrees of a [[graph|00C0BR7D7H]] add up to $2|E|$, an even number.
So no graph has nine vertices that all have [[degree|0KS0KRDV4Y]] $3$, since the sum would be $27$.

The [[Seven Bridges of Königsberg|0YCW781Q9D]] have no walk that crosses each bridge exactly once.
A walk enters and leaves each vertex that it passes through, so it uses the edges there in pairs, and only the start and the end can have odd degree.
All four land areas have odd degree, so no such walk exists.

A knight move changes $r + c$ by $\pm 1 \pm 2$, an odd number, so a knight changes the color of its square at each move and can return to its start square only after an even number of moves.

### Parity of sums and moves

No choice of signs makes $\pm 1 \pm 2 \pm \cdots \pm 10$ equal to $0$.
With all signs plus the sum is $55$, which is odd, and changing the sign of $k$ moves the sum by $2k$, an even number; the [[full example|54X6W97NRV]] gives the details.

Seven cups stand upright, and a move turns over exactly two cups.
The number of cups upside down changes by $-2$, $0$ or $2$, so it stays even, and it can never be $7$.

A product of an odd number of transpositions is never the identity permutation, because its sign is $-1$.
That fact is the core of the proof that half of the positions of the 15 puzzle cannot be solved.

### What parity cannot see

An even count does not prove that an object exists.
The $4 \times 4$ board without two opposite corners has $14$ cells, and it still has no domino tiling, as [[the example of the small board|JW87PBD98X]] shows.
The obstruction there is a split of $6$ and $8$ between two colors, and only a coloring proof sees it.

Some problems depend on a residue modulo $3$ or $4$, and parity is too coarse for them.
The $10 \times 10$ board has $100$ cells, an even number and a multiple of $4$, and still has no tiling by $1 \times 4$ bars; a coloring with four colors is needed.
A quantity whose parity changes in an irregular way gives no argument either: if a move can add $1$ or $2$ to a counter, its parity can take both values.

### The steps

1. Choose an integer quantity $Q$ that the problem determines: a count of cells, a sum of degrees, a sum of numbers, a number of inversions.
2. Find the parity of $Q$ for every allowed configuration, or show that each allowed move keeps the parity of $Q$.
3. Compute the parity of $Q$ for the target.
4. If the two parities differ, the target is impossible.
   If they agree, the argument decides nothing, and you need another method.

### Watch out

The most common error is to read "the parities agree" as a proof that the target can be reached.
For $\pm 1 \pm 2 \pm 3 \pm 4$, the sum with all signs plus is $10$, and the target $12$ has the same parity.
Still no choice of signs gives $12$, because the largest possible value is $10$.
Parity gives a necessary condition, and a matching parity only means that you must look further.

A second error is to forget a kind of move.
If one allowed move changes the parity, the argument fails, so check each kind of move.
A third error is to mix the parity of a number with the parity of a [[permutation|05RWFKVTJ7]]: a permutation is odd when its sign is $-1$, which is a different count.

### History

Leonhard Euler used a parity argument in 1736 to show that the Königsberg bridge walk does not exist.
In the same paper he observed that the degrees of a graph add up to twice the number of edges, the fact now called the handshaking lemma.
William Woolsey Johnson and William Edward Story used a parity argument in 1879 to show that half of the starting positions of the 15 puzzle cannot be solved.

### Try it

Remove two cells from a $7 \times 7$ board; can the rest have a domino tiling?
The rest has $49 - 2 = 47$ cells, which is odd, so no tiling exists, whichever two cells you remove.

Can $11$ lines in the plane be drawn so that each meets exactly $3$ of the others?
No: the meeting graph would have $11$ vertices of degree $3$, and $11 \cdot 3 = 33$ is odd.

## Explanations

### L1 human

Every whole number is even or odd, and never both.
A parity argument uses this fact to show that something cannot happen.
Take a board with $5$ rows and $5$ columns, so it has $25$ squares.
Each domino covers exactly $2$ squares, so any number of dominoes covers an even number of squares.
Since $25$ is odd, no set of dominoes covers this board exactly.
We did not try any placements: one check of even and odd was enough.

### L2 human

We show that a knight on a chessboard cannot return to its start square after an odd number of moves.
Give the square in row $r$ and column $c$ the number $r + c$, with rows and columns numbered $1$ to $8$.
A knight move changes one coordinate by $1$ and the other by $2$, so it changes $r + c$ by
$$\pm 1 \pm 2 \in \{-3, -1, 1, 3\}.$$
Each of these changes is odd, so each move changes the parity of $r + c$.
After $k$ moves the parity has changed $k$ times, and for odd $k$ the final parity differs from the start parity.
So after an odd number of moves the knight stands on a different square.

The proof rules out a target with one short invariant, before any search starts.
Watch out for the converse: the argument does not show that the knight can return after every even number of moves.
For two moves it can, by a move and its reverse, but that is a construction, not a parity fact.

### L3 human

A parity argument is a homomorphism to the group $\mathbb{Z}/2\mathbb{Z}$.
In general, the quantity $Q$ takes values in an abelian group, and the allowed moves add elements of a subgroup $H$.
The target is impossible when it lies outside the coset of the start modulo $H$.
Parity is the case where the group is $\mathbb{Z}$ and the obstruction is seen in the quotient $\mathbb{Z}/2\mathbb{Z}$.
Larger quotients, such as $\mathbb{Z}/n\mathbb{Z}$, and the color counts of [[coloring proofs|90Q4PK1CST]] detect finer obstructions.

The same pattern appears in many fields.
The sign homomorphism from the symmetric group to $\{1, -1\}$ gives the alternating group and the theory of determinants.
In topology, the degree of a map modulo $2$ and the Euler characteristic modulo $2$ are parity invariants.
General [[invariants|8NQ190278Y]] keep the idea and replace the two-element group by richer structures.
