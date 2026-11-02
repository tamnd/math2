---
tag: HYA7QQ1E38
kind: concept
name: Strip of convergence of the bilateral transform
msc: [44A10]
sources:
  - url: https://en.wikipedia.org/wiki/Two-sided_Laplace_transform
---

## Summary

The strip of convergence of a [[two-sided Laplace transform|6J2AGD0BYY]] is the vertical strip $\alpha < \operatorname{Re} s < \beta$ in the complex plane where the defining integral converges absolutely.
The left edge $\alpha$ is set by the growth of $f$ as $t \to +\infty$, and the right edge $\beta$ by its growth as $t \to -\infty$.
Inside the strip the transform is holomorphic.
The strip must be given along with the formula, since one formula can be the transform of different functions on different strips.

## Explanations

### L1 human

The two-sided transform needs $f(t) e^{-s t}$ to be small at both ends of the time axis.
A large $\operatorname{Re} s$ helps for positive times and hurts for negative times, so only a band of values of $\operatorname{Re} s$ works.
For $e^{-\abs{t}}$ the band is $-1 < \operatorname{Re} s < 1$.
The formula $1/(1 - s)$ is the transform of $e^{t}$ for $t < 0$ (and $0$ for $t > 0$) on $\operatorname{Re} s < 1$, but of $-e^{t}$ for $t > 0$ (and $0$ for $t < 0$) on $\operatorname{Re} s > 1$.
