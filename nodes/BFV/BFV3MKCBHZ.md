---
tag: BFV3MKCBHZ
kind: definition
name: Schlegel diagram
msc: [52B05, 52B11, 52B10]
defines: S2JE8M3FMP
uses: [300K6CB1KH, DPDXN2FJC4, KY7SB854VH, 0YMB1676R1]
sources:
  - url: https://en.wikipedia.org/wiki/Schlegel_diagram
---

## Definition

Let $P \subset \R^d$ be a [[convex polytope|300K6CB1KH]] of dimension $d \ge 2$, and let $F$ be a [[facet|DPDXN2FJC4]] of $P$.
For each facet $G$, let $H_G$ be the hyperplane spanned by $G$.
Choose a point $p \in \R^d$ such that:

1. $p$ and $P$ lie on opposite sides of $H_F$, strictly;
2. for every facet $G \ne F$, $p$ lies strictly on the same side of $H_G$ as the interior of $P$.

For $x \in P$, let $\pi(x)$ be the point where the segment from $p$ to $x$ meets $H_F$.
The *Schlegel diagram* of $P$ based at $F$ is the collection of the sets $\pi(G')$.
Here $G'$ runs over the [[faces|KY7SB854VH]] of $P$ other than $P$ and $F$.

## Remarks

Each $\pi(G')$ is a convex polytope contained in $F$, of the same dimension as $G'$.
These polytopes cover $F$, two of them meet in a common face, and their inclusions are those of the faces of $P$.
So the diagram is a polytopal subdivision of $F$ that records the whole face lattice of $P$.
Points $p$ as in the definition exist; any point beyond $F$ close enough to an interior point of $F$ works.

Example: let $P = [0,1]^3$, $F$ the facet $x_3 = 1$, and $p = (\tfrac12, \tfrac12, 1 + \epsilon)$ with $\epsilon > 0$ small.
Then $p$ is above $x_3 = 1$, and on the inner side of the four side planes and of $x_3 = 0$.
The bottom square projects to a smaller square in the middle of $F$, and the four side squares project to trapezoids between the two squares.

Non-example: in the same example, $p = (5, \tfrac12, 2)$ satisfies condition 1 but fails condition 2 for the facet $x_1 = 1$, since $p$ has $x_1 > 1$.
Then the images are not even inside $F$: the segment from $p$ to the vertex $(1, 0, 0)$ meets the plane $x_3 = 1$ at $(3, \tfrac14, 1) \notin F$.
