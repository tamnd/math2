---
tag: F9CZVRHKZY
kind: concept
name: Coloring
sources:
  - wikipedia: en:325802@r1373839425
    locator: Glossary of graph theory, section C
    note: adopted
    mention: wikipedia://en/325802#RXZG
    sections: [Summary]
inventory: [DHB12CAJ5Y]
---

## Summary

A [[graph coloring|0NCPXH194Y]] is a labeling of the vertices of a graph by elements from a given set of colors, or equivalently a partition of the vertices into subsets, called "color classes", each of which is associated with one of the colors.

Some authors use "coloring", without qualification, to mean a proper coloring, one that assigns different colors to the endpoints of each edge. In graph coloring, the goal is to find a proper coloring that uses as few colors as possible; for instance, [[bipartite graphs|07DVHJ8N0A]] are the graphs that have colorings with only two colors, and the [[four color theorem|0M406JC8J1]] states that every [[planar graph|029JQEK15B]] can be colored with at most four colors. A graph is said to be $k$-colored if it has been (properly) colored with $k$ colors, and $k$-colorable or $k$-chromatic if this is possible.

Many variations of coloring have been studied, including [[edge coloring|0B5WCC02AN]] (coloring edges so that no two edges with the same endpoint share a color), list coloring (proper coloring with each vertex restricted to a subset of the available colors), acyclic coloring (every 2-colored subgraph is acyclic), co-coloring (every color class induces an independent set or a clique), complete coloring (every two color classes share an edge), and total coloring (both edges and vertices are colored).

The coloring number of a graph is one plus the degeneracy. It is so called because applying a greedy coloring algorithm to a degeneracy ordering of the graph uses at most this many colors.
