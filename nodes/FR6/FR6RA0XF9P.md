---
tag: FR6RA0XF9P
kind: concept
name: Meshfree methods
msc: [65N99, 65M99, 65D15]
sources:
  - url: https://en.wikipedia.org/wiki/Meshfree_methods
same_as:
  wikidata: Q14866890
  wikipedia: Meshfree methods
---

## Summary

Meshfree methods solve differential equations using only a cloud of nodes, with no mesh that connects them into elements.
Each node carries a shape function built from the positions of nearby nodes, for example by [[moving least squares|T0JZN6WP5X]] or by [[radial basis functions|ZBSXSTQM2J]].
This avoids the cost of [[mesh generation|RTSAFF4KFJ]] and handles large deformations, fragmentation and moving boundaries with ease.
Examples include [[smoothed-particle hydrodynamics|S9DG3SNXCV]], the element-free Galerkin method and radial basis function collocation.
See the [[definition|30GF7TK8YP]].

## Explanations

### L1 human

A finite element method needs the domain cut into triangles or boxes that fit together, which is hard for complicated or changing shapes.
A meshfree method only scatters points over the domain.
The value of the approximate solution at a place is a weighted mix of the values at nearby points.
If the material tears or splashes, the points just move along, and no mesh has to be rebuilt.
