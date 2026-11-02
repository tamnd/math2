---
tag: MWB6Y5Q4VK
kind: concept
name: Extended finite element method
msc: [65N30, 74S05, 74R10]
specializes: [98GZ9DVHTA]
sources:
  - url: https://en.wikipedia.org/wiki/Extended_finite_element_method
same_as:
  wikidata: Q3333647
  wikipedia: Extended finite element method
---

## Summary

The extended finite element method, or XFEM, enriches a standard [[finite element|98GZ9DVHTA]] space with extra functions.
These carry known features of the solution, such as a jump across a crack.
The enrichment is built with the [[partition of unity|NH739XXVXK]] formed by the usual shape functions.
So cracks, interfaces and inclusions can cut through elements, and the mesh does not need to follow them.
It was developed in fracture mechanics by Ted Belytschko and coworkers, and is often combined with the [[level-set method|7KWR08FJET]] to describe the moving crack.
See the [[definition|35KXRGMAHT]].

## Explanations

### L1 human

A crack in a plate makes the displacement jump across the crack faces.
Ordinary finite elements are continuous, so they need a mesh that is cut exactly along the crack, and a new mesh whenever the crack grows.
XFEM keeps a fixed mesh and adds a jump function, such as a step that is $0$ on one side and $1$ on the other, near the crack.
The method then finds how much of this step each node needs.
