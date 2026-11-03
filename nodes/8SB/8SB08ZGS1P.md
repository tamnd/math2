---
tag: 8SB08ZGS1P
kind: definition
name: Thermal expansion coefficient
msc: [80A10, 74A15]
defines: 2NRW3XGP3T
uses: [WYAY33ZVYQ, 05AXG3QRKR, N7R0H2VNDJ]
sources:
  - url: https://en.wikipedia.org/wiki/Thermal_expansion
---

## Definition

Let a simple system with a fixed amount of matter have volume $V > 0$, pressure $p$ and temperature $T$, with $V$ a differentiable function of $(T, p)$.
The *(volumetric) thermal expansion coefficient* is the [[partial derivative|05AXG3QRKR]] expression
$$\alpha = \frac{1}{V} \left( \frac{\partial V}{\partial T} \right)_p,$$
the relative change of volume per unit temperature along an [[isobaric process|WYAY33ZVYQ]].

## Remarks

For a solid one also uses the linear coefficient $\alpha_L = \frac{1}{L} \frac{dL}{dT}$ of a length $L$; for an isotropic solid with small expansion, $\alpha \approx 3 \alpha_L$.
By a Maxwell relation, $\alpha V = -(\partial S / \partial p)_T$, where $S$ is the entropy.

Example: for an [[ideal gas|N7R0H2VNDJ]], $V = nRT/p$, so $(\partial V / \partial T)_p = nR/p = V/T$ and $\alpha = 1/T$.
At $T = 300\,\mathrm{K}$ this gives $\alpha \approx 3.3 \times 10^{-3}\,\mathrm{K}^{-1}$.

Non-example of the usual sign: liquid water at atmospheric pressure between $0\,^\circ\mathrm{C}$ and $4\,^\circ\mathrm{C}$ has $\alpha < 0$.
The definition still applies; only the expectation $\alpha > 0$ fails, and nothing in thermodynamic stability forces $\alpha$ to be positive.
