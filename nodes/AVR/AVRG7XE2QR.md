---
tag: AVRG7XE2QR
kind: concept
name: Quotient type
sources:
  - wikipedia: en:42011185@r1316023810
    locator: Quotient type
    note: adopted
    mention: wikipedia://en/42011185
    sections: [Summary]
same_as:
  wikidata: Q17045118
  wikipedia: Quotient type
inventory: [31A6BAMCZB]
---

## Summary

In the field of type theory in computer science, a **quotient type** is a data type that respects a user-defined equality relation. A quotient type defines an [[equivalence relation|0G8VEZ3WTK]] $\equiv$ on elements of the type — for example, we might say that two values of the type `Point` are equivalent if they have the same respective x- and y-coordinates; formally `p1 == p2` if `p1.x == p2.x && p1.y == p2.y`. In type theories that allow quotient types, an additional requirement is made that all operations must respect the equivalence between elements. For example, if `f` is a function on values of type `Point`, it must be the case that for two `Point`s `p1` and `p2`, if `p1 == p2` then `f(p1) == f(p2)`.
