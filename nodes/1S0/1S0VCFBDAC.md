---
tag: 1S0VCFBDAC
kind: definition
name: Thermoelectric effect
msc: [82C35, 80A17, 82D37]
defines: 36BBVY7S4F
uses: [KK46Q2YV1D, 1Y36434YTE, CY4GJQGF06]
sources:
  - url: https://en.wikipedia.org/wiki/Thermoelectric_effect
---

## Definition

Let an isotropic conductor carry an electric current density $J$ and a [[heat flux|1Y36434YTE]] $J_Q$ at absolute [[temperature|KK46Q2YV1D]] $T(x)$.
Let $E$ be the effective electric field, the electric field plus the gradient of the chemical potential of the carriers divided by their charge.
In the linear regime the conductor obeys
$$J = \sigma (E - S \nabla T), \qquad J_Q = \Pi J - \kappa \nabla T,$$
where $\sigma > 0$ is the electrical conductivity and $\kappa > 0$ the thermal conductivity at zero current.
The *thermoelectric effect* is the coupling of $J$ and $J_Q$ through the coefficients $S$ and $\Pi$, in three forms.

1. Seebeck effect: at zero current, a temperature gradient produces the field $E = S \nabla T$; $S$ is the *Seebeck coefficient*.
2. Peltier effect: at uniform temperature, a current carries the [[heat|CY4GJQGF06]] flux $J_Q = \Pi J$; $\Pi$ is the *Peltier coefficient*.
3. Thomson effect: a steady current along a temperature gradient produces heat reversibly at the rate $-\mathcal{K}\, J \cdot \nabla T$ per unit volume. This adds to the Joule heating $\abs{J}^2/\sigma$, and $\mathcal{K}$ is the *Thomson coefficient*.

## Remarks

Example: let a thermocouple be made of two conductors $A$ and $B$, with junctions at temperatures $T_1$ and $T_2$.
Its open-circuit voltage is $\int_{T_1}^{T_2} (S_B - S_A)\, dT$, up to a sign that depends on the orientation.
Non-example: a conductor whose heat flux is $-\kappa \nabla T$ and whose current is $\sigma E$, with no coupling, shows no thermoelectric effect, since $S = \Pi = 0$.
The energy balance gives $\mathcal{K} = d\Pi/dT - S$.
The signs of $S$, $\Pi$ and $\mathcal{K}$ depend on conventions that vary between texts.
