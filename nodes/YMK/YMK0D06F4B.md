---
tag: YMK0D06F4B
kind: definition
name: Site
msc: [18F10, 14F20]
defines: NYE0Z94MME
uses: [A2DE66937D, GDRFSJ8E2B]
sources:
  - url: https://en.wikipedia.org/wiki/Grothendieck_topology
---

## Definition

A *site* is a pair $(\mathcal{C}, J)$, where $\mathcal{C}$ is a [[category|A2DE66937D]] and $J$ is a [[Grothendieck topology|GDRFSJ8E2B]] on $\mathcal{C}$.
The site is *small* when $\mathcal{C}$ is a small category.

## Remarks

Example: for a topological space $X$, let $\mathcal{O}(X)$ be the category of open sets with inclusions.
Let a sieve on $U$ cover when the union of its members is $U$.
This rule satisfies the three axioms of a Grothendieck topology, so $(\mathcal{O}(X), J)$ is a small site.
Non-example: the category $\mathcal{O}(X)$ alone, with no choice of covering sieves, is not a site, since it does not say which families cover.
Some authors define a site with a Grothendieck pretopology, that is, with covering families of morphisms instead of covering sieves; each pretopology determines a topology with the same sheaves.
