---
tag: XZF9BFJFXB
kind: statement
role: theorem
name: Erdős–Stone theorem
msc: [05C35]
uses: [00C0BR7D7H, 0WBFFC8XZ9, 0VHJRXNAAS, DRGS5TT784]
about: [SC5QB5F4TE]
sources:
  - url: https://en.wikipedia.org/wiki/Erdős–Stone_theorem
same_as:
  wikidata: Q5385326
  wikipedia: Erdős–Stone theorem
---

## Statement

For integers $r \ge 1$ and $t \ge 1$, let $K_{r+1}(t)$ be the complete $(r+1)$-partite [[graph|00C0BR7D7H]] with $r + 1$ parts of $t$ vertices each.
Let $r \ge 1$ and $t \ge 1$ be integers and let $\varepsilon > 0$ be a real number.
Then there is an integer $n_0$ such that every graph with $n \ge n_0$ vertices and at least $\left(1 - \frac{1}{r} + \varepsilon\right) \frac{n^2}{2}$ edges contains a [[subgraph|0WBFFC8XZ9]] isomorphic to $K_{r+1}(t)$.

## Remarks

The main consequence is a formula for the [[extremal number|DRGS5TT784]].
Let $H$ be a graph with [[chromatic number|0VHJRXNAAS]] $\chi(H) = r + 1 \ge 2$.
Then $H$ is a subgraph of $K_{r+1}(t)$ for $t = |V(H)|$, and the [[Turán graph|0VTCABADBE]] $T(n, r)$ is $H$-free, so
$$\mathrm{ex}(n, H) = \left(1 - \frac{1}{r}\right) \frac{n^2}{2} + o(n^2) \quad (n \to \infty).$$
For example, the Petersen graph has chromatic number $3$, so a graph on $n$ vertices with no Petersen subgraph has at most $n^2/4 + o(n^2)$ edges.
For bipartite $H$ ($r = 1$) the formula only says $\mathrm{ex}(n, H) = o(n^2)$; the true order is the subject of the [[Zarankiewicz problem|KT9WJFRQ3F]].
A modern proof applies the [[Szemerédi regularity lemma|ETMAPNQY7T]] to find a dense $K_{r+1}$ in the reduced graph, and then a counting lemma to blow it up to $K_{r+1}(t)$.

## Explanations

### L1 human

[[Turán's theorem|0JG1KZSPFZ]] says how many edges force a complete graph $K_{r+1}$.
The Erdős–Stone theorem says that only a tiny bit more forces a much larger graph: a "blown-up" $K_{r+1}$ with many vertices in each part.
As a result, the largest number of edges avoiding any fixed graph $H$ is governed, up to a small error, by its chromatic number alone.

### L2 human

The theorem is often called the fundamental theorem of [[extremal graph theory|SC5QB5F4TE]].
It gives $\mathrm{ex}(n, H) / \binom{n}{2} \to 1 - \frac{1}{\chi(H) - 1}$ for every graph $H$ with at least one edge.
It is sharp for non-bipartite $H$ and degenerate for bipartite $H$, where the extremal number is $o(n^2)$.
Stability results refine it: an $H$-free graph with nearly $\mathrm{ex}(n, H)$ edges is close in structure to the Turán graph.
