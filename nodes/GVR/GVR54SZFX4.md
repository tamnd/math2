---
tag: GVR54SZFX4
kind: concept
name: Smale's degree for proper Fredholm maps
msc: [58C25, 58B15, 47H11]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_operator
---

## Summary

Smale's degree is a mod $2$ degree for proper [[Fredholm maps|GFXQ6HEM65]] of index $0$ between connected Banach manifolds.
It counts the preimages of a regular value modulo $2$.
It extends the mod $2$ [[degree of a continuous map|TMFG2P912R]] between compact manifolds of the same dimension to infinite dimensions.
It rests on the [[Sard–Smale theorem|Z0NPFYDVP2]], which supplies regular values.

## Explanations

### L1 human

For a map between two spaces of the same finite dimension, one can pick a typical point of the target and count how many points land on it.
Modulo $2$, this count does not depend on the point chosen, as long as the map is proper.
Smale noticed that the same count works in infinite dimensions when the derivative of the map is a [[Fredholm operator|8HWGKWD6ZM]] of index $0$.
Such an operator behaves like a square matrix up to finite-dimensional errors.
For example, $x \mapsto x^3$ on $\R$ has one preimage over every point, so its degree is $1$.
The map $x \mapsto x^2$ has two preimages over $1$ and none over $-1$, so its degree is $0$.
