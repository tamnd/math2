---
tag: JDH0THTVGM
kind: concept
name: Householder transformation
msc: [65F25, 15A23]
specializes: [06BRDF3F0E]
sources:
  - url: https://en.wikipedia.org/wiki/Householder_transformation
same_as:
  wikidata: Q304490
  wikipedia: Householder transformation
---

## Summary

A Householder transformation is the [[reflection|06BRDF3F0E]] of $\R^n$ or $\C^n$ in a hyperplane through the origin.
Its matrix is $I - 2 v v^*$ for a unit vector $v$ normal to the hyperplane.
It is an [[orthogonal|0W02QESPJQ]] or unitary matrix, and in $\R^n$ it can send any given vector to any other vector of the same length.
This makes it the basic tool for creating zeros in a matrix in a stable way.
It is used in the [[QR decomposition|0ERWG4NXQ9]] and in the reduction to Hessenberg or tridiagonal form.

## Explanations

### L1 human

Think of a mirror through the origin.
The Householder transformation reflects every vector in this mirror: the part along the mirror stays, and the part perpendicular to it flips sign.
By placing the mirror halfway between two vectors of the same length, one can swap them.
For example, the mirror between $(3, 4)$ and $(5, 0)$ in the plane sends $(3, 4)$ to $(5, 0)$, so the second entry becomes zero.
