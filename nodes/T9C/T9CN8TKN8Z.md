---
tag: T9CN8TKN8Z
kind: statement
role: fact
name: Terzaghi's principle of effective stress
msc: [74L10, 74F10]
uses: [KG2XWEMJ30, Q5CF1Z6179]
about: [987R9XR8KH]
sources:
  - url: https://en.wikipedia.org/wiki/Effective_stress
---

## Statement

Consider a soil whose pores are fully saturated with water at pore pressure $u$.
Let $\sigma$ be the total [[Cauchy stress|KG2XWEMJ30]], with compressive stresses counted positive as is usual in soil mechanics.
Define the *effective stress*
$$\sigma' = \sigma - u I,$$
so that each effective normal stress is the total normal stress minus the pore pressure, and shear stresses are unchanged.
Then all measurable effects of a change of stress on the soil are due to changes of the effective stress $\sigma'$ alone.
These effects include compression, distortion and change of shear strength.

## Remarks

The principle is an empirical law of soil mechanics, not a theorem; it is accurate when the soil grains and the water are much less compressible than the soil skeleton.
Example: in the [[Mohr–Coulomb|Q5CF1Z6179]] failure criterion it gives the drained shear strength $\tau_f = c' + \sigma'_n \tan\phi'$.
Raising the pore pressure $u$ at fixed total stress lowers $\sigma'_n$ and weakens the soil, which is why saturated slopes can slide after heavy rain.
Take a uniform soil with saturated unit weight $\gamma_{\mathrm{sat}}$ and the water table at the surface.
At a depth $z$ the vertical effective stress is $\sigma'_v = (\gamma_{\mathrm{sat}} - \gamma_w) z$, where $\gamma_w$ is the unit weight of water.
In [[poroelasticity|987R9XR8KH]] the principle is refined to Biot's effective stress $\sigma - \alpha u I$ with a Biot coefficient $\alpha \le 1$; Terzaghi's form is the case $\alpha = 1$.

## Explanations

### L1 human

A wet soil is a frame of grains with water in between.
Part of any load is carried by the water pressure and the rest by the grains pressing on each other.
Terzaghi's principle says that only the part carried by the grains, the effective stress, makes the soil compress or fail.
That is why the same soil can be firm when dry and give way when water pressure builds up in it.

### L2 human

Effective stress is the variable in which constitutive laws for soils, such as Mohr–Coulomb and critical state models, are written.
It is the link between the mechanics of the skeleton and the flow of pore water, and it is the stress that enters consolidation theory.
Undrained and drained analyses differ in how the pore pressure is determined, but both use $\sigma'$ to decide deformation and failure.
