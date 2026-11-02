---
tag: 9GQQ7TK36T
kind: statement
role: theorem
name: Keller's conjecture
msc: [52C22, 05B45]
uses: [GKJK293DXS, 087VJM5Q77]
about: [GKJK293DXS]
sources:
  - url: https://en.wikipedia.org/wiki/Keller%27s_conjecture
same_as:
  wikidata: Q4802474
  wikipedia: Keller's conjecture
---

## Statement

Let $n \ge 1$.
Call a [[tiling|GKJK293DXS]] of $\R^n$ a *cube tiling* if each tile is a [[translate|087VJM5Q77]] $[0, 1]^n + v$ of the unit cube, with $v \in \R^n$.
Then the following are equivalent.

1. Every cube tiling of $\R^n$ contains two cubes that meet in a common $(n-1)$-dimensional face.
2. $n \le 7$.

## Remarks

Ott-Heinrich Keller conjectured in 1930 that clause 1 holds in every dimension.
Oskar Perron proved it for $n \le 6$ in 1940.
Jeffrey Lagarias and Peter Shor showed in 1992 that it fails for $n \ge 10$, and John Mackey showed in 2002 that it fails for $n = 8$, hence also for $n = 9$.
The case $n = 7$ was settled positively in 2020 by Joshua Brakensiek, Marijn Heule, John Mackey and David Narváez with a large computer search based on a SAT solver.
The counterexamples come from cliques in the *Keller graphs*, finite graphs whose large cliques correspond to cube tilings without face-to-face pairs.
For $n = 2$ the statement is easy to see.
A tiling of the plane by unit squares splits into rows or into columns, and two neighbouring squares in a row or column share an edge.

## Explanations

### L1 human

Fill space with equal cubes, all facing the same way, with no gaps and no overlaps.
Keller guessed that some two cubes must always touch along a whole face.
This is true in dimensions up to $7$ but false from dimension $8$ on.

### L2 human

In the plane the conjecture is easy, and in three dimensions it can still be checked by hand.
Hajós turned the problem into a question about factorizations of finite abelian groups, and later the problem was reduced to finite graphs.
These reductions allowed computer searches, and the final case, dimension $7$, needed a computer-assisted proof.
The lattice version, where the translation vectors form a lattice, is Minkowski's conjecture, proved by Hajós in 1941 in all dimensions.
