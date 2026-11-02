---
tag: 5W95QFHXPR
kind: concept
name: CW complex
msc: [57Q05, 55U10]
sources:
  - url: https://en.wikipedia.org/wiki/CW_complex
same_as:
  wikidata: Q189061
  wikipedia: CW complex
---

## Summary

A CW complex is a space built by gluing closed balls of increasing dimension, called cells.
Each ball is glued along its boundary sphere to the cells already present.
The class of CW complexes is flexible enough to contain spheres, projective spaces, Grassmannians, all [[simplicial complexes|V8GZ0W1ZZ5]] and, up to homotopy equivalence, all manifolds.
It is rigid enough for homotopy theory to work well.
Weak homotopy equivalences between CW complexes are homotopy equivalences, and homology can be computed cell by cell.
The letters C and W stand for closure-finite and weak topology, the two conditions of J. H. C. Whitehead's definition.

## Explanations

### L1 human

Start with a set of points, the $0$-cells.
Glue intervals to them by their ends, giving a graph.
Then glue disks along their boundary circles to the graph, then solid balls along their boundary spheres, and so on.
The sphere $S^2$ is a CW complex with one point and one disk whose whole boundary circle is glued to that point.
The torus is a CW complex with one point, two loops and one square glued along the word $aba^{-1}b^{-1}$.
