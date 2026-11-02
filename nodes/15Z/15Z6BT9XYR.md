---
tag: 15Z6BT9XYR
kind: concept
name: Model predictive control
msc: [93B45, 49N35, 93C55]
sources:
  - url: https://en.wikipedia.org/wiki/Model_predictive_control
same_as:
  wikidata: Q1782962
  wikipedia: Model predictive control
---

## Summary

Model predictive control is a feedback strategy that solves a finite-horizon [[optimal control|T3V6ZNAMDN]] problem at every sampling time.
From the measured state it predicts the future with a model and optimises the controls over a horizon of $N$ steps subject to constraints.
It applies only the first control and repeats at the next step.
This receding-horizon principle turns open-loop optimisation into a closed-loop controller that handles constraints on states and inputs directly.
It is standard in process industry, power electronics and autonomous driving.

## Explanations

### L1 human

A driver looks a little way down the road, plans the next few seconds, starts doing the first part of the plan, and then plans again with fresh information.
Model predictive control does the same with a mathematical model of the system and an optimiser.
Because it replans all the time, it corrects for disturbances and model errors.
Constraints such as a maximum speed or a limited motor force simply enter the optimisation problem.
The short horizon must be handled with care: if the plan ignores what happens after the horizon, the closed loop may fail to settle.
