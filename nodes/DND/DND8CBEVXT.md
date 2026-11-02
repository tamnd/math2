---
tag: DND8CBEVXT
kind: concept
name: Volterra integral equation
msc: [45D05]
sources:
  - url: https://en.wikipedia.org/wiki/Volterra_integral_equation
same_as:
  wikidata: Q2632613
  wikipedia: Volterra integral equation
---

## Summary

A Volterra integral equation is an integral equation in which the integral runs from a fixed point up to the variable $t$.
The typical form of the second kind is $x(t) = f(t) + \int_a^t K(t, s) x(s) \, ds$.
Every [[initial value problem|0FXDW992DS]] for an ordinary differential equation can be written as a Volterra equation of the second kind, in general a nonlinear one.
Under mild conditions, the linear equation of the second kind has a unique solution, given by a convergent series of iterated kernels.

## Explanations

### L1 human

In a Volterra equation, the value at time $t$ is built from a known part and a weighted sum over all earlier times.
So the solution depends only on the past, as in a process that unfolds in time.
The equation $x(t) = 1 + \int_0^t x(s) \, ds$ is the integral form of $x' = x$, $x(0) = 1$.
Its solution is $x(t) = e^t$.
