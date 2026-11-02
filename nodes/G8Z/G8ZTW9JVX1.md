---
tag: G8ZTW9JVX1
kind: concept
name: Stiffness matrix
msc: [65N30, 74S05]
sources:
  - url: https://en.wikipedia.org/wiki/Stiffness_matrix
same_as:
  wikidata: Q3851930
  wikipedia: Stiffness matrix
---

## Summary

The stiffness matrix is the matrix of the linear system that the [[finite element method|98GZ9DVHTA]] produces from the bilinear form of a boundary value problem.
Its entries are the values of the form on pairs of basis functions.
Because finite element basis functions have small supports, the matrix is [[sparse|JGACZYEEY7]].
For symmetric coercive problems such as the Poisson equation it is [[symmetric|0VR671PHE5]] and [[positive definite|0KX66CZMBB]].
The name comes from structural mechanics, where the matrix links the displacements of the nodes with the forces on them.
See the [[definition|DPR9DJRPAF]].

## Explanations

### L1 human

Think of a chain of springs whose ends are tied to walls.
If you push one joint, the forces on that joint and on its two neighbours change, and nothing else.
The stiffness matrix records these numbers: row $i$ says how the force at joint $i$ depends on the positions of all joints.
For equal springs in a chain, each row has $2$ on the diagonal and $-1$ next to it, and zeros elsewhere.
