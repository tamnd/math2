---
tag: ATPSAHYG7C
kind: concept
name: Volterra equation of the second kind
msc: [45D05]
specializes: [DND8CBEVXT, 8KJCN49V64]
sources:
  - url: https://en.wikipedia.org/wiki/Volterra_integral_equation
---

## Summary

A Volterra equation of the second kind is an equation $x(t) = f(t) + \lambda \int_a^t K(t, s) \, x(s) \, ds$, in which the unknown appears both outside and inside the integral.
It is the [[Volterra integral equation|DND8CBEVXT]] case of an [[integral equation of the second kind|8KJCN49V64]].
Unlike the Fredholm case, it has exactly one continuous solution for every value of $\lambda$ when the kernel and the function $f$ are continuous.
Initial value problems for linear ordinary differential equations lead to equations of this kind.

## Explanations

### L1 human

The value of the unknown at time $t$ is a known input plus a weighted memory of its own past values.
So one can compute the solution forward in time, starting from $x(a) = f(a)$.
For example, $x(t) = 1 + \int_0^t x(s) \, ds$ means $x' = x$ with $x(0) = 1$, so $x(t) = e^t$.
Because only the past enters, there is no resonance, and the equation can always be solved.
