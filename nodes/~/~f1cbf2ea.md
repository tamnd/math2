---
tag: ~f1cbf2ea
kind: statement
role: theorem
name: Lachlan-Woodrow theorem
aliases: [lachlan-woodrow-theorem, classification-of-countable-homogeneous-graphs]
msc: ["03C15", "05C63", "05C75"]
topics: [ZS8X8KS54R]
audience: research
about: [~7468669e, RMXR0FEF54, TZT25G2YB3]
uses: [~7468669e, RMXR0FEF54, TZT25G2YB3, 0MCYJ72VGA, 03WKB2H474, 2MWTBETCWQ, 00C0BR7D7H, ~8123841a, A22K1X8GKD]
sources:
  - url: https://en.wikipedia.org/wiki/Homogeneous_graph
    locator: Classification
  - url: https://en.wikipedia.org/wiki/Henson_graph
    locator: Symmetry
---

## Statement

Let $G$ be a countably infinite [[graph|00C0BR7D7H]].
Then $G$ is [[ultrahomogeneous|~7468669e]] if and only if $G$ or its [[complement|0MCYJ72VGA]] is isomorphic to one of the following:

1. the disjoint union $m \cdot K_n$ of $m$ copies of the [[complete graph|03WKB2H474]] $K_n$, where $1 \le m, n \le \aleph_0$ and at least one of $m, n$ is infinite;
2. the [[Henson graph|TZT25G2YB3]] $G_n$ for some $n \ge 3$;
3. the [[Rado graph|RMXR0FEF54]] $R$.

## Remarks

### Why each hypothesis is needed

- Countably infinite: for finite graphs the list is different. Gardiner's list of finite homogeneous graphs adds $C_5$ and the rook's graph $K_3 \times K_3$, and $m \cdot K_n$ is allowed with $m, n$ finite.
- Graph, meaning one symmetric irreflexive relation: for directed graphs and tournaments the lists are longer, and Henson found $2^{\aleph_0}$ countable homogeneous directed graphs.

### Consequences

- There are countably many countable homogeneous graphs, up to isomorphism.
- Every countable homogeneous graph is [[$\aleph_0$-categorical|A22K1X8GKD]], since its signature is finite and relational.
- The graphs $m \cdot K_n$ are the [[cluster graphs|2MWTBETCWQ]] with equal finite or infinite parts; their complements are complete multipartite graphs.

### Converse

The "if" direction is the easier half: each listed graph is homogeneous, and complements of homogeneous graphs are homogeneous.

### Generalizations

Cherlin classified the countable homogeneous directed graphs.
Lachlan classified the countable homogeneous tournaments, and Schmerl the countable homogeneous partial orders; see [[homogeneous structures beyond graphs|~8f184581]].
The classification of homogeneous $3$-uniform hypergraphs is open.

## History

Gardiner classified the finite homogeneous graphs in 1976.
Lachlan and Woodrow proved the countable case in 1980.

## Explanations

### L1 human

Very few countable graphs are as symmetric as possible.
They are: unions of equal cliques, the generic graph, the generic graphs with a forbidden clique, and the complements of these.
Nothing else works.

### L2 human

We place some graphs on the list.

1. $\aleph_0 \cdot K_1$ is the infinite edgeless graph, and its complement is the countable complete graph.
2. $2 \cdot K_{\aleph_0}$ is two disjoint infinite cliques, and its complement is the complete bipartite graph $K_{\aleph_0, \aleph_0}$.
3. $G_3$ is the generic triangle-free graph.

The typical use is to recognize a homogeneous graph by one or two invariants: is it connected, which cliques does it omit.
A trap is to forget the complements; the complement of $G_3$ is homogeneous and has no independent set of size $3$.

### L3 human

The proof splits into the imprimitive case, where $G$ or its complement is disconnected, and the primitive case.
The imprimitive case is short; see [[the proof|~35b603aa]].
In the primitive case, Lachlan and Woodrow show that the age of $G$ is all finite graphs, or the $K_n$-free graphs, or the complements of these.
Fraïssé's uniqueness theorem then identifies $G$.
