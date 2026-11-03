---
tag: 84EKH5XPRK
kind: definition
name: Nusselt film condensation theory
msc: [80A19, 80A22, 76T10]
defines: NRXQWBBF3W
uses: [FN6Z9QKAH5, J821AD6YTE, XBQBT9E7JT, KK46Q2YV1D]
sources:
  - url: https://en.wikipedia.org/wiki/Condensation
---

## Definition

Consider a vertical plate of height $L$ at uniform [[temperature|KK46Q2YV1D]] $T_w$, in contact with quiescent saturated vapour at temperature $T_{\mathrm{sat}} > T_w$.
Let $x$ be the distance down the plate from its top and $g$ the gravitational acceleration.
Let $\rho_l$ and $\rho_v$ be the densities of liquid and vapour, and $\mu_l$ and $k_l$ the viscosity and [[thermal conductivity|XBQBT9E7JT]] of the liquid.
Let $h_{fg}$ be the [[latent heat|FN6Z9QKAH5]] of condensation per unit mass.
*Nusselt's film condensation theory* is the model of the condensate film with these assumptions:

1. The film is laminar and flows down under gravity, with constant properties.
2. Inertia and convection of momentum and heat in the film are neglected.
   So gravity, buoyancy and viscosity set the velocity profile, and heat crosses the film by conduction only.
3. There is no shear at the liquid–vapour interface, and the interface is at $T_{\mathrm{sat}}$.

Its result is the film thickness and the local [[heat transfer coefficient|J821AD6YTE]]
$$\delta(x) = \left(\frac{4 k_l \mu_l (T_{\mathrm{sat}} - T_w) \, x}{g \rho_l (\rho_l - \rho_v) h_{fg}}\right)^{1/4}, \qquad h(x) = \frac{k_l}{\delta(x)}.$$

## Remarks

Derivation: the velocity is $u(y) = \frac{g(\rho_l - \rho_v)}{\mu_l}\big(\delta y - \tfrac12 y^2\big)$, so the mass flow per unit width is $\Gamma = \rho_l g (\rho_l - \rho_v) \delta^3 / (3 \mu_l)$.
The heat conducted across the film condenses new liquid: $h_{fg} \, d\Gamma = k_l (T_{\mathrm{sat}} - T_w) / \delta \; dx$.
This gives $\delta^3 \, d\delta$ proportional to $dx$, so $\delta^4$ is proportional to $x$, which is the formula above.

Since $h \propto x^{-1/4}$, the mean over the plate is $\bar h = \tfrac43 h(L)$, that is
$$\bar h = 0.943 \left(\frac{g \rho_l (\rho_l - \rho_v) h_{fg} k_l^3}{\mu_l (T_{\mathrm{sat}} - T_w) L}\right)^{1/4}.$$

Non-example: on a tall cold plate the film becomes wavy and then turbulent; assumption 1 fails, and the formula underestimates the heat transfer.

A common refinement replaces $h_{fg}$ by $h_{fg} + 0.68 \, c_{p,l} (T_{\mathrm{sat}} - T_w)$ to account for the cooling of the film below $T_{\mathrm{sat}}$, where $c_{p,l}$ is the specific heat of the liquid.
