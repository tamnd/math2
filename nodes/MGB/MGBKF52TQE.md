---
tag: MGBKF52TQE
kind: concept
name: Cauchy-type integral
msc: ["30E20", "45E05"]
sources:
  - url: https://en.wikipedia.org/wiki/Sokhotski%E2%80%93Plemelj_theorem
---

## Summary

A Cauchy-type integral is a function $\Phi(z) = \frac{1}{2\pi i} \int_\Gamma \frac{\varphi(\tau)}{\tau - z} \, d\tau$ built from a curve $\Gamma$ and a function $\varphi$ on it.
It has the form of [[Cauchy's integral formula|0DG10TVYPN]], but $\varphi$ is arbitrary and need not be the boundary value of a holomorphic function.
It is a [[holomorphic function|0NAHXR1FRH]] off $\Gamma$, and in general it jumps across $\Gamma$ by exactly $\varphi$.
This makes it the basic tool for boundary value problems of Riemann–Hilbert type and for singular integral equations.

## Explanations

### L1 human

Cauchy's formula recovers a holomorphic function inside a curve from its values on the curve.
A Cauchy-type integral uses the same formula with any function $\varphi$ on the curve.
The result is still holomorphic on both sides of the curve, but the inside and outside functions need not fit together.
The amount by which they differ across the curve is $\varphi$ itself.
For example, on the unit circle with $\varphi(\tau) = \tau + \tau^{-1}$, the integral equals $z$ inside and $-1/z$ outside, and the difference at $\tau$ on the circle is $\tau + \tau^{-1}$.
