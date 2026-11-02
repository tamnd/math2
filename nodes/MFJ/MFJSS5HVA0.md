---
tag: MFJSS5HVA0
kind: concept
name: Volterra equations with completely monotone kernels
msc: [45D05, "45E10", 26A48]
specializes: [SNFYTC1TTA]
sources:
  - url: https://en.wikipedia.org/wiki/Bernstein%27s_theorem_on_monotone_functions
---

## Summary

These are [[Volterra equations of convolution type|SNFYTC1TTA]] whose kernel $k$ is completely monotone on $(0, \infty)$: it is infinitely differentiable and its derivatives alternate in sign.
By [[Bernstein's theorem on monotone functions|ZBS1JA62QP]], such a kernel is a superposition $k(t) = \int e^{-st} \, d\mu(s)$ of decaying exponentials with a positive measure $\mu$.
The class contains the exponential kernels and the Abel kernels $t^{\alpha - 1}$ with $0 < \alpha < 1$.
It is a natural setting for positivity and decay results for solutions.
Such kernels model fading memory, for instance in linear viscoelasticity.

## Explanations

### L1 human

A completely monotone kernel describes a memory that fades with time in the most regular way possible.
It is positive, decreasing, convex, and so on for all higher derivatives.
Each such kernel is a mixture of simple exponential memories $e^{-st}$ with different decay rates $s$.
For example, $k(t) = 1/\sqrt{t}$ is completely monotone: it is the mixture $\frac{1}{\sqrt{\pi}} \int_0^\infty e^{-st} s^{-1/2} \, ds$.
So Abel's integral equation is an equation of this type.
