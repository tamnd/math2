---
tag: RAGR38Q40B
kind: concept
name: Lp multiplier
msc: [42B15, 42A45]
specializes: [ZQEFCY61T7]
sources:
  - url: https://en.wikipedia.org/wiki/Multiplier_(Fourier_analysis)
---

## Summary

An $L^p$ multiplier is a bounded function $m$ on $\R^n$ such that the operator $f \mapsto (m \hat f)^\vee$ is bounded on the [[$L^p$ space|SASP14MA1Z]] $L^p(\R^n)$.
It is a [[Fourier multiplier|ZQEFCY61T7]] that respects the size of functions measured in the $L^p$ norm.
For $p = 2$ every bounded function is an $L^p$ multiplier, but for $p \ne 2$ the question is subtle.
Many operators of analysis and PDE are multiplier operators, such as partial sums of Fourier integrals and Riesz transforms.
So criteria for $L^p$ multipliers are a central topic of harmonic analysis.

## Explanations

### L1 human

A multiplier operator changes a function by turning each of its frequencies up or down by a factor $m(\xi)$.
The question is whether this change can blow up the size of the function.
In the $L^2$ norm, the size is the total energy over all frequencies, so a bounded factor can never blow it up.
In other $L^p$ norms, sharp cuts in the frequency picture can make the function much larger, so not every bounded $m$ works.
For example, $m(\xi) = e^{2\pi i \xi h}$ only shifts a function by $h$, so it keeps every $L^p$ norm and is an $L^p$ multiplier for all $p$.
