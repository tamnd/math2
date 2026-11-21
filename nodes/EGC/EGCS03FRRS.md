---
tag: EGCS03FRRS
kind: example
name: Triangle-free graphs form a universal class
aliases: [triangle-free-graphs-universal-class]
msc: ["03C52", "05C75"]
topics: [JYJHB4YBAH]
audience: grad
instance_of: [ZSTEZ3PRT9]
uses: [ZSTEZ3PRT9, 00C0BR7D7H, 676H7EGTKJ, C9494XYEMN]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_class
    locator: Definition
  - book: isbn:9780521587136
---

## Example

Let $L = \set{E}$ with $E$ binary, and let $\mathcal{K}$ be the class of triangle-free [[graphs|00C0BR7D7H]]: graphs with no three pairwise adjacent vertices.
We show that $\mathcal{K}$ is a [[universal class|ZSTEZ3PRT9]].

1. Irreflexivity is $\forall x \, \neg E(x, x)$, a universal sentence.
2. Symmetry is $\forall x \forall y \, (E(x, y) \rightarrow E(y, x))$, a universal sentence.
3. Triangle-freeness is $\forall x \forall y \forall z \, \neg(E(x, y) \wedge E(y, z) \wedge E(x, z))$, a universal sentence. Irreflexivity makes $x, y, z$ distinct when the three edges hold.
4. An $L$-structure satisfies these three sentences exactly when it is a triangle-free graph.
5. So $\mathcal{K}$ is the class of models of a set of universal sentences.

## Remarks

The example shows the typical universal class: it forbids one finite pattern.
By [[this statement|C9494XYEMN]], every induced subgraph of a triangle-free graph is triangle-free, which one can also see directly.
Replacing the triangle by the complete graph $K_n$ gives the $K_n$-free graphs, also a universal class, with one axiom in $n$ variables.
Replacing "no triangle" by "some triangle" gives the existential sentence $\exists x \exists y \exists z \, (E(x, y) \wedge E(y, z) \wedge E(x, z))$, and the graphs that contain a triangle are not closed under substructures.
The class is not closed under homomorphic images: a proper $3$-coloring of the $5$-cycle is a homomorphism of graphs onto a triangle.
The countable [[generic triangle-free graph|AH6BAJW1DA]] is the Fraïssé limit of the finite members of this class.

## Explanations

### L1 human

A triangle in a network is three points that are all linked to each other.
A triangle-free network has no such three points.
If we keep only some points of the network, and the links between them, we still find no triangle.
That is why one rule that speaks about every three points at a time is enough to describe the class.

### L2 human

We check the axiom of step 3 on the $5$-cycle $C_5$, with vertices $0, 1, 2, 3, 4$ and edges $\set{i, i + 1 \bmod 5}$.

1. A triangle through the vertex $i$ needs two adjacent neighbors of $i$.
2. The neighbors of $i$ are $i - 1$ and $i + 1 \pmod 5$.
3. They differ by $2$, and $2 \not\equiv \pm 1 \pmod 5$, so they are not adjacent.
4. So $C_5$ is triangle-free, and so is every induced subgraph, such as the path on $\set{0, 1, 2, 3}$.

The typical use is to see that a class defined by forbidding a finite graph is universal.
A trap is to think that triangle-free graphs have few edges: the complete bipartite graph $K_{n, n}$ is triangle-free with $n^2$ edges.
