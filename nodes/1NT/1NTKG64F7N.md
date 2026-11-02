---
tag: 1NTKG64F7N
kind: concept
name: Radon–Nikodym derivative
msc: [28A15]
sources:
  - url: https://en.wikipedia.org/wiki/Radon–Nikodym_theorem
---

## Summary

The Radon–Nikodym derivative $d\nu / d\mu$ is the density of one measure $\nu$ with respect to another measure $\mu$.
It exists when both measures are σ-finite and $\nu$ is absolutely continuous with respect to $\mu$, by the [[Radon–Nikodym theorem|1ZSZS5G1Q4]].
It turns integrals against $\nu$ into integrals against $\mu$.
Probability densities, likelihood ratios and conditional expectations are all Radon–Nikodym derivatives.

## Explanations

### L1 human

Think of $\mu$ as a way to measure size and $\nu$ as a way to measure mass.
The derivative $d\nu / d\mu$ at a point is the mass per unit size near that point.
For the standard normal distribution $\nu$ and Lebesgue measure $\mu$ on the line, the derivative is the bell curve $e^{-x^2/2}/\sqrt{2\pi}$.
The name comes from the rule $d\nu = \frac{d\nu}{d\mu} \, d\mu$, which looks like the chain rule of calculus.
