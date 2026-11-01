---
tag: KXJG5VV340
kind: concept
name: Frattini subgroup
msc: [20D25, "20E28"]
specializes: [0KABPMRHM2]
sources:
  - url: https://en.wikipedia.org/wiki/Frattini_subgroup
same_as:
  wikidata: Q176244
  wikipedia: Frattini subgroup
---

## Summary

The Frattini subgroup $\Phi(G)$ of a group $G$ is the intersection of all maximal subgroups of $G$.
It is exactly the set of non-generators: elements that can be dropped from any generating set without changing the group generated.
It is a [[characteristic subgroup|0KABPMRHM2]], and for a finite group it is [[nilpotent|0Q7MMQHC1P]].
For a finite [[p-group|06QYRTX9KQ]] $P$, the quotient $P/\Phi(P)$ is elementary abelian, and its dimension is the minimal number of generators of $P$.

## Explanations

### L1 human

Some elements of a group are useless for generating it.
If a set of elements together with such an element generates the whole group, the set already generates it without that element.
The Frattini subgroup collects all these useless elements.
In the cyclic group $\Z/8\Z$, the even residues are useless: any generating set must contain an odd residue, which alone generates the group.
So the Frattini subgroup of $\Z/8\Z$ is $\set{0, 2, 4, 6}$.
