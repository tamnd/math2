---
tag: DC81TCR98Y
kind: concept
name: (p,q)-form
msc: [32W05, 58A10]
specializes: [0E3G0GRPZ6]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_differential_form
---

## Summary

A $(p, q)$-form on an open subset of $\C^n$, or on a complex manifold, is a complex-valued [[differential form|0E3G0GRPZ6]] of a special type.
Each of its terms contains $p$ of the differentials $dz_j$ and $q$ of the conjugate differentials $d\bar z_j$.
Every complex differential form of degree $k$ splits in a unique way as a sum of $(p, q)$-forms with $p + q = k$.
This splitting does not depend on the choice of holomorphic coordinates.
It is the setting of the [[$\bar\partial$ operator|M1VKCW3RFW]] and of Dolbeault cohomology.

## Explanations

### L1 human

In $\C$, the differential $dx$ of the real part and $dy$ of the imaginary part can be traded for $dz = dx + i\,dy$ and $d\bar z = dx - i\,dy$.
A $(p, q)$-form is a form whose terms each contain exactly $p$ factors of the kind $dz_j$ and $q$ of the kind $d\bar z_j$.
For example, $dz_1 \wedge d\bar z_2$ in $\C^2$ is a $(1, 1)$-form.
The form $dx_1 = \tfrac12 (dz_1 + d\bar z_1)$ is a sum of a $(1, 0)$-form and a $(0, 1)$-form, so it has no single type.
