---
tag: 5126SDXYHF
kind: concept
name: Volterra integro-differential equation
msc: [45J05, 45D05]
specializes: [YRKW2KX2CW]
sources:
  - url: https://en.wikipedia.org/wiki/Integro-differential_equation
---

## Summary

A Volterra integro-differential equation is an [[integro-differential equation|YRKW2KX2CW]] in which the integral runs only over the past.
The integral goes from a fixed initial time up to the current time.
So the rate of change at time $t$ depends on the present state and on the history up to $t$, not on the future.
Together with an initial condition it is equivalent to a [[Volterra integral equation|DND8CBEVXT]], and under Lipschitz conditions it has a unique solution.
Such equations model materials with memory, such as viscoelastic bodies, and populations whose growth depends on past sizes.

## Explanations

### L1 human

Imagine a spring made of a material that remembers how it was stretched before.
Its force now depends on its current stretch and on a weighted sum of all past stretches.
Newton's law then gives an equation with both a derivative and an integral over the past: a Volterra integro-differential equation.
A small example is $x'(t) = \int_0^t x(s) \, ds$ with $x(0) = 1$, whose solution is $x(t) = \cosh t$.
