---
tag: E3ECET66DQ
kind: definition
name: Hyperbolic group
msc: [20F67, 20F65]
defines: JWJ8YPR7EB
uses: [0VKD1TP7F3, 082DWWXMRJ, 0RP7VWQ0YN, 0GYQK9NDJF, 6FKYSH729T]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperbolic_group
---

## Definition

Let $(X, d)$ be a [[metric space|0VKD1TP7F3]] that is geodesic: any two points are joined by a geodesic segment.
A geodesic segment is an isometric image of a closed interval of $\R$.
A geodesic triangle in $X$ consists of three points and three geodesic segments joining them in pairs.
For $\delta \ge 0$, a geodesic triangle is *$\delta$-slim* if each of its sides lies in the closed $\delta$-neighbourhood of the union of the other two sides.
The space $X$ is *$\delta$-hyperbolic* if every geodesic triangle in $X$ is $\delta$-slim.

Let $G$ be a [[finitely generated group|082DWWXMRJ]] and let $S$ be a finite [[generating set|0RP7VWQ0YN]].
Give the [[Cayley graph|0GYQK9NDJF]] $\Gamma(G, S)$ the path metric in which each edge has length $1$.
The group $G$ is *hyperbolic* if $\Gamma(G, S)$ is $\delta$-hyperbolic for some $\delta \ge 0$.

## Remarks

The definition does not depend on $S$: Cayley graphs for different finite generating sets are [[quasi-isometric|6FKYSH729T]], and among geodesic spaces hyperbolicity is invariant under quasi-isometry, though $\delta$ may change.

Example: the [[free group|0KTW26C80J]] $F_2$ with a free basis $S$.
Its Cayley graph is a tree, in which every geodesic triangle is a tripod, so each side lies in the union of the other two and the graph is $0$-hyperbolic.

Example: every finite group is hyperbolic, with $\delta$ equal to the diameter of its Cayley graph.

Non-example: $\Z^2$ is not hyperbolic.
Its Cayley graph is quasi-isometric to the Euclidean plane.
In the plane, take the triangle with vertices $(0, 0)$, $(n, 0)$ and $(0, n)$.
The point $(n/2, n/2)$ of its hypotenuse is at distance $n/2$ from the other two sides, which is unbounded in $n$.

Equivalent definitions use the Gromov product, or ask that the group be finitely presented with a linear [[Dehn function|Q4HGMRA9JQ]].
Such groups are also called word-hyperbolic or Gromov hyperbolic groups.
