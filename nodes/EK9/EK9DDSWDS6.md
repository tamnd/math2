---
tag: EK9DDSWDS6
kind: concept
name: System identification
msc: [93B30, "93E12"]
sources:
  - url: https://en.wikipedia.org/wiki/System_identification
same_as:
  wikidata: Q1366192
  wikipedia: System identification
---

## Summary

System identification is the construction of mathematical models of dynamical systems from measured input and output data.
One fixes a class of models with unknown parameters and records how the real system responds to chosen inputs.
Then one picks the parameters that best explain the data.
Most models used in control and signal processing are obtained in this way.
It raises statistical questions of consistency, bias and the design of informative experiments.

## Explanations

### L1 human

Suppose you want a model of how a room warms up when a heater is switched on.
You switch the heater on and off, record the temperature, and look for the equation in a chosen family that best reproduces the record.
For a family $y(t) = a\, y(t-1) + b\, u(t-1)$, this means finding the two numbers $a$ and $b$, typically by least squares.
The quality of the result depends on the data: if the heater is never switched on, nothing can be learned about $b$.
