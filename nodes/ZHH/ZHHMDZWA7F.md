---
tag: ZHHMDZWA7F
kind: concept
name: Relative homotopy group
msc: [55Q05]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy_group
---

## Summary

The relative homotopy group $\pi_n(X, A, x_0)$ of a pair $A \subseteq X$ consists of homotopy classes of maps of an $n$-disk into $X$ with boundary in $A$.
It is the homotopy analogue of relative homology.
The relative groups fit into a long exact sequence with the [[homotopy groups|P976WYEFMB]] of $A$ and of $X$.
This sequence is the main tool for computing homotopy groups of fibrations.

## Explanations

### L1 human

A relative homotopy group counts disks in a big space whose rim lies in a smaller subspace.
Two such disks count as the same if one can be deformed into the other while the rim stays in the subspace.
Take the disk $D^2$ with its boundary circle as subspace.
The identity disk cannot be pushed off, and the group is $\Z$, counting how many times the rim winds around the circle.
