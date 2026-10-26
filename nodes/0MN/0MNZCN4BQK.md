---
tag: 0MNZCN4BQK
kind: definition
name: Product of rings
msc: [16B99]
defines: 0QM2G72DXA
uses: [0894J980RK]
sources:
  - url: https://en.wikipedia.org/wiki/Product_of_rings
    locator: lead section
---

## Definition

Let $I$ be a set and let $(R_i)_{i \in I}$ be a family of [[rings|0894J980RK]].
The product $\prod_{i \in I} R_i$ is the set of families $(a_i)_{i \in I}$ with $a_i \in R_i$ for each $i \in I$.
Its addition is $(a_i)_{i \in I} + (b_i)_{i \in I} = (a_i + b_i)_{i \in I}$.
Its multiplication is $(a_i)_{i \in I} \cdot (b_i)_{i \in I} = (a_i \cdot b_i)_{i \in I}$.
With these operations, $\prod_{i \in I} R_i$ is a ring, with zero $(0)_{i \in I}$ and identity $(1)_{i \in I}$.

## Remarks

For two rings $R$ and $S$, the product is $R \times S = \{(r, s) : r \in R, s \in S\}$.
For each $j \in I$, the projection $\prod_{i \in I} R_i \to R_j$, $(a_i)_{i \in I} \mapsto a_j$, is a [[ring homomorphism|0GGE0Z0JQ1]].
The product of two nonzero rings is not an [[integral domain|09S3PFBEPM]]: in $R \times S$, $(1, 0) \cdot (0, 1) = (0, 0)$.

## Explanations

### L1 human

To multiply two pairs, you multiply the first entries and the second entries apart.
For example, in $\mathbb{Z} \times \mathbb{Z}$, $(2, 3) \cdot (4, 5) = (8, 15)$.
