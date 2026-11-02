---
tag: ZBKVRMWHMW
kind: concept
name: Category of posets
msc: [18B35, 06A06]
sources:
  - url: https://en.wikipedia.org/wiki/Category_of_preordered_sets
---

## Summary

The category of posets, written $\mathbf{Pos}$, has the [[partially ordered sets|011C29Q1S1]] as objects and the [[monotone functions|0WFF6AZPBP]] as morphisms.
Its isomorphisms are the [[order isomorphisms|0Y74KN99A5]].
It sits inside the larger category of preordered sets, and it lets order theory use the language of [[category theory|Q1RZT7DV0F]].

## Explanations

### L1 human

The category of posets collects all ordered sets and all maps that respect order.
Two such maps compose to another map that respects order, and the identity map respects order.
For example, $n \mapsto 2n$ from $\N$ to $\N$ and the inclusion of $\N$ into $\Z$ compose to a monotone map from $\N$ to $\Z$.
Treating posets this way makes products, sums and other constructions on orders into special cases of general constructions.
