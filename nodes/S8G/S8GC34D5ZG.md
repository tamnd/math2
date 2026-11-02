---
tag: S8GC34D5ZG
kind: concept
name: Principal symbol of an operator on a manifold
msc: [58J40, 35S05, 47F05]
sources:
  - url: https://en.wikipedia.org/wiki/Differential_operator
---

## Summary

The principal symbol of a [[differential operator between vector bundles|CGBX1N9V8H]] records the top-order part of the operator.
It is a bundle map that depends on a covector.
It is a function on the cotangent bundle with values in linear maps between the fibres.
It is homogeneous in the covector, of degree the order of the operator.
Unlike the full local expression of the operator, it does not depend on coordinates or trivialisations.
Ellipticity, characteristic directions and the index theorem are all phrased in terms of the principal symbol.
It is the manifold version of the [[principal symbol|F31T650DKY]] on $\R^n$.

## Explanations

### L1 human

In coordinates, a differential operator is a sum of partial derivatives with coefficients.
If one keeps only the derivatives of highest order and replaces each $\partial_j$ by a variable $\xi_j$, one gets a polynomial in $\xi$ with matrix coefficients.
The lower-order terms change when the coordinates change, but this top part does not, once $\xi$ is read as a covector.
For example, the exterior derivative $d$ has principal symbol "wedge with $\xi$": it sends a form $\omega$ to $\xi \wedge \omega$.
