---
tag: H6ZGEDM4VV
kind: concept
name: Volterra equation of the first kind
msc: [45D05]
specializes: [DND8CBEVXT, ZDS77Q0F06]
sources:
  - url: https://en.wikipedia.org/wiki/Volterra_integral_equation
---

## Summary

A Volterra equation of the first kind is an equation $f(t) = \int_a^t K(t, s) \, x(s) \, ds$ in which the unknown function $x$ appears only under the integral.
It is the [[Volterra integral equation|DND8CBEVXT]] analogue of an [[integral equation of the first kind|ZDS77Q0F06]].
Solving it is like inverting an integration, so it behaves like differentiation and is in general ill-posed.
When the kernel is smooth and does not vanish on the diagonal, it can be reduced to an equation of the second kind.

## Explanations

### L1 human

The data $f(t)$ is an accumulated quantity: a weighted total of the unknown $x$ over all past times $s \le t$.
The task is to recover the rate $x$ from the totals.
With $K = 1$ and $a = 0$, the equation $f(t) = \int_0^t x(s) \, ds$ has the solution $x = f'$, provided $f$ is differentiable and $f(0) = 0$.
For instance, $f(t) = t^2$ gives $x(t) = 2t$.
A small wiggle in $f$ can produce a large change in $f'$, which is why such equations are delicate.
