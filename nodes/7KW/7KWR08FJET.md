---
tag: 7KWR08FJET
kind: concept
name: Level-set method
msc: [65M06, 35F21, 65D18]
sources:
  - url: https://en.wikipedia.org/wiki/Level-set_method
same_as:
  wikidata: Q1751397
  wikipedia: Level-set method
---

## Summary

The level-set method tracks a moving curve or surface as the zero [[level set|0B2RZ0778N]] of a function $\phi(x, t)$ defined on a fixed grid.
The motion of the interface becomes a [[Hamilton–Jacobi equation|5TRXQKP7DY]] for $\phi$, which is solved with finite difference schemes.
It was introduced by Stanley Osher and James Sethian.
Its main strength is that merging and splitting of interfaces need no special treatment, and normals and curvature are computed from derivatives of $\phi$.
See the [[definition|KT0380H39M]].

## Explanations

### L1 human

Think of a landscape whose shoreline is the interface you want to follow.
Instead of moving points along the shoreline, you raise or lower the whole landscape, and the shoreline moves by itself.
If two islands grow and touch, the shoreline simply changes its shape, with no bookkeeping.
For a circle of radius $r_0$ that grows at unit speed, the function $\phi(x, t) = \abs{x} - (r_0 + t)$ works: its zero set at time $t$ is the circle of radius $r_0 + t$.
