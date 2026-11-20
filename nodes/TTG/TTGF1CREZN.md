---
tag: TTGF1CREZN
kind: example
name: An injective graph homomorphism that is not an embedding
msc: ["03C07", "05C60"]
topics: [AY09KYSW81]
audience: ug2
not_instance_of:
  - target: SCRB74SWQN
    note: the identity map from the path to the triangle is injective and preserves the edge relation, but it does not reflect it, since the non-edge between 1 and 3 becomes an edge
uses: [SCRB74SWQN, KBXSZC6BV1, 00C0BR7D7H, 09NWETVTNY]
sources:
  - url: https://en.wikipedia.org/wiki/Embedding
    locator: Universal algebra and model theory
---

## Example

Let $L = \set{E}$ with one binary relation symbol.
A [[graph|00C0BR7D7H]] is an $L$-structure in which $E$ is symmetric and irreflexive.
Let $\mathcal{A}$ have domain $\set{1, 2}$ and $E^{\mathcal{A}} = \emptyset$, and let $\mathcal{B}$ have domain $\set{1, 2}$ and $E^{\mathcal{B}} = \set{(1, 2), (2, 1)}$.
Let $h \colon \set{1, 2} \to \set{1, 2}$ be the identity map.

1. $h$ is [[injective|09NWETVTNY]].
2. $h$ is a [[homomorphism|KBXSZC6BV1]]: the condition $(a, b) \in E^{\mathcal{A}} \Rightarrow (h(a), h(b)) \in E^{\mathcal{B}}$ holds for all pairs, because $E^{\mathcal{A}}$ is empty.
3. $h$ does not reflect $E$: $(h(1), h(2)) = (1, 2) \in E^{\mathcal{B}}$, but $(1, 2) \notin E^{\mathcal{A}}$.

So $h$ is an injective homomorphism and not an [[embedding|SCRB74SWQN]].

## Remarks

The quantifier-free formula $\neg E(x, y)$ is true of $(1, 2)$ in $\mathcal{A}$ and false of $(h(1), h(2))$ in $\mathcal{B}$.
So an injective homomorphism need not preserve negated atomic formulas, while an embedding does.
In graph theory, injective homomorphisms correspond to subgraphs and embeddings correspond to induced subgraphs.
The image of $h$ is a subgraph of $\mathcal{B}$ with the same vertices and fewer edges, and it is not a substructure of $\mathcal{B}$.

For a signature without relation symbols, the example cannot happen: every injective homomorphism of groups, rings or vector spaces is an embedding.
Then the only way to fail is non-injectivity, as for the ring homomorphism $\Z \to \Z/2\Z$, where $0 \ne 2$ in $\Z$ and both map to $0$.

## Explanations

### L1 human

Think of two drawings with the same two dots.
The first drawing has no line between the dots, and the second has a line.
Sending each dot to itself keeps every line of the first drawing, because there is none.
But it does not keep the fact that the dots were not joined.
A true copy must keep both the lines and the missing lines.

### L2 human

We test the identity map from the path on $\set{1, 2, 3}$ with edges $\set{1, 2}$ and $\set{2, 3}$ to the triangle on $\set{1, 2, 3}$.

1. It is injective.
2. Each edge of the path is an edge of the triangle, so the map is a homomorphism.
3. The pair $(1, 3)$ is an edge of the triangle but not of the path, so the map does not reflect $E$.

So the map is not an embedding.
The typical use of this check is to tell subgraphs from induced subgraphs.
A trap is to check only the edges and to forget the non-edges.
