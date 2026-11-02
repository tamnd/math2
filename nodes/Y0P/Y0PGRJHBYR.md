---
tag: Y0PGRJHBYR
kind: concept
name: Poisson–Mellin–Newton cycle
msc: [44A15, 39A70, 68W40]
sources:
  - url: https://en.wikipedia.org/wiki/N%C3%B8rlund%E2%80%93Rice_integral
---

## Summary

The Poisson–Mellin–Newton cycle is a chain of three transforms that links a sequence $(f_n)$, its Poisson generating function, and the [[Mellin transform|N5PVGRJE1T]] of that function.
Going round the cycle recovers the sequence from the Mellin transform by a Nörlund–Rice integral, which is a contour integral over a Newton-type kernel.
It explains why alternating binomial sums and the Mellin transform have the same kind of asymptotic analysis.
It is used in the average-case analysis of algorithms such as digital search trees and tries.

## Explanations

### L1 human

Start with a sequence $f_0, f_1, f_2, \dots$ of numbers.
Mix it with a Poisson weight to get a smooth function $g(t) = e^{-t} \sum_n f_n t^n / n!$, which is the mean of $f_N$ when $N$ is a Poisson random number with mean $t$.
Take the Mellin transform of $g$; its poles describe how $g(t)$ behaves for small and large $t$.
A contour integral then turns the Mellin transform back into the numbers $f_n$, and this closes the cycle.
For example, for the constant sequence $f_n = 1$ one gets $g(t) = 1$ for all $t$.
