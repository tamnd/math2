---
tag: 901CCKQHVY
kind: concept
name: Exterior differential system
msc: [58A15]
sources:
  - url: https://en.wikipedia.org/wiki/Differential_ideal
---

## Summary

An exterior differential system on a [[smooth manifold|F45VQ47GPV]] is an [[ideal|096Z9MP2ME]] of [[differential forms|0E3G0GRPZ6]] that is closed under the [[exterior derivative|0ZHSTAG8ZY]].
Its integral manifolds are the submanifolds on which all forms of the ideal vanish.
Every system of partial differential equations can be written as an exterior differential system, so that solutions become integral manifolds.
The theory, largely due to Élie Cartan, studies existence and size of integral manifolds in a way that does not depend on coordinates.

## Explanations

### L1 human

A differential equation can be rewritten as a set of conditions "this form must vanish" on a space of variables and derivatives.
For example, the conditions $du - p\, dx = 0$ and $dp - u\, dx = 0$ on the space with coordinates $(x, u, p)$ describe curves with $p = du/dx$ and $dp/dx = u$, that is, solutions of $u'' = u$.
The curves on which these forms vanish are the integral manifolds.
Working with forms instead of equations makes changes of variables painless and shows the geometry of the solution set.
