---
tag: 2FATVDAN2E
kind: concept
name: Reduced norm
msc: ["16K20", "16K50", 19B99]
sources:
  - url: https://en.wikipedia.org/wiki/Central_simple_algebra
    locator: Splitting field
---

## Summary

The reduced norm is a multiplicative map $\mathrm{Nrd} \colon A \to F$ on a [[central simple algebra|5HRKJBAY2V]] $A$ over a field $F$.
It is the determinant of the matrix of an element after the algebra is split into a matrix algebra over a larger field.
An element is invertible exactly when its reduced norm is nonzero.
The kernel of the reduced norm on $K_1(A)$ is the group [[SK1|AAB05HS00Y]] of the algebra.

## Explanations

### L1 human

A central simple algebra looks like a matrix algebra once the field of scalars is enlarged enough.
After that enlargement, each element is a matrix, and one can take its determinant.
The answer always lands back in the original field and does not depend on the choices.
For the quaternions $a + bi + cj + dk$, the reduced norm is $a^2 + b^2 + c^2 + d^2$.
