---
tag: 2V9Q4KHY1T
kind: concept
name: Fredholm index
msc: [47A53]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_operator
---

## Summary

The index of a Fredholm operator is the dimension of its kernel minus the dimension of its cokernel.
It is an integer that does not change under small perturbations, under compact perturbations, or along continuous paths of Fredholm operators.
The Atiyah–Singer index theorem computes it for elliptic differential operators in terms of topology.

## Explanations

### L1 human

The index counts how many more solutions a linear equation has than conditions it fails to meet.
The kernel counts independent solutions of $Tx = 0$, and the cokernel counts independent directions missed by $T$.
For a linear map from $\R^5$ to $\R^3$, the index is always $5 - 3 = 2$, whatever the map is.
The surprise is that in infinite dimensions the index is still stable under small changes, although the kernel and cokernel alone can jump.
