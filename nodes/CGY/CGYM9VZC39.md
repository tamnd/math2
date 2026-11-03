---
tag: CGYM9VZC39
kind: concept
name: Finite element method in structural mechanics
msc: [74S05, 65N30]
specializes: [98GZ9DVHTA]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_element_method_in_structural_mechanics
same_as:
  wikidata: Q5450397
  wikipedia: Finite element method in structural mechanics
---

## Summary

The finite element method in structural mechanics is the [[finite element method|98GZ9DVHTA]] applied to the equilibrium of elastic bodies and structures.
The body is cut into small elements, and the displacement is approximated by simple functions on each element.
The [[minimum total potential energy principle|A5T30ZHVGH]] then turns the equilibrium problem into a linear system $K d = F$.
Here $K$ is the global [[stiffness matrix|G8ZTW9JVX1]], $d$ the vector of nodal displacements and $F$ the vector of nodal loads.
It is the standard tool for computing deformations and stresses in engineering design.

## Explanations

### L1 human

A real structure, such as a bridge or a machine part, has a shape too complicated for exact formulas.
The method splits it into many small simple pieces, such as triangles, bricks or short beams, joined at points called nodes.
For each piece one computes how strongly it resists moving its nodes.
Putting all pieces together gives a large system of linear equations for the node displacements.
For example, a bar cut into two equal pieces gives a $3 \times 3$ system for its three nodes, and fixing one end makes it solvable.
