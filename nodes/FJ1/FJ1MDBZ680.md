---
tag: FJ1MDBZ680
kind: concept
name: Schouten–Nijenhuis bracket
msc: [58A10, 17B70, 53D17]
sources:
  - url: https://en.wikipedia.org/wiki/Schouten%E2%80%93Nijenhuis_bracket
same_as:
  wikidata: Q7432782
  wikipedia: Schouten–Nijenhuis bracket
---

## Summary

The Schouten–Nijenhuis bracket extends the [[Lie bracket of vector fields|68FGQEBD6J]] to multivector fields, the sections of the exterior powers of the tangent bundle.
It lowers the total degree by one and obeys graded versions of antisymmetry, the Jacobi identity and the Leibniz rule.
Its main use is in [[Poisson geometry|A2KQ49Y4NF]]: a bivector field $\pi$ defines a Poisson structure exactly when $[\pi, \pi] = 0$.
It also describes the deformation theory of Poisson structures through Poisson cohomology.

## Explanations

### L1 human

A vector field is an arrow at each point; a bivector field is an oriented little parallelogram at each point, and so on.
The Lie bracket combines two vector fields into a third.
The Schouten–Nijenhuis bracket does the same for these higher objects, with signs that keep track of degrees.
For example, the bracket of a vector field with any multivector field is the derivative of the multivector field along the flow of the vector field.
