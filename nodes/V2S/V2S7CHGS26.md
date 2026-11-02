---
tag: V2S7CHGS26
kind: concept
name: Tight frame
msc: [42C15]
sources:
  - url: https://en.wikipedia.org/wiki/Frame_(linear_algebra)
---

## Summary

A frame of a [[Hilbert space|HM2HHE3J51]] is a family of vectors that recovers every vector stably from its inner products with the family.
Unlike a basis, a frame may be redundant.
A tight frame is a frame whose lower and upper frame bounds are equal.
Then reconstruction is as simple as for an [[orthonormal basis|0S9GGTR0EX]], up to a constant factor.
Tight frames are used in signal processing, coding and quantum information, where redundancy gives robustness.

## Explanations

### L1 human

In the plane, take three unit vectors at angles of $120^\circ$ to each other, like the Mercedes-Benz star.
They are not a basis, since there are three of them in a two-dimensional space.
Still, for every vector $f$ the sum of the squares of its three components along them is exactly $\tfrac32 \norm{f}^2$.
This is the defining property of a tight frame: the energy of $f$ is spread evenly over the frame, whatever direction $f$ has.
