---
tag: 3SCXCW4AH3
kind: concept
name: Calderón–Zygmund operator
msc: [42B20, 47G10]
specializes: [HTMCEARGDD]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_integral
---

## Summary

A Calderón–Zygmund operator is a bounded linear operator on $L^2(\R^n)$ that is given away from the diagonal by integration against a [[Calderón–Zygmund kernel|78N6AXP9VV]].
This class contains the Hilbert transform, the [[Riesz transforms|FRNDFJ9WQ5]], the operators with smooth multipliers of Hörmander–Mikhlin type, and many operators that are not translation invariant.
Every Calderón–Zygmund operator is bounded on $L^p(\R^n)$ for $1 < p < \infty$ and of weak type $(1, 1)$.
This makes it the standard class of [[singular integral operators|HTMCEARGDD]].

## Explanations

### L1 human

A Calderón–Zygmund operator averages a function against a kernel that blows up near the diagonal at the borderline rate.
The definition asks for two things: the operator is already known to be bounded in the energy norm $L^2$, and its kernel has the right size and smoothness.
The theory then shows that the operator is bounded in every $L^p$ norm with $1 < p < \infty$.
The Hilbert transform $f \mapsto \frac{1}{\pi}\,\mathrm{p.v.}\int \frac{f(y)}{x - y} \, dy$ is the basic example.
