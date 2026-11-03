---
tag: FRYAQABP4P
kind: concept
name: Sliding mode control
msc: [93B12, 93C10, 93B52]
sources:
  - url: https://en.wikipedia.org/wiki/Sliding_mode_control
same_as:
  wikidata: Q6008560
  wikipedia: Sliding mode control
---

## Summary

Sliding mode control is a method of [[nonlinear control|RZ94FKGZ5Z]] that uses a feedback law which switches discontinuously across a chosen surface in the state space.
The switching drives the state onto the surface in finite time and then keeps it there.
The state then slides along the surface toward the goal.
On the surface the motion obeys a reduced equation chosen by the designer.
It is insensitive to bounded disturbances that enter through the same channel as the input, provided the switching gain exceeds their bound.
Solutions of the discontinuous closed loop are understood in the sense of Filippov, through a [[differential inclusion|9ZSMF6NYKM]].

## Explanations

### L1 human

Imagine steering a car toward a line painted on the road and then along it.
Whenever the car is left of the line, steer right as hard as allowed; whenever it is right of the line, steer left.
The car reaches the line quickly and then zig-zags along it with very small swings.
In the ideal limit it moves exactly along the line, whatever small bumps the road has.
