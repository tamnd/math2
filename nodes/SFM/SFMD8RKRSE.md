---
tag: SFMD8RKRSE
kind: concept
name: Relaxed control
msc: [49J15, 49J45, 93C15]
sources:
  - url: https://en.wikipedia.org/wiki/Optimal_control
---

## Summary

A relaxed control assigns to each time a probability measure on the set of control values, instead of a single control value.
The system then moves with the average of the velocities with respect to this measure.
Relaxed controls fill in the convex hulls of the velocity sets, so optimal control problems without a minimizer gain one in the relaxed sense.
They are the control theory counterpart of [[Young measures|6TQSVJQDEH]] and of the [[relaxation of a variational problem|DPS8QZBVB0]].

## Explanations

### L1 human

Suppose a car may only steer fully left or fully right, but you want it to drive straight.
By switching very fast between left and right, it moves almost straight.
A relaxed control describes the limit of such fast switching: at each moment it says "half left, half right".
In the limit the car goes straight, even though no ordinary control does that.
[[Filippov's existence theorem|XEX7QZV1BS]] needs convex velocity sets, and relaxed controls supply this convexity.
