---
tag: YCSH2WK69M
kind: concept
name: Abscissa of absolute convergence
msc: [44A10]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Summary

The abscissa of absolute convergence $\sigma_a$ of a [[Laplace transform|0V49JEZW06]] marks the left edge of the half-plane where $\int_0^\infty \abs{f(t)} e^{-\operatorname{Re}(s) t}\, dt$ is finite.
It is never smaller than the [[abscissa of convergence|FTHFSJ30WJ]] $\sigma_c$.
In the half-plane of absolute convergence the transform can be handled with the standard theorems of Lebesgue integration, such as dominated convergence and Fubini's theorem.
The strip $\sigma_c < \operatorname{Re} s < \sigma_a$, where the integral converges only conditionally, can be nonempty.

## Explanations

### L1 human

Convergence of an integral can come from two sources: the size of the integrand gets small, or positive and negative parts cancel.
Absolute convergence uses only the size.
The abscissa of absolute convergence tells where size alone is enough.
For $f(t) = e^{t} \sin(e^{t})$ the integral converges for $\operatorname{Re} s > 0$ thanks to cancellation, but converges absolutely only for $\operatorname{Re} s > 1$.
