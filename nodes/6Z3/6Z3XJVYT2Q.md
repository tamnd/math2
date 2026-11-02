---
tag: 6Z3XJVYT2Q
kind: concept
name: Laplace transform of distributions
msc: [46F12, 44A10]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Summary

The [[Laplace transform|0V49JEZW06]] extends from functions to distributions supported in $[0, \infty)$ that do not grow faster than an exponential.
The extension gives meaning to transforms of generalized functions such as the [[Dirac delta|0KPHENZ5S7]] and its derivatives: $\mathcal{L}\delta = 1$ and $\mathcal{L}\delta^{(k)} = s^k$.
It makes the rule "differentiation becomes multiplication by $s$" exact, with no initial-value terms, which is the natural setting for impulses in operational calculus.

## Explanations

### L1 human

Engineers like to feed a system an instantaneous kick, the Dirac delta, which is not a genuine function.
The ordinary Laplace transform cannot handle it, but the distributional version can, and it gives the delta the transform $1$.
The jump of a switched-on signal is then accounted for by a delta in its derivative.
For example, the unit step has transform $1/s$, and its derivative, the delta, has transform $s \cdot 1/s = 1$.
