---
tag: NSVEH6VMX8
kind: concept
name: Equicontinuous system
msc: [37B05, 37B02]
sources:
  - url: https://en.wikipedia.org/wiki/Equicontinuity
---

## Summary

An equicontinuous system is a topological dynamical system whose family of iterates $\set{f^n : n \ge 0}$ is [[equicontinuous|0XN66MZN0Y]].
Then points that start close stay close for all future times, uniformly in time.
Isometries are the typical examples, such as rotations of the circle or translations on a compact group.
Equicontinuity is the opposite of sensitive dependence on initial conditions, so equicontinuous systems are the most orderly ones in [[topological dynamics|5X6E97EMFR]].

## Explanations

### L1 human

In an equicontinuous system, if two starting points are close enough, their orbits remain close forever, and the needed closeness does not depend on how long one waits.
Rotating a circle is the model: it keeps all distances exactly.
The doubling map $x \mapsto 2x \bmod 1$ is not equicontinuous: two points at distance $\delta$ move to distance $2\delta$, then $4\delta$, until they are far apart.
