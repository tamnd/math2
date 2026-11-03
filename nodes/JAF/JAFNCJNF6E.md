---
tag: JAFNCJNF6E
kind: concept
name: Ray parameter
msc: [86A15, 74J05]
sources:
  - url: https://en.wikipedia.org/wiki/Seismic_wave
---

## Summary

The ray parameter $p$ of a seismic ray is its horizontal slowness: the sine of its angle from the vertical divided by the wave speed.
In a layered or spherically symmetric Earth it stays the same along the whole ray, so it labels the ray.
It equals the slope of the travel-time curve at the distance where the ray emerges.
It is the basic variable in computing travel times and in the $\tau$-$p$ method.

## Explanations

### L1 human

Think of a wavefront crossing the surface: the ray parameter is how many seconds the wavefront needs to sweep one kilometre along the ground.
A wave coming straight up hits all points at once, so $p = 0$.
A wave travelling horizontally at speed $v$ has $p = 1/v$.
Since $p$ never changes along a ray in a layered Earth, a ray turns back up exactly at the depth where the speed reaches $1/p$.
