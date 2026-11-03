---
tag: JSSYGY0V87
kind: concept
name: Relaxation modulus
msc: [74D05]
sources:
  - url: https://en.wikipedia.org/wiki/Stress_relaxation
---

## Summary

The relaxation modulus $G(t)$ of a linear [[viscoelastic|GCX1B3DAJN]] material is its stress at time $t$ after a unit strain step at time $0$.
It typically decays in time, from an instantaneous modulus $G(0^+)$ to an equilibrium modulus $G(\infty)$, which is zero for a fluid-like material.
By the [[Boltzmann superposition principle|KJ6AAHKJ91]], this one function determines the response to every strain history.
Its companion is the creep compliance $J(t)$, the strain produced by a unit stress step.

## Explanations

### L1 human

Stretch a rubber band by a fixed amount and hold it still.
The force it pulls back with is largest at first and then slowly fades.
Divide that force by the stretch and follow it in time: this curve is the relaxation modulus.
For a [[Maxwell material|PQ8Z5HS2JR]] it is a decaying exponential $E e^{-t/\tau}$.
