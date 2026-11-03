---
tag: AAB05HS00Y
kind: concept
name: SK1
msc: [19B99, 19B28]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Summary

For a commutative ring $R$, the group $SK_1(R)$ is the kernel of the determinant map $K_1(R) \to R^\times$.
Here $K_1(R)$ is [[K1 of a ring|SXVNJY4XFY]] and $R^\times$ is the group of units.
It collects the part of $K_1(R)$ that the determinant cannot see, and $K_1(R) \cong R^\times \oplus SK_1(R)$.
It vanishes for fields, for local rings and for Euclidean domains.
Bass, Milnor and Serre showed that it also vanishes for rings of integers of number fields.
A parallel group $SK_1(A)$, defined with the [[reduced norm|2FATVDAN2E]], exists for central simple algebras.

## Explanations

### L1 human

The determinant gives a map from $K_1$ to the units of the ring.
$SK_1$ is what is left over: matrices of determinant $1$ that cannot be reduced to the identity by row operations, even after enlarging them.
For most rings met in a first course, such as fields or the integers, nothing is left over.
When $SK_1$ is not zero, the ring has invertible matrices that the determinant fails to classify.
