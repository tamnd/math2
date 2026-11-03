---
tag: XG8W326PPJ
kind: definition
name: Compressibility
msc: [80A10, 76N15]
defines: 1BPF2AA6VR
uses: [C9MM7GFRWN, ECAXF3AWWX, 05AXG3QRKR, N7R0H2VNDJ, NA1VVMJXVA]
sources:
  - url: https://en.wikipedia.org/wiki/Compressibility
---

## Definition

Let a simple system with a fixed amount of matter have volume $V > 0$, pressure $p$, temperature $T$ and entropy $S$.
Assume that $V$ is a differentiable function of the state.
The *isothermal compressibility* is
$$\kappa_T = -\frac{1}{V} \left( \frac{\partial V}{\partial p} \right)_T,$$
the relative change of volume per unit pressure along an [[isothermal process|C9MM7GFRWN]].
The *isentropic compressibility* is
$$\kappa_S = -\frac{1}{V} \left( \frac{\partial V}{\partial p} \right)_S,$$
the same quantity along an [[isentropic process|ECAXF3AWWX]].
Both derivatives are [[partial derivatives|05AXG3QRKR]].

## Remarks

The bulk modulus is $K = 1/\kappa$.
The two compressibilities are related by $\kappa_S / \kappa_T = C_V / C_p = 1/\gamma$, where $\gamma$ is the [[heat capacity ratio|NA1VVMJXVA]].

Example: for an [[ideal gas|N7R0H2VNDJ]], $V = nRT/p$, so $(\partial V / \partial p)_T = -nRT/p^2 = -V/p$ and $\kappa_T = 1/p$.
Along a reversible adiabat $pV^\gamma$ is constant, so $(\partial V / \partial p)_S = -V/(\gamma p)$ and $\kappa_S = 1/(\gamma p)$.

Non-example: in the two-phase region of a pure fluid at fixed temperature, the volume changes while the pressure stays at the vapour pressure.
There $(\partial p / \partial V)_T = 0$, so $\kappa_T$ is not finite.
