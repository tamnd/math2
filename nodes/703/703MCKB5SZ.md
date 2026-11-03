---
tag: 703MCKB5SZ
kind: concept
name: Controllability Gramian
msc: [93B05, 93C05]
sources:
  - url: https://en.wikipedia.org/wiki/Controllability_Gramian
same_as:
  wikipedia: Controllability Gramian
---

## Summary

The controllability Gramian of a linear system $x' = Ax + Bu$ is a symmetric positive semidefinite matrix.
It is built from $A$ and $B$ by an integral of the [[matrix exponential|020M04FN1H]].
It is invertible exactly when the system is [[controllable|A9WFM77Z4P]], and its inverse gives the least energy needed to reach a state.
For a stable matrix $A$, the Gramian over infinite time solves a [[Lyapunov equation|92GVPZH9FT]].
It is used in the proof of the [[Kalman rank condition|9NSCZ2KBEB]], in the construction of steering controls and in model reduction.

## Explanations

### L1 human

The controllability Gramian measures how strongly the input can push the state in each direction.
Directions in which it is large are easy to reach, and directions in which it is small cost a lot of input energy.
Directions in which it is zero cannot be reached at all.
For the scalar system $x' = u$, the Gramian over time $T$ is the number $T$.
To move the state by $d$ in time $T$, the cheapest input is the constant $d/T$, with energy $d^2/T$, which is $d^2$ divided by the Gramian.
