---
tag: YBNZWCG8AC
kind: statement
role: theorem
name: Balinski's theorem
msc: [52B05, 05C40]
uses: [300K6CB1KH, 7FZB7YYBXA, 00C0BR7D7H]
about: [300K6CB1KH, 7FZB7YYBXA]
sources:
  - url: https://en.wikipedia.org/wiki/Balinski%27s_theorem
same_as:
  wikidata: Q32182
  wikipedia: Balinski's theorem
---

## Statement

Let $d \ge 1$ and let $P$ be a [[convex polytope|300K6CB1KH]] of dimension $d$.
Let $G(P)$ be the [[graph|00C0BR7D7H]] whose vertices are the vertices of $P$ and whose edges are the edges of $P$.
Then $G(P)$ is [[d-vertex-connected|7FZB7YYBXA]]: it has more than $d$ vertices, and it stays connected after the removal of any $d - 1$ vertices.

## Remarks

The theorem was proved by Michel Balinski in 1961.
Proof idea: remove a set $S$ of $d - 1$ vertices, and pass a hyperplane through $S$ and one further vertex.
From every vertex that does not maximise a linear function on $P$ there is an edge along which the function increases, as in the simplex method.
Use this for the linear function defining the hyperplane and for its negative.
It connects every remaining vertex, avoiding $S$, to the top face or the bottom face of $P$.
These pieces are then joined through the extra vertex.

Example: the graph of the $3$-cube is $3$-connected; removing the $3$ neighbours of a vertex isolates it, so the bound $d$ is sharp.

## Explanations

### L1 human

Take a convex polytope in $d$ dimensions and look at its network of corners and edges.
Balinski's theorem says that this network is very robust: you must delete at least $d$ corners to cut it into pieces.
For a solid in space you need to remove at least three corners.

### L2 human

For $d = 3$ this is the easy half of Steinitz's theorem on graphs of $3$-polytopes.
The bound is sharp for every simple polytope, since a vertex has only $d$ neighbours.
It is one of the few general facts known about graphs of polytopes in high dimension, along with results and open questions about their diameter, such as the Hirsch conjecture.
