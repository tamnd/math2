---
tag: QVRP8FSAZM
kind: concept
name: Hypersingular integral equation
msc: ["45E99", "45E05"]
specializes: [R3SG1SN7JQ]
sources:
  - url: https://en.wikipedia.org/wiki/Hadamard_regularization
---

## Summary

A hypersingular integral equation is an integral equation with a very singular kernel.
Its integral exists neither as an ordinary integral nor as a [[Cauchy principal value|0SYR10HD4R]].
The typical kernel on an interval is $1/(t - x)^2$, and the integral is read as a [[Hadamard finite part|G7VE41JHHH]].
Such equations arise in crack problems of elasticity and in the scattering of waves by thin screens.
They also arise in boundary element methods that use the normal derivative of a double layer potential.

## Explanations

### L1 human

In a Cauchy singular equation the kernel behaves like $1/(t - x)$, and the two sides of the singularity cancel.
In a hypersingular equation the kernel behaves like $1/(t - x)^2$, which is positive on both sides, so nothing cancels.
One gives the integral a meaning by removing its divergent part.
A useful picture: the hypersingular operator is the derivative of a Cauchy singular operator.
For example, the finite part of $\frac{1}{\pi}\int_{-1}^{1} \frac{\sqrt{1 - t^2}}{(t - x)^2}\, dt$ equals $-1$ for every $x$ in $(-1, 1)$.
