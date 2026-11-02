---
tag: 8M012XRPZM
kind: concept
name: Stability of Volterra equations
msc: [45M10, 45D05, "45E10"]
sources:
  - url: https://en.wikipedia.org/wiki/Volterra_integral_equation
---

## Summary

Stability of a [[Volterra integral equation|DND8CBEVXT]] concerns the behaviour of its solutions on the whole half-line $t \ge 0$.
For a linear equation of convolution type it asks whether bounded or integrable data always give bounded or integrable solutions.
This holds when the resolvent kernel of the equation is integrable, which is the standard notion of stability for such equations.
Stability results are used for models with memory, such as viscoelastic materials, feedback systems with delay and population dynamics.

## Explanations

### L1 human

In a Volterra equation the present value of the unknown depends on its whole past through a kernel.
Such a memory can damp disturbances or amplify them.
The equation is stable when every bounded input produces a bounded output, so that small causes have small effects for all time.
For example, $x(t) + \int_0^t a e^{-(t - s)} x(s) \, ds = f(t)$ is stable exactly when the real part of $a$ is larger than $-1$.
For $a = -1$ and $f = 1$ the solution is $x(t) = 1 + t$, which grows without bound.
