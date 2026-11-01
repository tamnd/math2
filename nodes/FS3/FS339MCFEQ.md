---
tag: FS339MCFEQ
kind: concept
name: Logarithm of a matrix
msc: [15A16]
sources:
  - url: https://en.wikipedia.org/wiki/Logarithm_of_a_matrix
same_as:
  wikidata: Q902017
  wikipedia: Logarithm of a matrix
---

## Summary

A logarithm of a square matrix $A$ is a matrix $B$ whose [[matrix exponential|020M04FN1H]] is $A$.
Over the complex numbers, a matrix has a logarithm exactly when it is [[invertible|0EB9N0S33C]].
The logarithm is not unique, just as for the [[complex logarithm|02QGGD5G87]].
Matrix logarithms pass from a matrix Lie group to its Lie algebra.
They are also used to interpolate between rotations and to find the generator of a linear system from its flow.

## Explanations

### L1 human

For numbers, the logarithm undoes the exponential.
For matrices, a logarithm of $A$ is any matrix $B$ with $e^B = A$.
The rotation of the plane by an angle $\theta$ has the logarithm $\begin{pmatrix} 0 & -\theta \\ \theta & 0 \end{pmatrix}$, an infinitesimal rotation.
Adding $2\pi$ to $\theta$ gives the same rotation and another logarithm, so a logarithm is not unique.
