---
tag: W9QTFV0Z8D
kind: concept
name: End and coend
msc: [18A30, 18A23]
sources:
  - url: https://en.wikipedia.org/wiki/End_(category_theory)
same_as:
  wikidata: Q5375781
  wikipedia: End (category theory)
---

## Summary

An end is a universal way of extracting from a [[functor|28NQ0KRHD3]] $S \colon \mathcal{C}^{\mathrm{op}} \times \mathcal{C} \to \mathcal{D}$ an object that is compatible with all the diagonal values $S(c, c)$.
A coend is the dual notion.
Ends are special [[limits|CHS5AFJGWE]] and coends are special [[colimits|BJS1CGTKQ5]].
The set of [[natural transformations|KYCPCC57FT]] between two functors is an end, and many constructions such as tensor products and Kan extensions are coends or ends.

## Explanations

### L1 human

Some functors take two inputs from the same category, one in a backward and one in a forward way, like $\Hom(c, c')$.
An end picks out the families of diagonal elements, one for each object $c$, that are consistent along all arrows.
For example, a natural transformation between two functors is a family of maps, one per object, consistent with all arrows.
So the natural transformations form the end of the functor $(c, c') \mapsto \Hom(F c, G c')$.
A coend glues the diagonal values together instead, and plays the role of a tensor product.
