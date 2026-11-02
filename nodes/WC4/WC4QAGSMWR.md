---
tag: WC4QAGSMWR
kind: definition
name: Penny graph
msc: [05C62, 52C15, 52C10]
defines: 6DG5BBQPRA
uses: [00C0BR7D7H]
sources:
  - url: https://en.wikipedia.org/wiki/Penny_graph
---

## Definition

A finite [[graph|00C0BR7D7H]] $G = (V, E)$ is a *penny graph* if there is a map $p \colon V \to \R^2$ such that:

1. $\norm{p(u) - p(v)} \ge 1$ for all distinct $u, v \in V$;
2. $uv \in E$ if and only if $\norm{p(u) - p(v)} = 1$.

Equivalently, $G$ is the contact graph of a family of closed discs of diameter $1$ with pairwise disjoint interiors, centred at the points $p(v)$.

## Remarks

Example: the triangle $K_3$ is a penny graph.
Put $p$ at the vertices of an equilateral triangle of side $1$; all distances are equal to $1$, so both clauses hold.

Non-example: $K_4$ is not a penny graph.
Three of its vertices would have to sit at the corners of an equilateral triangle of side $1$.
No point of the plane is at distance $1$ from all three corners, so clause 2 fails for the fourth vertex.

Every penny graph is planar and has maximum degree at most $6$.
Take a vertex whose point is a corner of the convex hull of $p(V)$.
Its neighbours are at angles at least $60^\circ$ apart inside an angle less than $180^\circ$, so it has degree at most $3$.
Hence every penny graph can be properly coloured with $4$ colours, by colouring greedily after removing such vertices one at a time.
