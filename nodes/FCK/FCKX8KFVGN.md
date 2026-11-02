---
tag: FCKX8KFVGN
kind: concept
name: Convolution on the half-line
msc: [44A35, 44A40]
specializes: [ERP5737VZ1]
sources:
  - url: https://en.wikipedia.org/wiki/Convolution
---

## Summary

The convolution on the half-line combines two functions $f, g$ on $[0, \infty)$ into $(f * g)(t) = \int_0^t f(\tau) g(t - \tau) \, d\tau$.
It is the [[convolution on the line|ERP5737VZ1]] of the two functions extended by zero to negative times.
The [[Laplace transform|0V49JEZW06]] turns it into a pointwise product.
It is also the product of the [[Mikusiński operational calculus|TD5XK5AHNV]].

## Explanations

### L1 human

Think of $t$ as time and of $f$ and $g$ as signals that start at time $0$.
The value $(f * g)(t)$ adds up the effects at time $t$ of all the inputs $f(\tau)$ from earlier times $\tau$, each weighted by $g$ at the elapsed time $t - \tau$.
Only the past matters, so the integral runs from $0$ to $t$.
For example, convolving the constant $1$ with itself gives $\int_0^t 1 \, d\tau = t$.
