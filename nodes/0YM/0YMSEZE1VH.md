---
tag: 0YMSEZE1VH
kind: definition
name: Free abelian group
msc: [20K15, 20K20]
defines: 0WJX8MGG37
uses: [071DDFVG4J, 085PND4KNT, 0H9K5D3RDV, 020Z5SEN27]
sources:
  - url: https://en.wikipedia.org/wiki/Free_abelian_group
    locator: Definition and examples
  - url: https://en.wikipedia.org/wiki/Free_abelian_group
    locator: Rank
  - url: https://en.wikipedia.org/wiki/Free_abelian_group
    locator: Subgroups
  - url: https://en.wikipedia.org/wiki/Free_group
    locator: Free abelian group
---

## Definition

Let $A$ be an [[abelian group|082GHNPJ53]], written additively.
A basis of $A$ is a subset $B \subseteq A$ such that each $a \in A$ has exactly one expression $a = k_1 b_1 + \cdots + k_n b_n$ with distinct $b_i \in B$ and nonzero integers $k_i$.
The group $A$ is a free abelian group when it has a basis.

## Remarks

The additive group $\mathbb{Z}$ is free abelian with basis $\{1\}$, and $\mathbb{Z}^2$ is free abelian with basis $\{(1, 0), (0, 1)\}$.
All bases of $A$ have the same cardinality, the rank, and a free abelian group of finite rank $n$ is [[isomorphic|08MG7H8JW5]] to $\mathbb{Z}^n$.
The free abelian group on a set $S$ is the [[abelianisation|0AQZV0905N]] of the [[free group|0KTW26C80J]] $F_S$.
Each subgroup of a free abelian group is free abelian.

## Explanations

### L1 human

A free abelian group is like a vector space over the integers with a basis.
Each element is an integer combination of basis elements in exactly one way.
The standard examples are $\mathbb{Z}^n$ for $n \geq 0$.
