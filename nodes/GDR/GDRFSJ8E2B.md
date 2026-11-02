---
tag: GDRFSJ8E2B
kind: concept
name: Grothendieck topology
msc: [18F10, 14F20]
sources:
  - url: https://en.wikipedia.org/wiki/Grothendieck_topology
same_as:
  wikidata: Q1062242
  wikipedia: Grothendieck topology
---

## Summary

A Grothendieck topology on a [[category|A2DE66937D]] says which families of morphisms into an object count as coverings of that object.
It is stated with [[sieves|CNCXNWKC6R]] and abstracts the open covers of a topological space.
A category with a Grothendieck topology is a [[site|NYE0Z94MME]], and one can define [[sheaves|RT8A8FJ566]] and sheaf cohomology on it.
Grothendieck introduced it to define étale cohomology of schemes, where the "open sets" are étale maps rather than subsets.

## Explanations

### L1 human

On a topological space, a sheaf is defined by gluing data along open covers.
A Grothendieck topology keeps only what is needed for this: a rule saying which collections of arrows into an object cover it.
The rule must contain the trivial cover, be stable when restricted to smaller pieces, and allow covers of covers.
For example, on the open sets of a space $X$, a family of open subsets of $U$ covers $U$ when its union is $U$.
