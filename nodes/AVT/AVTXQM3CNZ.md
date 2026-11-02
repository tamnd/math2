---
tag: AVTXQM3CNZ
kind: definition
name: Domino tiling
msc: [05B45, 05C70, 52C20]
defines: 83PJCPB9VA
uses: [GKJK293DXS, 0NHK9MFFW9]
sources:
  - url: https://en.wikipedia.org/wiki/Domino_tiling
---

## Definition

A *cell* is a unit square $[a, a+1] \times [b, b+1]$ with $a, b \in \Z$.
A *domino* is the union of two cells that share an edge, so it is a $1 \times 2$ or $2 \times 1$ rectangle with integer corners.
Let $R \subseteq \R^2$ be a region that is a union of finitely many cells.
A *domino tiling* of $R$ is a finite set $D$ of dominoes such that:

1. every domino of $D$ is contained in $R$;
2. the union of the dominoes of $D$ is $R$;
3. two distinct dominoes of $D$ have disjoint interiors.

## Remarks

Example: the $2 \times 3$ rectangle $[0, 3] \times [0, 2]$ has exactly three domino tilings.
They are: three vertical dominoes; one vertical domino on the left and two horizontal ones on the right; and the mirror image of the second.
More generally, the $2 \times n$ rectangle has $F_{n+1}$ domino tilings, where $F_1 = F_2 = 1$ and $F_{k+1} = F_k + F_{k-1}$ are the [[Fibonacci numbers|0GA9K57A39]].

Non-example: remove two opposite corner cells from the $8 \times 8$ board.
Colour the cells like a chessboard; each domino covers one black and one white cell, but the two removed cells have the same colour.
So the remaining $62$ cells have $32$ of one colour and $30$ of the other, and no set of dominoes satisfies clauses 2 and 3.

Equivalently, a domino tiling of $R$ is a [[perfect matching|0NHK9MFFW9]] of the graph whose vertices are the cells of $R$, two cells being adjacent when they share an edge.
