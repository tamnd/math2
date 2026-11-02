---
tag: 39PCDRDB01
kind: concept
name: Delay differential equation
msc: [34K06, 34K05]
specializes: [ZMCFEEPEKT]
sources:
  - url: https://en.wikipedia.org/wiki/Delay_differential_equation
same_as:
  wikidata: Q2146125
  wikipedia: Delay differential equation
---

## Summary

In a delay differential equation, the rate of change at time $t$ depends on the state at earlier times, such as $t - \tau$.
To solve it, one must give the whole history of the solution on an initial interval, not just one initial value.
So the natural state space is a space of functions, and the equation is infinite-dimensional even for one unknown.
Delay equations model systems with reaction times, such as feedback control, population dynamics and epidemics.

## Explanations

### L1 human

A shower whose temperature responds to the tap only after a few seconds is a classic picture of delay.
You react to the water you feel now, which reflects the tap setting of a moment ago, and so you tend to overshoot.
The equation $x'(t) = -x(t - 1)$ says that the state decreases at a rate given by its value one time unit earlier.
Unlike $x' = -x$, which only decays, this equation has oscillating solutions.
