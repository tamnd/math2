---
tag: 7DBPJKYC6C
kind: concept
name: Runge–Kutta methods
msc: [65L06, 65L05]
sources:
  - url: https://en.wikipedia.org/wiki/Runge–Kutta_methods
same_as:
  wikidata: Q725944
  wikipedia: Runge–Kutta methods
---

## Summary

Runge–Kutta methods are one-step methods for the numerical solution of an [[initial value problem|0FXDW992DS]] $y' = f(t, y)$, $y(t_0) = y_0$.
Each step evaluates $f$ at several intermediate points, the stages, and combines these slopes to advance the solution.
They reach high order without derivatives of $f$, and they include the [[Euler method|0JARTXX4XP]], the classical fourth-order method, and implicit methods for [[stiff equations|RR5FCG92PN]].
A method is described by its coefficients, collected in a [[Butcher tableau|RH8BD7PW5F]].

## Explanations

### L1 human

The Euler method follows the slope at the start of each step, which is crude.
A Runge–Kutta method first probes the slope at a few points inside the step and then takes a weighted average of them.
This is like checking the road ahead before deciding how to steer.
The classical fourth-order method uses four slopes per step; halving the step size makes its error about sixteen times smaller.
