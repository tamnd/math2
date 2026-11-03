---
tag: FN5YH8KTFV
kind: definition
name: Electromagnetic stress–energy tensor
msc: [78A25, 83A05, 83C50]
defines: N22WEQ3GWH
uses: [WRZJRJS44W, P3PK0Q02CZ, ZWVYST76GE, WX302T93TW]
sources:
  - url: https://en.wikipedia.org/wiki/Electromagnetic_stress%E2%80%93energy_tensor
---

## Definition

Work in Minkowski space with coordinates $x^0 = ct, x^1, x^2, x^3$ and metric $\eta = \operatorname{diag}(1, -1, -1, -1)$.
Let $F^{\mu\nu}$ be the [[electromagnetic tensor|WRZJRJS44W]] and $\mu_0 > 0$ the vacuum permeability.
The *electromagnetic stress–energy tensor* is the symmetric [[tensor field|WX302T93TW]]
$$T^{\mu\nu} = \frac{1}{\mu_0} \Big( \eta_{\alpha\beta} F^{\mu\alpha} F^{\beta\nu} + \frac{1}{4} \eta^{\mu\nu} F_{\alpha\beta} F^{\alpha\beta} \Big),$$
with summation over repeated indices.

## Remarks

In terms of the electric field $E$ and the magnetic field $B$:

1. $T^{00} = \frac{\varepsilon_0}{2} \abs{E}^2 + \frac{1}{2 \mu_0} \abs{B}^2$ is the energy density.
2. $T^{0i} = T^{i0} = S_i / c$, where $S$ is the [[Poynting vector|P3PK0Q02CZ]].
3. $T^{ij} = -\sigma_{ij}$, where $\sigma$ is the [[Maxwell stress tensor|ZWVYST76GE]].

Example: for a static uniform field $E = (0, 0, E_0)$, $B = 0$, the tensor is $\frac{\varepsilon_0 E_0^2}{2} \operatorname{diag}(1, 1, 1, -1)$; the last entry is a tension along the field.

The tensor is traceless, $\eta_{\mu\nu} T^{\mu\nu} = 0$, as a direct computation shows in four dimensions.
For solutions of Maxwell's equations without sources, $\partial_\nu T^{\mu\nu} = 0$; the component $\mu = 0$ is Poynting's theorem and the components $\mu = i$ are the momentum balance.

Non-example: the tensor $\frac{1}{\mu_0} \eta_{\alpha\beta} F^{\mu\alpha} F^{\beta\nu}$ without the trace term gives $T^{00} = \varepsilon_0 \abs{E}^2$ when $B = 0$, which is twice the correct energy density.
