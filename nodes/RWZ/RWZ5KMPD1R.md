---
tag: RWZ5KMPD1R
kind: concept
name: Random ordinary differential equation
msc: [34F05, 37H10]
sources:
  - url: https://en.wikipedia.org/wiki/Random_dynamical_system
---

## Summary

A random ordinary differential equation is an [[ordinary differential equation|0NT64JV96A]] whose right side depends on a [[stochastic process|0QH5ENKZM1]] with regular sample paths.
For each fixed outcome of the randomness it is an ordinary, non-autonomous differential equation, and it is solved path by path with classical calculus.
Such equations generate random dynamical systems, and many [[stochastic differential equations|B219G9SHJA]] can be turned into them by a change of variables.

## Explanations

### L1 human

Think of a boat whose speed depends on a wind that changes in a random but smooth way.
Once the weather of a given day is known, the motion of the boat is an ordinary differential equation.
A random ordinary differential equation collects all these equations, one for each possible weather.
For example, $x' = -x + \eta_t$ with a random continuous signal $\eta$ has, for each path of $\eta$, the solution $x(t) = e^{-t} x(0) + \int_0^t e^{-(t - s)} \eta_s \, ds$.
