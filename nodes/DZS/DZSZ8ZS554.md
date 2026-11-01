---
tag: DZSZ8ZS554
kind: concept
name: Elementary abelian group
msc: [20K01, 20D15]
specializes: [082GHNPJ53]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_abelian_group
same_as:
  wikidata: Q1017231
  wikipedia: Elementary abelian group
---

## Summary

An elementary abelian $p$-group, for a prime $p$, is an [[abelian group|082GHNPJ53]] in which every element other than the identity has order $p$.
Such a group is the same thing as a [[vector space|000AYPA9AJ]] over the field $\F_p$.
So a finite one is isomorphic to $(\Z/p\Z)^n$ for some $n$.
They appear everywhere in finite group theory.
For example, minimal normal subgroups of finite solvable groups are elementary abelian, and so is the quotient of a finite [[p-group|06QYRTX9KQ]] by its Frattini subgroup.

## Explanations

### L1 human

Take $n$ switches, each of which can be on or off, and combine two settings by flipping the switches that are on in the second one.
Doing the same move twice brings you back to the start, so every element has order $2$.
This is the elementary abelian group $(\Z/2\Z)^n$ with $2^n$ elements.
For $n = 2$ it is the Klein four-group.
Replacing on/off by the $p$ residues modulo a prime $p$ gives $(\Z/p\Z)^n$.
