---
tag: G4WSPQJ6W1
kind: statement
role: theorem
name: Art gallery theorem
msc: [52C45, 68U05]
uses: [Q6KKBP3RRP, 0VHJRXNAAS]
about: [Q6KKBP3RRP]
sources:
  - url: https://en.wikipedia.org/wiki/Art_gallery_problem
---

## Statement

Let $P \subset \R^2$ be a simple polygon with $n \ge 3$ vertices.
Say that a point $g \in P$ sees a point $x \in P$ when the segment from $g$ to $x$ lies in $P$.

1. There is a set of at most $\floor{n/3}$ vertices of $P$ such that every point of $P$ is seen by at least one of them.
2. For every $n \ge 3$ there is a simple polygon $P$ with $n$ vertices that no set of fewer than $\floor{n/3}$ points of $P$ sees entirely.

## Remarks

The theorem is due to Václav Chvátal; the short proof below is due to Steve Fisk.
Take a [[triangulation|Q6KKBP3RRP]] of $P$, and consider the graph whose edges are the sides of $P$ and the diagonals used.
This graph can be properly coloured with $3$ colours (its [[chromatic number|0VHJRXNAAS]] is $3$), by removing an ear triangle, colouring the rest, and giving the last vertex the missing colour.
Each triangle then has one vertex of each colour.
The smallest colour class has at most $\floor{n/3}$ vertices, and it contains a vertex of every triangle, which sees the whole triangle because triangles are convex.

For sharpness, a comb with $k$ narrow teeth has $n = 3k$ vertices, and no point sees into two different teeth, so $k = n/3$ guards are needed.

## Explanations

### L1 human

Picture an art gallery whose floor plan is a polygon, and guards who stand still but can turn around.
The theorem says that one guard for every three corners is always enough.
Some galleries, shaped like combs, really need that many.

### L2 human

The proof is a model use of polygon triangulation: cut, colour, and count.
The bound $\floor{n/3}$ is a worst case over all polygons; for a given polygon the minimum number of guards can be much smaller, and computing it is NP-hard.
Many variants exist, such as orthogonal polygons, where $\floor{n/4}$ guards suffice, and polygons with holes.
