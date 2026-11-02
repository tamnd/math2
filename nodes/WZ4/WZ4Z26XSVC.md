---
tag: WZ4Z26XSVC
kind: concept
name: Urysohn integral equation
msc: [45G10]
specializes: [BSCYBP6AS6]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
---

## Summary

A Urysohn integral equation is a nonlinear integral equation in which the unknown function enters the integrand through a general function of three variables: $\varphi(x) = f(x) + \int_\Omega K(x, t, \varphi(t))\, dt$.
It is the most general form of a [[nonlinear integral equation|BSCYBP6AS6]] of Fredholm type in one unknown.
It contains the Hammerstein equation as a special case.
Existence results for it usually come from fixed point theorems, such as the [[Schauder fixed-point theorem|DCPFVVZZ54]], applied to the operator on the right side.
The name is also written Uryson.

## Explanations

### L1 human

In a linear integral equation the unknown is multiplied by a kernel and then integrated.
In a Urysohn equation the kernel may depend on the unknown in any way, for example through $\sin(x\, \varphi(t))$.
The equation still says that the unknown at a point is a weighted total of its values elsewhere.
For instance, $\varphi(x) = x$ solves $\varphi(x) = x + \int_0^1 \sin\bigl(x(\varphi(t) - t)\bigr)\, dt$, since the sine is then $0$.
