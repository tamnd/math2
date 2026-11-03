---
tag: X9XJ6RH3DB
kind: definition
name: Adiabatic flame temperature
msc: ["80A25", "80A30"]
defines: W0RDGHXHFD
uses: [722RZK72P5, F6JVQ12X43, W1RS8DA2H6, 2KMN67HYNC]
sources:
  - url: https://en.wikipedia.org/wiki/Adiabatic_flame_temperature
---

## Definition

Consider a fixed mass of a combustible mixture at initial temperature $T_i$ and pressure $p$.
Assume that it burns in an [[adiabatic process|W1RS8DA2H6]], with no work other than the work of expansion.
Assume that the products have a known composition, given either by complete combustion or by [[chemical equilibrium|2KMN67HYNC]].
Let $H_r(T, p)$ be the [[enthalpy|722RZK72P5]] of the reactants and $H_p(T, p)$ the enthalpy of the products, both measured from the same reference state of the elements.
The *constant-pressure adiabatic flame temperature* is the temperature $T_{\mathrm{ad}}$ such that
$$H_p(T_{\mathrm{ad}}, p) = H_r(T_i, p).$$
For combustion in a closed rigid vessel, the *constant-volume adiabatic flame temperature* is defined in the same way.
There the [[internal energy|F6JVQ12X43]] $U$ replaces $H$, and the volume is held fixed.

## Remarks

Example: assume complete combustion, a heat of reaction $Q > 0$ per unit mass of mixture at $T_i$, and a constant specific heat $c_p$ of the products.
Then $H_p(T, p) = H_r(T_i, p) - Q + c_p (T - T_i)$, and the defining equation gives $T_{\mathrm{ad}} = T_i + Q / c_p$.
Non-example: if the mixture loses an amount of heat $q > 0$ to the walls, the final temperature $T_f$ satisfies $H_p(T_f, p) = H_r(T_i, p) - q$.
The process is not adiabatic, and $T_f < T_{\mathrm{ad}}$ because $H_p$ increases with $T$.
The constant-volume value is higher than the constant-pressure value, since at constant volume no energy is spent on expansion work.
With chemical equilibrium, dissociation of the products at high temperature absorbs energy and lowers $T_{\mathrm{ad}}$ below the complete-combustion value.
For a stoichiometric methane–air mixture at room conditions, the constant-pressure value is about $2200$ K.
