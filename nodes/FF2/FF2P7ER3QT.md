---
tag: FF2P7ER3QT
kind: concept
name: Plurisubharmonic function
msc: [32U05, 31C10]
specializes: [Z1MHMGFNFW]
sources:
  - url: https://en.wikipedia.org/wiki/Plurisubharmonic_function
same_as:
  wikidata: Q7205565
  wikipedia: Plurisubharmonic function
---

## Summary

A plurisubharmonic function on an open subset of $\C^n$ is an upper semicontinuous function whose restriction to every complex line is [[subharmonic|Z1MHMGFNFW]].
For $C^2$ functions this means that the complex Hessian $\left(\partial^2 u / \partial z_j \partial \bar z_k\right)$ is positive semidefinite, that is, the [[Levi form|80MTNXWW80]] is nonnegative.
If $f$ is [[holomorphic|507C34W0ZT]], then $\log\abs{f}$ is plurisubharmonic, and this is the main source of examples.
Plurisubharmonic functions are the basic objects of pluripotential theory, and they characterise [[pseudoconvexity|AHYZMSBBNH]] and domains of holomorphy.

## Explanations

### L1 human

A subharmonic function of one complex variable lies below the harmonic function with the same values on any circle.
A plurisubharmonic function of several complex variables has this property on every complex line through every point.
Convex functions are examples, but the class is much larger, because only complex directions matter.
For example, $u(z_1, z_2) = \abs{z_1}^2$ is plurisubharmonic on $\C^2$: on each complex line it is the squared modulus of an affine function of one variable.
The function $\log\abs{z_1 z_2 - 1}$ is plurisubharmonic too, and it equals $-\infty$ on the curve $z_1 z_2 = 1$.
