---
tag: G8J0YQRPA3
kind: concept
name: Energy method
msc: [35L05, 35B45, 35A02]
sources:
  - url: https://en.wikipedia.org/wiki/Well-posed_problem
---

## Summary

The energy method is a way to prove uniqueness, stability and a priori bounds for solutions of partial differential equations.
One attaches to a solution a nonnegative quantity, often a physical energy, and shows from the equation that it cannot grow too fast.
For evolution equations this gives control of the solution at time $t$ by its data at time $0$, which is the core of [[well-posedness|W09B9NZ9B5]].
It works for many [[hyperbolic|92C3S03AQZ]] and [[parabolic|1CCTH8X2FT]] equations where no explicit formula is available.

## Explanations

### L1 human

A vibrating string without friction keeps its total energy, kinetic plus elastic.
If two motions start from the same position and velocity, their difference starts with zero energy, and so it keeps zero energy forever, so the two motions agree.
The energy method turns this physical idea into a proof.
One multiplies the equation by a well-chosen quantity, such as $u_t$, integrates over space, and integrates by parts to find how the energy changes in time.
