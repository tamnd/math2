---
tag: 8M48N2ETSP
kind: statement
role: theorem
name: von Zeipel theorem
msc: [85A15, 76U05]
uses: [4FC5XQA2RK, WETKRE94E0]
about: [WETKRE94E0]
sources:
  - url: https://en.wikipedia.org/wiki/Von_Zeipel_theorem
same_as:
  wikidata: Q1616875
  wikipedia: Von Zeipel theorem
---

## Statement

Consider a star whose rotation is uniform, or more generally conservative, so that the centrifugal force has a potential.
Let $\Psi$ be the total potential, the sum of the gravitational and the centrifugal potentials.
Suppose that the star is in [[hydrostatic equilibrium|4FC5XQA2RK]] in the rotating frame.
Suppose that its pressure $P$ depends only on its density $\rho$ and temperature $T$.
Suppose that energy is carried by radiation, with flux $F = -\frac{4 a c T^3}{3 \kappa \rho} \nabla T$.
Here $a$ is the radiation constant, $c$ the speed of light and $\kappa(\rho, T)$ the opacity.
Let $g_{\mathrm{eff}} = \abs{\nabla \Psi}$ be the effective gravity.
Then on every surface of constant $\Psi$, the radiative flux is proportional to $g_{\mathrm{eff}}$.
In particular, the [[effective temperature|WETKRE94E0]] at the surface satisfies $T_{\mathrm{eff}} \propto g_{\mathrm{eff}}^{1/4}$.

## Remarks

Hydrostatic equilibrium reads $\nabla P = -\rho \nabla \Psi$, which forces $P$ and $\rho$ to be functions of $\Psi$ alone, and then so are $T$ and $\kappa$.
So $\nabla T = T'(\Psi) \nabla \Psi$, and the flux is $F = -f(\Psi) \nabla \Psi$ for a function $f$ that is constant on each level surface, which gives $\abs{F} = f(\Psi) \, g_{\mathrm{eff}}$.
Since $\sigma T_{\mathrm{eff}}^4 = \abs{F}$ at the surface, with $\sigma$ the Stefan–Boltzmann constant, $T_{\mathrm{eff}} \propto g_{\mathrm{eff}}^{1/4}$.
Example: a rapidly rotating star is flattened, and its effective gravity is larger at the poles than at the equator.
So its poles are hotter and brighter than its equator; this is called gravity darkening.
A consequence, known as von Zeipel's paradox, is that a uniformly rotating star cannot be in strict radiative equilibrium: $\nabla \cdot F$ does not vanish in general, which drives slow meridional circulation.

## Explanations

### L1 human

A star that spins fast bulges at its equator.
There, the surface is farther from the centre and the spin partly cancels gravity, so the effective pull is weaker.
The theorem says that the light coming out of each patch of surface is proportional to the pull there.
So the equator of a fast-spinning star is dimmer and cooler than its poles.

### L2 human

Gravity darkening has been observed by interferometry on fast rotators such as Altair and Vega.
The law $T_{\mathrm{eff}} \propto g_{\mathrm{eff}}^{1/4}$ holds for radiative envelopes; for convective envelopes a smaller exponent is used in practice.
The theorem was stated by Hugo von Zeipel in 1924.
