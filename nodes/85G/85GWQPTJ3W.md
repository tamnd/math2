---
tag: 85GWQPTJ3W
kind: statement
role: proposition
name: Schwarzschild criterion for convection
msc: [85A15, "76E06", "76E20"]
uses: [4FC5XQA2RK, XQ82TE42FH]
about: [4FC5XQA2RK]
sources:
  - url: https://en.wikipedia.org/wiki/Convection_zone
---

## Statement

Consider a layer of a star in [[hydrostatic equilibrium|4FC5XQA2RK]], made of an ideal gas of uniform chemical composition.
Let $P$ be the pressure and $T$ the temperature.
Let $\nabla = d \ln T / d \ln P$ be the actual temperature gradient of the layer.
Let $\nabla_{\mathrm{ad}} = (\partial \ln T / \partial \ln P)_{s}$ be the adiabatic gradient, taken at constant entropy $s$.
Suppose that a small parcel of gas, displaced vertically, moves adiabatically and stays in pressure balance with its surroundings.
Then the layer is stable against convection if $\nabla < \nabla_{\mathrm{ad}}$, and unstable if $\nabla > \nabla_{\mathrm{ad}}$.

## Remarks

Raise a parcel by a small height, where the pressure is lower.
Its temperature changes along the adiabat, while the temperature of the surroundings changes along the actual gradient.
At equal pressure, the parcel is lighter than its surroundings exactly when it is hotter.
This happens when the surroundings cool faster with height than the adiabat, that is, when $\nabla > \nabla_{\mathrm{ad}}$; the parcel then keeps rising.
Example: for a fully ionized monatomic ideal gas, $\nabla_{\mathrm{ad}} = 2/5$, so a radiative layer whose radiative gradient exceeds $0.4$ becomes convective.
Equivalently, in terms of the [[Brunt–Väisälä frequency|XQ82TE42FH]] $N$, the layer is unstable when $N^2 < 0$.
With a gradient of composition the criterion must be replaced by the [[Ledoux criterion|CVZBK60C26]].

## Explanations

### L1 human

Imagine nudging a small blob of gas upward inside a star.
It expands and cools as it rises, because the pressure around it drops.
If it still ends up hotter than its new neighbours, it is lighter and keeps rising, and the layer boils: this is convection.
If it ends up cooler, it sinks back, and the layer stays calm.
The criterion compares how fast the star cools with height against how fast a rising blob cools.

### L2 human

In stellar models one computes the gradient $\nabla_{\mathrm{rad}}$ that radiation alone would need to carry the luminosity, and compares it with $\nabla_{\mathrm{ad}}$.
Where $\nabla_{\mathrm{rad}} > \nabla_{\mathrm{ad}}$, the layer is convective, and the temperature gradient is close to adiabatic.
This decides where the convective cores of massive stars and the convective envelopes of cool stars lie.
Inside a convection zone the heat flow is usually modelled by [[mixing length theory|HWPBFFHQ2Y]].
