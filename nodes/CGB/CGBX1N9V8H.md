---
tag: CGBX1N9V8H
kind: concept
name: Differential operator between vector bundles
msc: [58J99, 47F05, 35A99]
sources:
  - url: https://en.wikipedia.org/wiki/Differential_operator
---

## Summary

A differential operator between [[vector bundles|P4DZM975BV]] over a manifold is a linear map from [[sections|WWX7H5W1RP]] of one bundle to sections of the other.
In local coordinates and trivialisations, it is a matrix of partial derivatives with smooth coefficients.
It is the coordinate-free form of a [[linear system of partial differential equations|6DZETZ5T9G]] on a manifold.
The exterior derivative, the Laplacian on forms, Dirac operators and connections are all examples.
Global analysis studies these operators on compact manifolds, where their properties are tied to the topology of the manifold.

## Explanations

### L1 human

On $\R^n$, a linear differential operator takes a function and returns a combination of its partial derivatives, with coefficients depending on the point.
On a manifold, the functions are often replaced by sections of a vector bundle, such as vector fields or differential forms.
A differential operator between bundles does the same job: in each small coordinate patch it is a matrix of ordinary partial derivative operators.
For example, the exterior derivative turns $1$-forms into $2$-forms, and in coordinates it takes $f \, dx + g \, dy$ to $(\partial_x g - \partial_y f) \, dx \wedge dy$.
