---
tag: C2KM20J9DZ
kind: concept
name: Stabilizability
msc: [93D15, 93B05, 93C05]
sources:
  - url: https://en.wikipedia.org/wiki/Controllability
---

## Summary

A linear system $x' = Ax + Bu$ is stabilizable if some linear state [[feedback|7NYES2D0Z4]] $u = Kx$ makes the closed loop asymptotically stable.
It is weaker than [[controllability|A9WFM77Z4P]]: the input need not reach every mode, but every mode it cannot reach must already decay by itself.
Stabilizability is the natural hypothesis in many results of linear control, such as the existence of stabilizing solutions of Riccati equations in linear-quadratic control.
Its dual notion is [[detectability|PE9HCFHXB5]].

## Explanations

### L1 human

Some parts of a system may be out of reach of the controls.
That is harmless if those parts calm down on their own, like a swinging door that slowly stops.
A system is stabilizable when every part that the controls cannot touch is of this calm kind, so that feedback can stabilize the rest.
For example, $x_1' = -x_1$, $x_2' = x_2 + u$ is stabilizable: $x_1$ decays by itself, and $u = -2 x_2$ gives $x_2' = -x_2$.
