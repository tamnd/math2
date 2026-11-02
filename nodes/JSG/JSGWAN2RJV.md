---
tag: JSGWAN2RJV
kind: concept
name: Complex manifold
msc: [32Q99, 53C15]
specializes: [F45VQ47GPV]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_manifold
same_as:
  wikidata: Q578874
  wikipedia: Complex manifold
---

## Summary

A complex manifold is a space that looks locally like an open subset of $\C^n$, glued together by holomorphic maps.
It is the setting for complex analysis beyond domains in $\C^n$, just as a [[smooth manifold|F45VQ47GPV]] is the setting for calculus.
[[Riemann surfaces|5K0N8QMV6Q]] are the complex manifolds of dimension $1$; complex projective space and complex tori are basic compact examples.
Compact complex manifolds behave very differently from smooth ones: for instance, on a compact connected complex manifold the only global holomorphic functions are the constants.

## Explanations

### L1 human

A complex manifold is built from pieces of $\C^n$ that are glued along overlaps.
The gluing rules must be holomorphic, so that the notion of a holomorphic function makes sense on the whole space.
The Riemann sphere is an example: it is made of two copies of the complex plane, glued by $z \mapsto 1/z$ away from $0$.
Every complex manifold of dimension $n$ is also a smooth manifold of real dimension $2n$, but a smooth manifold can carry many complex structures, or none.
