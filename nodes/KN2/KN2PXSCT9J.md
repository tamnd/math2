---
tag: KN2PXSCT9J
kind: conjecture
name: Sidorenko's conjecture
msc: [05C35]
uses: [00C0BR7D7H, 0ZVQKTRKVQ, 052JJ9YVNM]
about: [SC5QB5F4TE, 052JJ9YVNM]
sources:
  - url: https://en.wikipedia.org/wiki/Sidorenko's_conjecture
same_as:
  wikidata: Q85801084
  wikipedia: Sidorenko's conjecture
history:
  posed_by: "Alexander Sidorenko"
---

## Statement

Let $H$ and $G$ be finite simple [[graphs|00C0BR7D7H]], with $G$ having at least one vertex.
Let $\hom(H, G)$ be the number of [[graph homomorphisms|052JJ9YVNM]] from $H$ to $G$, and let
$$t(H, G) = \frac{\hom(H, G)}{|V(G)|^{|V(H)|}}$$
be the homomorphism density.
Let $K_2$ be the graph with one edge, so that $t(K_2, G) = 2 |E(G)| / |V(G)|^2$.
Let $H$ be a [[bipartite graph|0ZVQKTRKVQ]] with $e(H)$ edges.
Then for every graph $G$,
$$t(H, G) \ge t(K_2, G)^{e(H)}.$$

## Remarks

The conjecture is open.
It is known for trees, for even cycles, for complete bipartite graphs and for hypercube graphs.
It is also known for every bipartite graph that has a vertex adjacent to all vertices of the other part.

The right side is the density of $H$ in a random graph with the same edge density.
So the conjecture says that random graphs minimise the density of $H$ among graphs of a given edge density.
Bipartiteness is necessary.
If $H$ has an odd cycle and $G$ is the complete bipartite graph $K_{n,n}$, then $t(H, G) = 0$, while $t(K_2, G) = 1/2$.
For $H$ a path with two edges, the conjecture is the inequality $\frac{1}{n} \sum_v d(v)^2 \ge \left(\frac{1}{n}\sum_v d(v)\right)^2$ for the degrees $d(v)$ of $G$, which holds by the Cauchy–Schwarz inequality.

## Explanations

### L1 human

Fix a small pattern $H$ with no odd cycle, such as a square.
Among all graphs with a given proportion of edges, which one has the fewest copies of $H$?
Sidorenko's conjecture says that a random graph is always at least as good as anything else: no clever arrangement of the edges can beat it.
