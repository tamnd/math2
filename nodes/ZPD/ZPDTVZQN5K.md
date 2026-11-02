---
tag: ZPDTVZQN5K
kind: concept
name: Control system
msc: [93C15, 34H05, 93C10]
sources:
  - url: https://en.wikipedia.org/wiki/Control_theory
---

## Summary

A control system is a dynamical system whose evolution depends on an input that can be chosen, the control.
For systems governed by [[ordinary differential equations|0NT64JV96A]] it has the form $x' = f(x, u)$, where $x$ is the state and $u$ is the control.
It is the basic object of control theory.
That theory asks which states can be reached, how to steer the system, and how to do so in the best way.

## Explanations

### L1 human

A car is a control system: its position and speed are the state, and the driver chooses the pedals and the steering wheel.
The laws of motion say how the state changes for each choice of the inputs.
The driver wants to reach a goal, such as parking, by choosing the inputs well over time.
A simple mathematical example is $x_1' = x_2$, $x_2' = u$: a point on a line whose acceleration $u$ can be chosen.
