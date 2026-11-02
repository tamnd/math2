---
tag: 7WFKPAMQFG
kind: concept
name: Mixed-type equation
msc: [35M10]
specializes: [GC5BDZ6QBC]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%E2%80%93Tricomi_equation
---

## Summary

A mixed-type equation is a partial differential equation that is elliptic in one part of its domain and hyperbolic in another part.
The two regions are separated by a set where the equation degenerates, often a parabolic line.
The basic example is the [[Tricomi equation|21DD2334NR]].
Such equations arise in the study of transonic flow, where the speed of a gas crosses the speed of sound.
See the [[definition|GKFDKRHEP4]].

## Explanations

### L1 human

The type of a second-order equation can change from point to point when its coefficients vary.
In the Tricomi equation $u_{yy} + y \, u_{xx} = 0$, the upper half plane $y > 0$ is elliptic and the lower half plane $y < 0$ is hyperbolic.
So in one region the equation behaves like the Laplace equation and in the other like the wave equation.
For gas flow past an airplane wing, the flow is slower than sound in one region and faster in another, and this is the physical origin of such equations.
