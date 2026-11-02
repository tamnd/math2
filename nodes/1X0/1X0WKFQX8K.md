---
tag: 1X0WKFQX8K
kind: concept
name: Functor category
msc: [18A25, 18A23]
specializes: [A2DE66937D]
sources:
  - url: https://en.wikipedia.org/wiki/Functor_category
same_as:
  wikidata: Q2007878
  wikipedia: Functor category
---

## Summary

The functor category $[\mathcal{C}, \mathcal{D}]$, also written $\mathcal{D}^{\mathcal{C}}$, has the [[functors|28NQ0KRHD3]] from $\mathcal{C}$ to $\mathcal{D}$ as objects and the [[natural transformations|KYCPCC57FT]] between them as morphisms.
Many familiar categories are functor categories: sets with a group action, directed graphs, and [[presheaves|AND2WHZC8P]] on a topological space.
Its isomorphisms are the natural isomorphisms.
Functor categories into the category of sets are the setting of the [[Yoneda lemma|D6DF1ARPVD]].

## Explanations

### L1 human

Functors from one category to another can themselves be treated as objects, with natural transformations as the arrows between them.
For example, a group $G$ is a category with one object whose arrows are the elements of $G$.
A functor from it to sets is a set on which $G$ acts, and a natural transformation is a map that commutes with the action.
So the category of $G$-sets is a functor category.
