---
tag: F2RD2ZTZ8V
kind: concept
name: Adaptive control
msc: [93C40, 93D21, "93E35"]
sources:
  - url: https://en.wikipedia.org/wiki/Adaptive_control
same_as:
  wikidata: Q235781
  wikipedia: Adaptive control
---

## Summary

Adaptive control is the design of controllers that adjust their own parameters while they run.
It copes with a plant whose parameters are unknown or change slowly.
An adaptive controller combines a [[feedback|7NYES2D0Z4]] law with an adaptation law that updates the parameters from measured signals.
The closed loop is nonlinear and time-varying even when the plant is linear, so its stability is usually proved with a [[Lyapunov function|01REYCJ371]].
Classic forms are [[model reference adaptive control|3ZZYXW53XZ]] and self-tuning regulators.

## Explanations

### L1 human

A fixed controller is tuned once for one plant, and it may work badly if the plant differs from the model.
An adaptive controller keeps learning: it watches how the plant responds and keeps changing its own settings.
An autopilot that adapts as an aircraft burns fuel and becomes lighter is a typical picture.
For example, for the plant $x' = a x + u$ with unknown $a$, the rule $u = -\hat{k} x$ with $\hat{k}' = x^2$ raises the gain as long as $x$ is not zero.
The gain grows until it beats the unknown $a$, and then $x$ goes to $0$.
