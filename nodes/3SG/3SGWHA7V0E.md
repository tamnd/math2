---
tag: 3SGWHA7V0E
kind: definition
name: Permeability
msc: [78A30, 78A25]
defines: 5MJQ5J5H8Z
uses: [XRED3C547P, A2WZA4QA3V]
sources:
  - url: https://en.wikipedia.org/wiki/Permeability_(electromagnetism)
---

## Definition

Let $\mu_0 > 0$ be the vacuum permeability.
Consider a material with [[magnetization|A2WZA4QA3V]] $M$ in a [[magnetic field|XRED3C547P]] $B$, and let $H = B / \mu_0 - M$ be the magnetizing field.
The material is *linear and isotropic* if there is a scalar $\chi_m$, the magnetic susceptibility, such that $M = \chi_m H$ for all fields in the range considered.
Its *permeability* is then the scalar
$$\mu = \mu_0 (1 + \chi_m),$$
so that $B = \mu H$.
The *relative permeability* is $\mu_r = \mu / \mu_0 = 1 + \chi_m$.

## Remarks

The vacuum permeability is $\mu_0 \approx 1.25663706 \times 10^{-6}$ newtons per square ampere, very close to $4 \pi \times 10^{-7}$.
It is related to the vacuum permittivity $\varepsilon_0$ and the speed of light $c$ by $\varepsilon_0 \mu_0 c^2 = 1$.

Example: vacuum has $M = 0$, so $\chi_m = 0$ and $\mu = \mu_0$.

Non-example: a ferromagnet such as iron shows hysteresis.
Its magnetization depends on the past of the applied field, so $M$ is not a fixed multiple of $H$, and no single constant $\mu$ describes it.
For such materials one uses the slope of the curve of $B$ against $H$ at a point of operation instead.

For an anisotropic linear material $\chi_m$ is replaced by a $3 \times 3$ matrix, and the permeability becomes a tensor.
Materials with $\chi_m > 0$ small are called paramagnetic, and those with $\chi_m < 0$ are called diamagnetic.
