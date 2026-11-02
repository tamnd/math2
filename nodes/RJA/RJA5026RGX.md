---
tag: RJA5026RGX
kind: concept
name: Integral of a Hopf algebra
msc: [16T05]
sources:
  - url: https://en.wikipedia.org/wiki/Hopf_algebra
---

## Summary

A left integral in a [[Hopf algebra|7XFYP0N84H]] $H$ is an element $\Lambda$ that absorbs left multiplication through the counit: $h \Lambda = \varepsilon(h) \Lambda$ for all $h \in H$.
For a finite group algebra $KG$, the sum of all group elements is an integral.
Integrals generalize averaging over a finite group and the Haar measure of a compact group.
By the [[Larson–Sweedler theorem|BZPKCPCWTM]], the left integrals of a finite-dimensional Hopf algebra form a one-dimensional space.
Such an $H$ is semisimple exactly when $\varepsilon(\Lambda) \ne 0$ for a nonzero left integral $\Lambda$.

## Explanations

### L1 human

For a finite group, the sum $\sum_g g$ of all its elements does not change when it is multiplied by any element of the group, because multiplication only reorders the terms.
An integral is the Hopf algebra version of such an invariant sum.
Dividing it by the size of the group gives the averaging operator used to prove Maschke's theorem.
The criterion $\varepsilon(\Lambda) \ne 0$ is the Hopf algebra form of the condition that the size of the group is invertible in the field.
