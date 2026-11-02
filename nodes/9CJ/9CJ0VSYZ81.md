---
tag: 9CJ0VSYZ81
kind: definition
name: Topological vector space
msc: [46A03, 57N17]
defines: T32W553W95
uses: [000AYPA9AJ, 0CQHFPGJ45, 0GBG8B49AA, 0VGFHTM75Y]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_vector_space
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$ with its usual topology.
A *topological vector space* over $\mathbb{K}$ is a [[vector space|000AYPA9AJ]] $E$ over $\mathbb{K}$ together with a [[topology|0CQHFPGJ45]] on $E$ such that:

1. the addition $E \times E \to E$, $(x, y) \mapsto x + y$, is [[continuous|0VGFHTM75Y]];
2. the scalar multiplication $\mathbb{K} \times E \to E$, $(\lambda, x) \mapsto \lambda x$, is continuous.

Both products carry the [[product topology|0GBG8B49AA]].

## Remarks

Example: $\R^n$ with the Euclidean topology.
Addition and scalar multiplication are given by polynomials in the coordinates, so both are continuous.
Non-example: $\R$ as a vector space over $\R$ with the discrete topology.
Addition is continuous, but scalar multiplication fails clause 2.
If it were continuous, then the map $\lambda \mapsto \lambda \cdot 1$ from $\mathbb{K}$ to $E$ would be continuous.
Then the preimage $\set{1}$ of the open set $\set{1}$ would be open in $\mathbb{K}$, which is false.
Many authors also require the topology to be Hausdorff.
The definition extends to vector spaces over any topological field.
