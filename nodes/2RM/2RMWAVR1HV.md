---
tag: 2RMWAVR1HV
kind: concept
name: Fredholm equation of the first kind
msc: [45B05, 45A05]
specializes: [526TCVMSHP, ZDS77Q0F06]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_integral_equation
---

## Summary

A Fredholm equation of the first kind is an integral equation $\int_a^b K(x, y) \varphi(y) \, dy = f(x)$ with fixed limits $a$ and $b$.
The unknown function $\varphi$ appears only under the integral sign.
It is the [[Fredholm integral equation|526TCVMSHP]] form of an [[integral equation of the first kind|ZDS77Q0F06]].
Such equations model the recovery of a cause from a smoothed measurement, as in deblurring and tomography.
They are usually ill-posed: a solution may fail to exist, and small changes of $f$ can cause large changes of $\varphi$.

## Explanations

### L1 human

Think of $f$ as a blurred photograph and of $\varphi$ as the sharp picture that produced it.
The kernel $K(x, y)$ says how much the point $y$ of the sharp picture contributes to the point $x$ of the blurred one.
Solving the equation means undoing the blur, and blurring destroys fine detail, so this is hard.
For example, with $K(x, y) = 1$ on $[0, 1]$, the equation reads $\int_0^1 \varphi(y) \, dy = f(x)$.
It has a solution only when $f$ is constant, and then it has infinitely many.
