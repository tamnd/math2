---
tag: 6J9MPVHSMF
kind: concept
name: Linear time-invariant system
msc: [93C05, 93C80]
specializes: [21FN2KSTJZ]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_time-invariant_system
same_as:
  wikidata: Q1808960
  wikipedia: Linear time-invariant system
---

## Summary

A linear time-invariant system, or LTI system, is a system that is both [[linear|21FN2KSTJZ]] and [[time-invariant|S4THJVE1AJ]].
Its output is the [[convolution|2Z29JN3VES]] of the input with one fixed signal, the [[impulse response|3X3SYVM7R5]].
After a [[Laplace transform|0V49JEZW06]] or a Fourier transform, convolution becomes multiplication by the [[transfer function|86JKV3TRFD]].
This makes LTI systems the best understood class of systems, and the standard model in signal processing and classical control.

## Explanations

### L1 human

An LTI system obeys superposition and does not care when an input arrives.
So it is enough to know its answer to a single short kick at time $0$.
Any input is a sum of shifted and scaled kicks, and the output is the same sum of shifted and scaled answers.
For example, the moving average $y[n] = \tfrac{1}{2}(u[n] + u[n - 1])$ is LTI, and its answer to a kick is $\tfrac12$ at times $0$ and $1$ and $0$ elsewhere.
