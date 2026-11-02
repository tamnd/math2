---
tag: SNFYTC1TTA
kind: concept
name: Volterra equation of convolution type
msc: [45D05, "45E10"]
specializes: [DND8CBEVXT]
sources:
  - url: https://en.wikipedia.org/wiki/Volterra_integral_equation
---

## Summary

A Volterra equation of convolution type is a [[Volterra integral equation|DND8CBEVXT]] whose kernel depends only on the difference $t - s$.
Its integral term is the convolution $\int_0^t k(t - s) \, x(s) \, ds$ on the half-line.
Such equations describe systems whose rules do not change in time, and the [[Laplace transform|0V49JEZW06]] turns them into algebraic equations.
Renewal equations, Abel's equation and many models with memory are of this type.

## Explanations

### L1 human

The weight given to a past value $x(s)$ depends only on how long ago it was, the lag $t - s$, and not on the date $s$ itself.
This is the integral version of a linear differential equation with constant coefficients.
For example, $x(t) = 1 + \int_0^t e^{-(t - s)} x(s) \, ds$ has memory that fades exponentially with the lag.
Its solution is $x(t) = 1 + t$, as one can check by computing the integral.
