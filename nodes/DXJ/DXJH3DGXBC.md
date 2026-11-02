---
tag: DXJH3DGXBC
kind: concept
name: Section and retraction
msc: [18A20]
sources:
  - url: https://en.wikipedia.org/wiki/Section_(category_theory)
same_as:
  wikidata: Q60727552
  wikipedia: Section (category theory)
---

## Summary

When two [[morphisms|859F0TFVA3]] $f \colon A \to B$ and $r \colon B \to A$ satisfy $r \circ f = 1_A$, the morphism $f$ is a section of $r$ and $r$ is a retraction of $f$.
A morphism with a retraction is a split [[monomorphism|Y2NP1JFR86]], and a morphism with a section is a split [[epimorphism|RVXDSY04KG]].
These are one-sided forms of invertibility, and every functor preserves them.
In linear algebra and homological algebra, split monomorphisms and split epimorphisms describe direct summands.

## Explanations

### L1 human

A section is a morphism that can be undone from one side, though perhaps not from the other.
Think of $f$ as placing $A$ inside $B$ and of $r$ as folding $B$ back onto $A$ so that each placed point returns to where it came from.
For example, put $f \colon \R \to \R^2$, $f(x) = (x, 0)$, and $r \colon \R^2 \to \R$, $r(x, y) = x$.
Then $r(f(x)) = x$ for every $x$, so $f$ is a section of $r$ and $r$ is a retraction of $f$.
The other composite $f(r(x, y)) = (x, 0)$ is not the identity, so neither map is an isomorphism.
