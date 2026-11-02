---
tag: 6H3WCCHZB5
kind: concept
name: Hecke algebra of a locally compact group
msc: [22D20, 20C08, "22E50"]
sources:
  - url: https://en.wikipedia.org/wiki/Hecke_algebra_of_a_pair
---

## Summary

Let $K$ be a compact open subgroup of a [[locally compact group|AHV05ZBCYW]] $G$.
The Hecke algebra of $(G, K)$ is the algebra of compactly supported $K$-bi-invariant functions on $G$ under [[convolution|2Z29JN3VES]].
It has a basis given by the indicator functions of the double cosets $K g K$.
The $K$-fixed vectors of a smooth representation of $G$ form a module over it.
This makes it a main tool for representations of $p$-adic groups.
For $G = \mathrm{GL}_n(\Q_p)$ and $K = \mathrm{GL}_n(\Z_p)$ it is commutative, and it is closely related to the [[Hecke operators|S4SV3QZ8B1]] on modular forms.

## Explanations

### L1 human

Pick a compact open subgroup $K$, like $\mathrm{GL}_2(\Z_p)$ inside $\mathrm{GL}_2(\Q_p)$.
The group is then cut into double cosets $KgK$, which are like coarse blocks of the group.
The Hecke algebra records how these blocks multiply: the product of two blocks spreads over several blocks with integer multiplicities.
For a discrete group with $K$ trivial, the blocks are single elements and one gets the ordinary group algebra.
