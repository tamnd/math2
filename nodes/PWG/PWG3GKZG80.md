---
tag: PWG3GKZG80
kind: concept
name: Hodge Laplacian
msc: [58A14, 58J05, 58A10]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_operators_in_differential_geometry
---

## Summary

The Hodge Laplacian is the operator $\Delta = d\delta + \delta d$ on [[differential forms|0E3G0GRPZ6]] of a Riemannian manifold, built from the [[exterior derivative|0ZHSTAG8ZY]] $d$ and its adjoint $\delta$.
On functions it is the [[Laplace–Beltrami operator|F4NWZNTRMD]], up to sign convention.
It is elliptic, self-adjoint and nonnegative, and on a closed manifold its kernel, the harmonic forms, represents the de Rham cohomology.
This is the content of [[Hodge theory|32YJXG30MF]], which links analysis on a manifold with its topology.

## Explanations

### L1 human

The ordinary Laplacian measures how much a function differs from its average nearby.
The Hodge Laplacian does the same for differential forms, such as vector fields written as $1$-forms.
On flat $\R^n$ it simply applies the negative of the usual Laplacian $-\sum_j \partial_j^2$ to each coefficient of the form.
On a curved manifold extra curvature terms appear, which is why it carries geometric information.
A form killed by it is called harmonic, and on a closed manifold each cohomology class contains exactly one harmonic form.
