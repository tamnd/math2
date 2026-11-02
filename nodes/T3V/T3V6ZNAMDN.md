---
tag: T3V6ZNAMDN
kind: concept
name: Optimal control
msc: [49J15, 49K15, 93C15]
sources:
  - url: https://en.wikipedia.org/wiki/Optimal_control
same_as:
  wikidata: Q1971426
  wikipedia: Optimal control
---

## Summary

Optimal control is the theory of choosing the input of a [[control system|ZPDTVZQN5K]] in the best way.
The aim is to make a cost, which depends on the input and on the resulting trajectory, as small as possible.
An optimal control is an [[admissible control|8M31QKB0GW]] whose cost is not larger than that of any other admissible control.
The theory extends the calculus of variations to problems with constraints on the controls.
Its main tools are [[Pontryagin's maximum principle|7RPV2T29CF]], which gives necessary conditions, and dynamic programming with the [[Hamilton–Jacobi–Bellman equation|SJP9HW82VX]].
The [[definition|EZ8NBZ8D0E]] states the problem in Bolza form.

## Explanations

### L1 human

A driver wants to reach a destination using as little fuel as possible, and the car obeys the laws of motion.
At each moment the driver chooses the pedal position, and these choices together decide the path and the fuel used.
Optimal control finds the best way to make all these choices.
A simple case: a point on a line moves with speed $u(t)$, where $\abs{u} \le 1$, and should be as far right as possible at time $1$.
The best choice is full speed, $u = 1$, all the time, since the final position is the integral of the speed and the speed is at most $1$.
