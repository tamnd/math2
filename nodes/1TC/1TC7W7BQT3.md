---
tag: 1TC7W7BQT3
kind: concept
name: Slice category
msc: [18A25]
specializes: [PC6HG1JEGM]
sources:
  - url: https://en.wikipedia.org/wiki/Comma_category
---

## Summary

The slice category $\mathcal{C}/X$ of a [[category|A2DE66937D]] $\mathcal{C}$ over an object $X$ has the morphisms into $X$ as objects.
Its morphisms are the commuting triangles over $X$.
It is the [[comma category|PC6HG1JEGM]] $(1_{\mathcal{C}} \downarrow X)$.
Slice categories describe objects "over a base": families of sets indexed by $X$, spaces over a base space, and schemes over a base scheme.
The dual notion is the coslice category $X/\mathcal{C}$ of morphisms out of $X$, such as the category of pointed sets.

## Explanations

### L1 human

Fix an object $X$ and look at all arrows that end at $X$.
Each such arrow $A \to X$ is an object of the slice.
A map between two of them is a map of the sources that is compatible with the arrows to $X$.
For sets, a map $h \colon A \to I$ splits $A$ into the pieces $h^{-1}(i)$, one for each $i \in I$.
So a set over $I$ is a family of sets indexed by $I$, and maps over $I$ are maps sending each piece into the matching piece.
