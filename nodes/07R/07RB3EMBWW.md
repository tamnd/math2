---
tag: 07RB3EMBWW
kind: statement
role: theorem
name: Third isomorphism theorem for vector spaces
msc: [15A03, 16D10]
uses: [0SVR29SV1V]
sources:
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem C (modules)
---

## Statement

Let $F$ be a field, let $V$ be a vector space over $F$, and let $W \subseteq U$ be subspaces of $V$.
Then $U / W$ is a subspace of $V / W$, and the map
$$(V / W) / (U / W) \to V / U, \qquad (v + W) + U/W \mapsto v + U,$$
is well defined, and it is a linear isomorphism of [[quotient spaces|0BR3FY5Q8M]].

## Remarks

The proof applies the [[first isomorphism theorem|0MTBGVZ4XJ]] to the surjective map $V / W \to V / U$, $v + W \mapsto v + U$, whose kernel is $U / W$.
In finite dimensions, both sides have dimension $\dim V - \dim U$.

## Explanations

### L1 human

Dividing first by a small subspace and then by a larger one is the same as dividing by the larger one at once.
This works like cancelling in fractions.
The same theorem holds for groups, rings and modules.
