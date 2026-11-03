---
tag: 2KWQWH06AN
kind: definition
name: Christofides algorithm
msc: [90C27, 68W25, 05C85]
defines: 9WJV8JT13M
uses: [XJRHJX2241, 03HF5PMY5T, 0JW7KT6PQW, 0NHK9MFFW9, 05NWGBHKSZ, 9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Christofides_algorithm
---

## Definition

Let $V$ be a finite set of at least $3$ cities, and let $w(u, v) = w(v, u) \ge 0$ be the distance between distinct $u, v \in V$.
Assume the [[triangle inequality|03HF5PMY5T]] $w(u, x) \le w(u, v) + w(v, x)$ for all distinct $u, v, x \in V$.
Let $K$ be the complete graph on $V$ with edge weights $w$.
The *Christofides algorithm* is the following [[algorithm|9DMSG5HAQX]] for the [[travelling salesman problem|XJRHJX2241]] on $(V, w)$.

1. Compute a [[minimum spanning tree|0JW7KT6PQW]] $T$ of $K$.
2. Let $O$ be the set of vertices of odd degree in $T$.
3. Compute a [[perfect matching|0NHK9MFFW9]] $M$ of least total weight in the complete graph on $O$.
4. Form the multigraph $H$ whose edges are those of $T$ and those of $M$, counted with multiplicity.
5. Find an [[Eulerian circuit|05NWGBHKSZ]] of $H$, a closed trail that uses each edge of $H$ once.
6. List the vertices in the order of the circuit, keep only the first visit of each vertex, and return the resulting Hamiltonian cycle.

## Remarks

Step 3 makes sense because $\abs{O}$ is even, since the degrees of $T$ sum to an even number.
In $H$ every vertex has even degree, and $H$ is connected, so an Eulerian circuit exists.
Let $\mathrm{OPT}$ be the length of a shortest tour.
Deleting an edge from an optimal tour gives a spanning tree, so $w(T) \le \mathrm{OPT}$.
Shortcutting an optimal tour to the vertices of $O$ gives a cycle on $O$ of length at most $\mathrm{OPT}$, which splits into two perfect matchings, so $w(M) \le \mathrm{OPT}/2$.
By the triangle inequality, step 6 does not increase the length, so the tour has length at most $\frac32 \mathrm{OPT}$.

Example: four cities at the corners of a unit square, with Euclidean distances, satisfy the hypothesis.
A minimum spanning tree is the path along three sides, of weight $3$, with odd vertices at its two ends.
These ends are adjacent corners, so $M$ is the fourth side, $H$ is the square itself, and the output is the optimal tour of length $4$.

Non-example: if the triangle inequality fails, the algorithm can still be run, but the bound $\frac32 \mathrm{OPT}$ is lost, because shortcuts may make the tour longer.

The bound $\frac32$ is tight for this algorithm: there are metric instances where the ratio of its output to $\mathrm{OPT}$ tends to $\frac32$.
