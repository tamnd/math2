---
tag: T06PG3RWC0
kind: example
name: Permutohedron
msc: [52B12, 52B05, 05A05]
instance_of: [Z5SA6A67KF, 7E6FXTGH2Y]
uses: [300K6CB1KH, R7V3S9V891, DPDXN2FJC4, 05RWFKVTJ7]
sources:
  - url: https://en.wikipedia.org/wiki/Permutohedron
same_as:
  wikidata: Q1710083
  wikipedia: Permutohedron
---

## Example

Let $n \ge 1$.
The *permutohedron* $\Pi_n$ is the convex hull in $\R^n$ of the $n!$ points
$$(\sigma(1), \sigma(2), \dots, \sigma(n)),$$
where $\sigma$ runs over all [[permutations|05RWFKVTJ7]] of $\set{1, \dots, n}$.

All these points satisfy $x_1 + \cdots + x_n = n(n+1)/2$, so $\Pi_n$ lies in a hyperplane, and it has dimension $n - 1$.
Each of the $n!$ points is a [[vertex|R7V3S9V891]]: the vector $c = (\sigma(1), \dots, \sigma(n))$ is maximised over the points uniquely at that point, by the rearrangement inequality.
The [[facets|DPDXN2FJC4]] correspond to the nonempty proper subsets $S \subset \set{1, \dots, n}$, with facet inequality
$$\sum_{i \in S} x_i \ge \frac{\abs{S}(\abs{S}+1)}{2},$$
so there are $2^n - 2$ facets.
Two vertices are joined by an edge exactly when one is obtained from the other by swapping the values $k$ and $k+1$ for some $k$.
Hence every vertex lies in $n - 1$ edges and $\Pi_n$ is a [[simple polytope|7E6FXTGH2Y]].

$\Pi_n$ is a [[zonotope|Z5SA6A67KF]]: it is a translate of the Minkowski sum of the segments $[0, e_j - e_i]$ for $1 \le i < j \le n$.

## Remarks

For $n = 3$, $\Pi_3$ is a regular hexagon with vertices the six permutations of $(1,2,3)$.
For $n = 4$, $\Pi_4$ is the truncated octahedron, with $24$ vertices, $14$ facets ($6$ squares and $8$ hexagons) and $36$ edges.

## Explanations

### L1 human

Write the numbers $1$ to $n$ in every possible order and treat each order as a point in space.
The solid spanned by these points is the permutohedron.
Its corners are the orderings, and walking along an edge means swapping two neighbouring values.
For three numbers it is a hexagon, for four numbers a solid with $24$ corners built from squares and hexagons.
