---
tag: N470GNCK2Y
kind: concept
name: Mean-periodic function
msc: [42A75, 42A85]
sources:
  - url: https://en.wikipedia.org/wiki/Mean-periodic_function
same_as:
  wikidata: Q6803554
  wikipedia: Mean-periodic function
---

## Summary

A mean-periodic function is a continuous function on the real line that satisfies a convolution equation $f * \mu = 0$ for some nonzero compactly supported measure $\mu$.
A [[periodic function|0ATF6Q0633]] with period $p$ is the case $\mu = \delta_0 - \delta_p$, and exponentials $x^k e^{\lambda x}$ are also mean-periodic.
Equivalently, the translates of $f$ do not span a dense subspace of the continuous functions.
Laurent Schwartz proved that every mean-periodic function on $\R$ is a limit of exponential polynomials taken from the closed span of its translates.

## Explanations

### L1 human

A periodic function equals its own shift: $f(x) - f(x - p) = 0$.
A mean-periodic function satisfies a weaker rule: some fixed weighted average of its shifted copies is always zero.
For example, $e^{\lambda x}$ satisfies $f(x) - e^{\lambda} f(x - 1) = 0$, although it is not periodic for real $\lambda \ne 0$.
Such functions behave like sums of exponential waves, which explains the name.
