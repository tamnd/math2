---
tag: TWJ602ABBD
kind: definition
name: Joule–Thomson effect
msc: [80A10, 76N15]
defines: WABJJAQ3WV
uses: [722RZK72P5, W1RS8DA2H6, D36GZB2766, SYYGZ18FF5, 2NRW3XGP3T, N7R0H2VNDJ, 05AXG3QRKR]
sources:
  - url: https://en.wikipedia.org/wiki/Joule–Thomson_effect
---

## Definition

Let a fluid flow steadily through a throttle, such as a valve or a porous plug, from pressure $p_1$ to pressure $p_2 < p_1$.
Assume that the flow is [[adiabatic|W1RS8DA2H6]], that no shaft work is done, and that the changes of kinetic and potential energy are negligible.
Then the specific [[enthalpy|722RZK72P5]] is the same before and after the throttle, $h_1 = h_2$; this [[irreversible|D36GZB2766]] process is the *Joule–Thomson expansion*.
The *Joule–Thomson effect* is the resulting change of temperature, and the *Joule–Thomson coefficient* is the [[partial derivative|05AXG3QRKR]]
$$\mu_{\mathrm{JT}} = \left( \frac{\partial T}{\partial p} \right)_H.$$

## Remarks

A positive $\mu_{\mathrm{JT}}$ means the fluid cools on expansion, a negative one that it warms.
The states where $\mu_{\mathrm{JT}} = 0$ form the inversion curve in the $(T, p)$ plane.
From $dH = T\,dS + V\,dp$ and a Maxwell relation one gets
$$\mu_{\mathrm{JT}} = \frac{V}{C_p} (T \alpha - 1),$$
where $C_p$ is the [[heat capacity|SYYGZ18FF5]] at constant pressure and $\alpha$ the [[thermal expansion coefficient|2NRW3XGP3T]].

Example: for a van der Waals gas at low pressure, $\mu_{\mathrm{JT}} \approx \frac{1}{C_{p,m}} \left( \frac{2a}{RT} - b \right)$ per mole, so it cools below the inversion temperature $2a/(Rb)$ and warms above it.

Non-example: for an [[ideal gas|N7R0H2VNDJ]], $\alpha = 1/T$, so $T\alpha - 1 = 0$ and $\mu_{\mathrm{JT}} = 0$.
Since its enthalpy depends only on temperature, constant enthalpy means constant temperature, and there is no effect.
