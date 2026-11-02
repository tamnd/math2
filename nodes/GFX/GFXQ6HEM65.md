---
tag: GFXQ6HEM65
kind: concept
name: Fredholm map
msc: [58B15, 47A53, 58C25]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_operator
---

## Summary

A Fredholm map is a differentiable map between [[Banach manifolds|9K15AMGBV9]] whose derivative at every point is a [[Fredholm operator|8HWGKWD6ZM]].
Its index, the index of the derivative, is locally constant, and it plays the role of the difference of dimensions of source and target.
Nonlinear elliptic equations on compact manifolds give Fredholm maps between Sobolev spaces of maps.
The [[Sard–Smale theorem|Z0NPFYDVP2]] extends Sard's theorem to Fredholm maps, so that the solution spaces of generic perturbed elliptic equations are finite-dimensional manifolds.

## Explanations

### L1 human

A map between finite-dimensional spaces of dimensions $m$ and $n$ has, at a regular point, solution sets of dimension $m - n$.
A Fredholm map is a map between infinite-dimensional spaces that still behaves like this: infinitely many equations in infinitely many unknowns, but with a finite and well-defined difference.
That difference is the index.
For instance, the map $(x_1, x_2, x_3, \dots) \mapsto (x_2, x_3, \dots)$ on $\ell^2$ is linear and Fredholm of index $1$: one unknown is left free.
