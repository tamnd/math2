---
tag: XY8GEQSWPR
kind: concept
name: Elliptic operator
msc: [47F10, 35J99]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_operator
same_as:
  wikidata: Q427625
  wikipedia: Elliptic operator
---

## Summary

An elliptic operator is a linear differential operator whose principal symbol does not vanish at any nonzero covector.
The [[Laplacian|0E0B6RA8K0]] is the model example.
Elliptic operators have strong regularity properties: solutions of $Lu = f$ are as smooth as the data allow.
On compact manifolds they are Fredholm, which is the setting of index theory.

## Explanations

### L1 human

A linear differential operator is a sum of derivatives of a function, each multiplied by a coefficient.
The terms of highest order decide most of its behaviour, and the principal symbol records them by replacing each derivative $\partial_j$ by a variable $\xi_j$.
The operator is elliptic when this polynomial in $\xi$ vanishes only at $\xi = 0$.
For the Laplacian $\partial_1^2 + \partial_2^2$ the symbol is $\xi_1^2 + \xi_2^2$, which is zero only at the origin.
For the wave operator $\partial_t^2 - \partial_x^2$ the symbol $\tau^2 - \xi^2$ vanishes on the lines $\tau = \pm \xi$, so it is not elliptic.
Indeed, waves can carry sharp edges, while solutions of Laplace's equation are smooth.
