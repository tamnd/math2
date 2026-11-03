---
tag: QJ59HPYQ9D
kind: concept
name: Moving horizon estimation
msc: ["93E10", 93B45, 93C55]
sources:
  - url: https://en.wikipedia.org/wiki/Moving_horizon_estimation
same_as:
  wikidata: Q6927137
  wikipedia: Moving horizon estimation
---

## Summary

Moving horizon estimation is a method to estimate the state of a dynamical system.
At each time step, it solves an optimization problem over a window of the most recent measurements.
It is the estimation counterpart of [[model predictive control|15Z6BT9XYR]].
It handles nonlinear models and constraints on states and disturbances.
A [[Kalman filter|DFM9YXF9AG]] cannot do this directly.

## Explanations

### L1 human

Think of a window that slides along the time axis and always shows the last $N$ measurements.
At each step you look through the window and ask which state trajectory, consistent with the model, best explains what you see.
You keep the endpoint of that trajectory as your current estimate, then slide the window by one step and repeat.
Older data are not thrown away completely: they are summarized by a penalty on the first state of the window, the arrival cost.
For example, a tank level that can never be negative can be estimated with the constraint "level at least $0$" built into the optimization.
