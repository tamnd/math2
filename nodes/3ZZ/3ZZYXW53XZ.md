---
tag: 3ZZYXW53XZ
kind: concept
name: Model reference adaptive control
msc: [93C40, 93D21, 93B52]
specializes: [F2RD2ZTZ8V]
sources:
  - url: https://en.wikipedia.org/wiki/Adaptive_control
---

## Summary

Model reference adaptive control is a form of [[adaptive control|F2RD2ZTZ8V]].
The desired behaviour of the closed loop is given by a stable reference model.
The controller parameters are adjusted online so that the output of the plant follows the output of the reference model.
It is one of the oldest and most studied adaptive schemes, and its modern versions come with Lyapunov proofs of stability.

## Explanations

### L1 human

You write down a simple model that behaves exactly as you would like the real system to behave, for example a smooth first-order response.
Both the model and the real plant receive the same command.
The difference between their outputs is the tracking error.
The controller keeps changing its gains in the direction that shrinks this error.
When the gains reach the right values, the plant with its controller behaves like the model.
