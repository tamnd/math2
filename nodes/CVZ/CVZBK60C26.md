---
tag: CVZBK60C26
kind: statement
role: proposition
name: Ledoux criterion
msc: [85A15, "76E06", "76E20"]
uses: [85GWQPTJ3W, 4FC5XQA2RK, XQ82TE42FH]
about: [85GWQPTJ3W]
sources:
  - url: https://en.wikipedia.org/wiki/Convection_zone
---

## Statement

Consider a layer of a star in [[hydrostatic equilibrium|4FC5XQA2RK]], in which the mean molecular weight $\mu$ may vary with depth.
Let $P$, $T$ and $\rho$ be the pressure, the temperature and the density, and let $\nabla = d \ln T / d \ln P$ and $\nabla_\mu = d \ln \mu / d \ln P$ be the actual gradients of the layer.
Let $\nabla_{\mathrm{ad}}$ be the adiabatic gradient, and let $\delta = -(\partial \ln \rho / \partial \ln T)_{P, \mu}$ and $\varphi = (\partial \ln \rho / \partial \ln \mu)_{P, T}$.
Suppose that a small displaced parcel moves adiabatically, keeps its composition, and stays in pressure balance with its surroundings.
Then the layer is stable against convection if
$$\nabla < \nabla_{\mathrm{ad}} + \frac{\varphi}{\delta} \nabla_\mu,$$
and unstable if the opposite strict inequality holds.

## Remarks

The argument is that of the [[Schwarzschild criterion|85GWQPTJ3W]], but now a rising parcel carries its own composition.
So the densities of the parcel and of its surroundings also differ because of $\mu$.
For an ideal gas, $\delta = \varphi = 1$, and the condition of stability reads $\nabla < \nabla_{\mathrm{ad}} + \nabla_\mu$.
Example: around a core that has burnt part of its hydrogen, the heavier helium-rich gas lies deeper, so $\mu$ increases inward, $\nabla_\mu > 0$, and the composition gradient stabilizes the layer.
When $\nabla_\mu = 0$ the criterion reduces to the Schwarzschild criterion.
Layers with $\nabla_{\mathrm{ad}} < \nabla < \nabla_{\mathrm{ad}} + (\varphi/\delta) \nabla_\mu$ are stable by Ledoux but unstable by Schwarzschild; in them slow semiconvective mixing can occur.
The criterion is equivalent to the sign condition $N^2 > 0$ on the [[Brunt–Väisälä frequency|XQ82TE42FH]] including the composition term.

## Explanations

### L1 human

Heavy gas sitting below light gas is hard to stir, even if it is a bit too hot.
The Ledoux criterion adds this effect to the simpler Schwarzschild test for convection.
A layer in which the composition gets heavier with depth can stay calm, although its temperature profile alone would make it boil.

### L2 human

The difference between the two criteria matters in the regions left behind by a shrinking or growing convective core, where hydrogen and helium are layered.
Which criterion to use, and how fast semiconvection mixes, changes the computed lifetimes and tracks of massive stars.
For a uniform composition both criteria agree.
