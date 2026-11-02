---
tag: NZ8XFNCKQW
kind: concept
name: Flux limiter
msc: [65M08, 35L65]
sources:
  - url: https://en.wikipedia.org/wiki/Flux_limiter
same_as:
  wikidata: Q5463027
  wikipedia: Flux limiter
---

## Summary

A flux limiter is a function used in high-resolution schemes for [[conservation laws|8RA7AMWSAF]] to blend a low-order, non-oscillatory numerical flux with a high-order one.
It looks at the ratio of neighbouring slopes of the solution.
Where the solution is smooth it lets the high-order flux act, and near jumps or extrema it switches back to the low-order flux.
In this way the scheme is second-order accurate in smooth regions and still free of spurious oscillations.
This gets around the limits that [[Godunov's theorem|559N53ZTMV]] sets for linear schemes.
Standard examples are the minmod, superbee and van Leer limiters.

## Explanations

### L1 human

A careful but blurry method and a sharp but wiggly method can be mixed.
The flux limiter decides, at every grid point and every step, how much of the sharp method to use.
Where the solution is smooth, the ratio of consecutive slopes is close to $1$ and the sharp method is used in full.
Near a jump or a peak the ratio is far from $1$ or negative, and the limiter falls back to the careful method.
