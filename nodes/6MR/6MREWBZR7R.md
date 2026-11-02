---
tag: 6MREWBZR7R
kind: concept
name: Adaptive step size
msc: [65L50, 65L05, 65L06]
sources:
  - url: https://en.wikipedia.org/wiki/Adaptive_step_size
same_as:
  wikidata: Q4680766
  wikipedia: Adaptive step size
---

## Summary

Adaptive step size control lets a [[numerical method for an ordinary differential equation|558XADG64M]] change its step length as it goes.
At each step the method estimates its [[local truncation error|T220HF0562]] and compares it with a tolerance given by the user.
Steps whose error estimate is too large are rejected and repeated with a smaller step.
The next step size is predicted from the current estimate.
In this way the method takes long steps where the solution is smooth and short steps where it changes fast.
It reaches a target accuracy with far fewer steps than a fixed step size.

## Explanations

### L1 human

Think of driving a car along a winding road: on straight parts you go fast, and before sharp bends you slow down.
An adaptive solver does the same with its time step.
For an orbit of a comet, it takes tiny steps when the comet sweeps close to the sun and very large steps far away, where little happens.
The error estimate plays the role of the driver's eyes.
