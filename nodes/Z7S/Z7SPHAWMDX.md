---
tag: Z7SPHAWMDX
kind: concept
name: Nyquist plot
msc: [93C80, 93D10]
sources:
  - url: https://en.wikipedia.org/wiki/Nyquist_stability_criterion
---

## Summary

The Nyquist plot of a linear system is a curve in the [[complex plane|0CTE7A31XQ]].
It is traced by the [[frequency response|BMY8QZSD9H]] $G(i\omega)$ as $\omega$ runs over the real line.
Gain and phase are shown together: the gain is the distance from the origin and the phase is the angle.
Its main use is the [[Nyquist stability criterion|EZ1HMS875F]].
This criterion decides the stability of a feedback loop by counting how often the plot of the loop transfer function winds around $-1$.

## Explanations

### L1 human

Imagine a point in the plane that moves as the frequency of a test sine wave grows.
Its distance from the origin is how much the system amplifies the wave, and its angle is the phase shift.
The path of this point is the Nyquist plot.
For $G(s) = 1/(s + 1)$ the path is the circle with centre $1/2$ and radius $1/2$, run from $0$ through $1$ and back to $0$.
