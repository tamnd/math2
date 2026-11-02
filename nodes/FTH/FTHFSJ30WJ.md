---
tag: FTHFSJ30WJ
kind: concept
name: Abscissa of convergence
msc: [44A10]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Summary

The abscissa of convergence of a [[Laplace transform|0V49JEZW06]] is a number $\sigma_c$ in $[-\infty, +\infty]$.
The Laplace integral converges on the half-plane $\operatorname{Re} s > \sigma_c$ and diverges on the half-plane $\operatorname{Re} s < \sigma_c$.
It plays the role that the radius of convergence plays for a power series.
The same notion exists for [[Dirichlet series|8MWTEF6462]], which are Laplace–Stieltjes transforms of step functions.
On the boundary line $\operatorname{Re} s = \sigma_c$ the integral may converge at some points and diverge at others.

## Explanations

### L1 human

The Laplace integral $\int_0^\infty f(t) e^{-st}\, dt$ converges better when $\operatorname{Re} s$ is larger, because $e^{-st}$ then decays faster.
So the set of $s$ where it converges is a right half-plane, possibly the whole plane or empty.
The abscissa of convergence is the real part of its left edge.
For $f(t) = e^{3t}$ the integral converges exactly when $\operatorname{Re} s > 3$, so the abscissa is $3$.
