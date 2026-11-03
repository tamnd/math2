---
tag: YWAC5TXSRY
kind: concept
name: Output controllability
msc: [93B05, 93C05]
sources:
  - url: https://en.wikipedia.org/wiki/Controllability
    locator: Output controllability
---

## Summary

A system with an output is output controllable if its output can be driven to any prescribed value by a suitable input.
It asks less than [[controllability|A9WFM77Z4P]] of the state: only the measured or regulated quantities must be steerable, not every internal variable.
For linear systems it is decided by a rank test of the same type as the [[Kalman rank condition|9NSCZ2KBEB]].

## Explanations

### L1 human

Think of a room with two heaters and one thermometer.
The internal state is the temperature at many places, but we only care about the reading of the thermometer.
The system is output controllable if, by running the heaters suitably, we can make the thermometer show any value we like at some moment.
A simple case is the double integrator $x_1' = x_2$, $x_2' = u$ with output $y = x_1$: the position $y$ can be moved to any value.
It does not matter whether the full state could be steered as well.
