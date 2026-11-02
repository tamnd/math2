---
tag: HGPH5QWVC2
kind: concept
name: Periodic solutions of integral equations
msc: [45M15, 45G10, 45D05]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
---

## Summary

A periodic solution of an [[integral equation|R3SG1SN7JQ]] is a solution defined on the whole real line that repeats after a fixed period $T > 0$.
One looks for such solutions when the data of the equation, its forcing term and its kernel, are themselves $T$-periodic in time.
Equations with infinite memory, where the integral runs over the whole past, are the natural setting.
Periodic solutions describe the steady oscillations of systems with memory under periodic forcing, much as [[periodic solutions|FHNDX22WMK]] do for differential equations.

## Explanations

### L1 human

Think of a system that is pushed by a force that repeats every day, and that remembers its own past.
After a long time one expects the system to settle into a daily rhythm.
That rhythm is a periodic solution of the integral equation that models the system.
For example, $x(t) = \sin t$ solves $x(t) = \frac{1}{2}(\sin t + \cos t) + \int_{-\infty}^t e^{-(t - s)} x(s) \, ds$, and it repeats after the time $2\pi$.
