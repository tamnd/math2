---
tag: HC3VBBCJQP
kind: concept
name: Jet bundle
msc: [58A20, 55R10]
sources:
  - url: https://en.wikipedia.org/wiki/Jet_bundle
same_as:
  wikidata: Q6188933
  wikipedia: Jet bundle
---

## Summary

The $k$-th jet bundle of a [[fiber bundle|CX4M8K61AB]] $E \to M$ is the manifold of all [[$k$-jets|1QE0Z0756D]] of local sections of $E$.
A point of it records a point of $M$, a value in the fiber and all derivatives up to order $k$ of a section there.
It is the natural home of differential equations on bundles: an equation of order $k$ is a subset of the $k$-th jet bundle.
Jet bundles are used in the calculus of variations, in the geometric theory of partial differential equations and in field theory.

## Explanations

### L1 human

For a function $u(x)$ of one variable, the first jet bundle has three coordinates: the point $x$, the value $u$ and the slope $u_x$.
Every function $u$ gives a curve $x \mapsto (x, u(x), u'(x))$ in this three-dimensional space.
A first-order differential equation such as $u_x = u$ is just a surface in that space.
Solving the equation means finding functions whose curves stay in that surface.
Higher jet bundles add coordinates for higher derivatives.
