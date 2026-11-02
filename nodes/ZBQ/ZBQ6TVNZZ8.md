---
tag: ZBQ6TVNZZ8
kind: concept
name: Kohn Laplacian
msc: [32W10, 32V20]
sources:
  - url: https://en.wikipedia.org/wiki/Dolbeault_cohomology
---

## Summary

The Kohn Laplacian is the second order operator $\square_b = \bar\partial_b \bar\partial_b^* + \bar\partial_b^* \bar\partial_b$ on a [[CR manifold|ZC78JKZX9S]], built from the [[tangential Cauchy–Riemann operator|X7GP9BECD8]] $\bar\partial_b$ and its adjoint.
It plays on the boundary of a domain in $\C^n$ the role that the complex Laplacian $\bar\partial \bar\partial^* + \bar\partial^* \bar\partial$ of the [[dbar-Neumann problem|Q4P4R2GDNG]] plays inside.
It is not elliptic, but on strongly pseudoconvex CR manifolds it is hypoelliptic in suitable degrees.
Its study gives the solution of the tangential Cauchy–Riemann equations and the [[Kohn–Rossi cohomology|VC48WDWPV1]].

## Explanations

### L1 human

On a real hypersurface in $\C^n$, such as a sphere, only some of the complex directions are tangent to the surface.
The tangential Cauchy–Riemann operator differentiates only in these directions.
The Kohn Laplacian combines this operator with its adjoint, in the same way as the usual Laplacian combines the gradient with the divergence.
On the Heisenberg group $\C \times \R$, which is a model of the boundary of a ball, it acts on functions as $-Z \bar Z$ for the vector fields $\bar Z = \partial/\partial \bar z - i z\, \partial/\partial t$ and $Z = \partial/\partial z + i \bar z\, \partial/\partial t$.
It differentiates twice in the $z$ directions but only indirectly in the $t$ direction, which is why it is not elliptic.
