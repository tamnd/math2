---
tag: ZMCFEEPEKT
kind: concept
name: Functional differential equation
msc: [34K05]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_differential_equation
same_as:
  wikidata: Q28406324
  wikipedia: Functional differential equation
---

## Summary

A functional differential equation relates the derivative of an unknown function at time $t$ to its values at other times.
Often these times fill a whole past interval.
It includes [[ordinary differential equations|0NT64JV96A]], delay equations and equations with distributed memory.
The state at time $t$ is the piece of the solution on an interval $[t - r, t]$, so the phase space is a space of functions.
The theory, developed by Krasovskii, Hale and others, extends existence, uniqueness and stability theory to this setting.

## Explanations

### L1 human

In an ordinary differential equation, the future depends only on the present state.
In a functional differential equation, it may depend on the recent past as well.
For instance, $x'(t) = -\int_{t-1}^{t} x(s) \, ds$ lets the rate of change depend on the average of the last time unit.
To start such an equation, one needs the whole history over that time unit.
