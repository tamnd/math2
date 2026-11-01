---
tag: E6GYGZDBS7
kind: statement
role: theorem
name: Menger's theorem
msc: [05C40, 05C38]
uses: [0JD5C82QMB, 0JDE56HWQ8, 7FZB7YYBXA]
about: [0JDE56HWQ8, 7FZB7YYBXA]
sources:
  - url: https://en.wikipedia.org/wiki/Menger's_theorem
same_as:
  wikidata: Q928813
  wikipedia: Menger's theorem
---

## Statement

Let $G$ be a finite [[graph|0JD5C82QMB]], and let $u$ and $v$ be distinct vertices of $G$.
Two $u$–$v$ [[paths|0JDE56HWQ8]] are internally disjoint if they have no vertex in common other than $u$ and $v$.
A set $S$ of vertices or edges separates $u$ from $v$ if every $u$–$v$ path meets $S$.

1. Suppose that $u$ and $v$ are not adjacent. Consider the sets of vertices, other than $u$ and $v$, that separate $u$ from $v$. The least size of such a set equals the greatest number of pairwise internally disjoint $u$–$v$ paths.
2. The least size of a set of edges that separates $u$ from $v$ equals the greatest number of pairwise edge-disjoint $u$–$v$ paths.

## Remarks

In both parts, the inequality "at least" is easy: each separating set must contain a vertex or edge from each of the disjoint paths.
The other inequality can be proved by induction on the number of edges.
It also follows from the [[max-flow min-cut theorem|4HMR4KQ01T]], with capacity $1$ on each edge or each vertex and integral flows.
In part 1 the hypothesis that $u$ and $v$ are not adjacent is needed: if $uv$ is an edge, no set of other vertices separates $u$ from $v$.
For example, in the cycle $C_6$ two opposite vertices are joined by two internally disjoint paths, and removing one inner vertex from each of these paths separates them.
A global form, due to Whitney, follows.
A graph with more than $k$ vertices is [[$k$-vertex-connected|7FZB7YYBXA]] if and only if every two distinct vertices are joined by $k$ internally disjoint paths.

## Explanations

### L1 human

Think of a road map and two towns.
Count the fewest roads you must close to cut one town off from the other.
Count the most routes between the two towns that share no road.
Menger's theorem says that these two numbers are always equal.

### L2 human

Menger's theorem is the basic min-max theorem of graph connectivity.
It turns the definition of $k$-connectivity, which is about removing vertices, into a statement about disjoint paths, which is often easier to use.
It is a special case of max-flow min-cut, and it is equivalent in strength to [[Kőnig's theorem|0JP0ZF57PN]] and [[Hall's marriage theorem|08WCB90WND]] on bipartite matchings.
