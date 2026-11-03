---
tag: FNVVV5E5F0
kind: definition
name: Permittivity
msc: [78A30, 78A25]
defines: F768YN0P2V
uses: [NJVXQZ780B, YZ7Q9DP8RT, ASQAH710WN]
sources:
  - url: https://en.wikipedia.org/wiki/Permittivity
---

## Definition

Let $\varepsilon_0 > 0$ be the vacuum permittivity.
Let $E$ be the [[electric field|YZ7Q9DP8RT]] and $P$ the [[polarization density|ASQAH710WN]] in a dielectric material.
The material is *linear and isotropic* if $P = \varepsilon_0 \chi_e E$ at each point for a real number $\chi_e \ge 0$.
The number $\chi_e$ is the electric susceptibility.
For such a material the *permittivity* is $\varepsilon = \varepsilon_0 (1 + \chi_e)$, so that the [[electric displacement field|NJVXQZ780B]] is
$$D = \varepsilon E.$$
The *relative permittivity* is $\varepsilon_r = \varepsilon / \varepsilon_0 = 1 + \chi_e$.

## Remarks

For a linear anisotropic material, $D = \varepsilon E$ with a $3 \times 3$ matrix $\varepsilon$, the permittivity tensor.
For time-harmonic fields the permittivity depends on the frequency and may be complex, with the imaginary part describing absorption.
Example: in a medium of constant permittivity $\varepsilon$, a point charge $q$ at $0$ has $D = q x / (4 \pi \abs{x}^3)$ and $E = q x / (4 \pi \varepsilon \abs{x}^3)$, so the field is weaker than in vacuum by the factor $\varepsilon_r$.
Non-example: a ferroelectric material has a polarization that is not proportional to $E$ and shows hysteresis, so it has no permittivity in this sense.
In SI units $\varepsilon_0 \approx 8.854 \times 10^{-12}$ farad per metre.
