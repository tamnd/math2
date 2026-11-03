---
tag: SCDYDGR153
kind: object
name: Fullerene graph
msc: [05C92, 05C10, "92E10"]
instance_of: [0Q70YFB6ZM]
uses: [0NC9R64TXP, 0Q70YFB6ZM, 7FZB7YYBXA, 0W1C598HMS, 2PYAZX5VD4, AE724Y8CQX]
sources:
  - url: https://en.wikipedia.org/wiki/Fullerene
---

## Description

A *fullerene graph* is a [[planar|0NC9R64TXP]], $3$-[[regular|0Q70YFB6ZM]], [[3-vertex-connected|7FZB7YYBXA]] graph with the following property.
Every face of its plane embedding is bounded by a cycle of length $5$ or $6$.
It is the molecular graph of a fullerene, a closed cage molecule of carbon atoms in which each atom is bonded to three others.
By [[Steinitz's theorem|2PYAZX5VD4]], fullerene graphs are exactly the graphs of convex polyhedra with three edges at each vertex and only pentagonal and hexagonal faces.

## Remarks

Every fullerene graph has exactly $12$ pentagonal faces.
Indeed, let it have $V$ vertices, $E$ edges, $p$ pentagons and $h$ hexagons.
Counting edge ends gives $2E = 3V$, and counting edge sides gives $2E = 5p + 6h$.
[[Euler's formula|0W1C598HMS]] $V - E + (p + h) = 2$ then gives $-E/3 + p + h = 2$, so $-(5p + 6h)/6 + p + h = 2$, that is $p = 12$.
The number of vertices is even, since $3V = 2E$, and it equals $20 + 2h$.
Fullerene graphs exist with $n$ vertices exactly for $n = 20$ and for every even $n \ge 24$.
Example: the graph of the dodecahedron, with $20$ vertices and $12$ pentagons and no hexagons, is the smallest fullerene graph.
Example: the graph of the truncated icosahedron, with $60$ vertices, $90$ edges, $12$ pentagons and $20$ hexagons, is the graph of buckminsterfullerene $\mathrm{C_{60}}$.

## Explanations

### L1 human

A fullerene is a ball of carbon atoms, like a football: each atom has three bonds, and the bonds form pentagons and hexagons.
The graph of the bonds, drawn flat, is a fullerene graph.
A neat count with Euler's formula shows that every such ball has exactly twelve pentagons, however many hexagons it has.
The famous $\mathrm{C_{60}}$ molecule has the pattern of a classic football: $12$ pentagons and $20$ hexagons.
