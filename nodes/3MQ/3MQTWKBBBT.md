---
tag: 3MQTWKBBBT
kind: concept
name: Holomorphic map
msc: [32H02, 32A10]
sources:
  - url: https://en.wikipedia.org/wiki/Holomorphic_function
---

## Summary

A holomorphic map from an open subset of $\C^n$ to $\C^m$ is a map whose $m$ components are [[holomorphic functions of several variables|507C34W0ZT]].
Holomorphic maps are the morphisms of [[several complex variables|BH57D2FBNR]] and of complex manifolds.
Their derivative at each point is a complex linear map, given by the complex Jacobian matrix $(\partial F_k / \partial z_j)$.
For $n = m = 1$ they are the holomorphic functions of one variable, and [[holomorphic maps between Riemann surfaces|T19P7J53A1]] are the same notion for complex curves.

## Explanations

### L1 human

A holomorphic function returns one complex number; a holomorphic map returns several, each depending holomorphically on the inputs.
Near each point it looks like a complex linear map, up to a small error.
For example, $F(z_1, z_2) = (z_1 + z_2^2, \ e^{z_1})$ is a holomorphic map from $\C^2$ to $\C^2$.
Compositions of holomorphic maps are again holomorphic.
