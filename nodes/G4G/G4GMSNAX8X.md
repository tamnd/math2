---
tag: G4GMSNAX8X
kind: concept
name: Deficiency indices
msc: [47B25, 47A20]
sources:
  - url: https://en.wikipedia.org/wiki/Extensions_of_symmetric_operators
---

## Summary

The deficiency indices of a symmetric operator are two cardinal numbers that measure how far it is from being self-adjoint.
They are the dimensions of the solution spaces of $A^* u = i u$ and $A^* u = -i u$, where $A^*$ is the adjoint.
By von Neumann's theory, they decide whether the operator has self-adjoint extensions and describe all of them.

## Explanations

### L1 human

A symmetric operator, such as a derivative acting on functions that vanish near the boundary, may fail to be self-adjoint because its domain is too small.
The deficiency indices count the missing directions, in two ways that correspond to the two numbers $i$ and $-i$.
If both counts are zero, nothing is missing and the closure is already self-adjoint.
If they are equal, the operator can be made self-adjoint by adding the missing directions in a balanced way; if they differ, it cannot.
For $-i \, d/dx$ on functions vanishing near the ends of $[0,1]$, both indices are $1$, matching a one-parameter family of boundary conditions.
