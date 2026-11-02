---
tag: J0JY4AG3E6
kind: concept
name: Method of steps
msc: [34K05, 34K06]
sources:
  - url: https://en.wikipedia.org/wiki/Delay_differential_equation
---

## Summary

The method of steps solves a [[delay differential equation|39PCDRDB01]] with a constant delay one interval at a time.
On each interval of the length of the delay, the delayed term is already known, so the equation becomes an [[ordinary differential equation|0NT64JV96A]].
It proves existence and uniqueness of solutions forward in time, and it gives explicit solutions in simple cases.

## Explanations

### L1 human

If the delay is one second, then during the first second the delayed values are just the given history.
So one can solve an ordinary equation for the first second.
Then this answer becomes the history for the next second, and so on.
For $x'(t) = -x(t - 1)$ with $x = 1$ before time $0$, the first step gives $x(t) = 1 - t$ on $[0, 1]$.
The second step gives $x(t) = (t - 1)(t - 3)/2$ on $[1, 2]$.
