---
tag: K8T15QHN3W
kind: concept
name: Cohomology operation
msc: [55S05, 55S10]
sources:
  - url: https://en.wikipedia.org/wiki/Cohomology_operation
same_as:
  wikidata: Q5141397
  wikipedia: Cohomology operation
---

## Summary

A cohomology operation turns cohomology classes of one fixed degree into classes of another degree.
It does so on every space at once, compatibly with all continuous maps.
Examples are the cup square $x \mapsto x \smile x$, the [[Bockstein homomorphism|H7PCM776GR]] and the [[Steenrod squares|VR7RHP41M0]].
Operations give extra structure on cohomology that can distinguish spaces and maps with the same cohomology groups or rings.
By [[representability of cohomology|GPDPYHM3RE]], operations from degree $n$ with coefficients $G$ correspond to cohomology classes of the [[Eilenberg–MacLane space|AJHEYJE5XY]] $K(G, n)$.

## Explanations

### L1 human

Cohomology attaches groups to spaces, and maps between spaces give maps between these groups.
A cohomology operation is a recipe that works on the cohomology of every space and commutes with all these induced maps.
Squaring a class with the cup product is such a recipe, because induced maps respect cup products.
Operations are useful because a map must respect them, which can rule out maps that the groups alone allow.
