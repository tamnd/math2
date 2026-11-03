---
tag: RH17N68SJP
kind: definition
name: Eddington luminosity
msc: [85A15, 85A25]
defines: WSJ9G94MXZ
uses: [29WRN5J730, 4FC5XQA2RK]
sources:
  - url: https://en.wikipedia.org/wiki/Eddington_luminosity
---

## Definition

Let $M > 0$ be the mass of a spherically symmetric body.
Let the gas around it have opacity $\kappa > 0$, the cross-section per unit mass for absorption and scattering of radiation.
Let $G$ be the gravitational constant and $c$ the speed of light.
The *Eddington luminosity* of the body is
$$L_{\mathrm{Edd}} = \frac{4 \pi G M c}{\kappa}.$$

## Remarks

At distance $r$, the radiative force on a unit mass of gas is $\kappa L / (4 \pi r^2 c)$.
The Eddington luminosity is the value of $L$ for which it equals the gravitational force $G M / r^2$ given by [[Newton's law of gravitation|29WRN5J730]].
For $L < L_{\mathrm{Edd}}$ gravity wins and a static atmosphere in [[hydrostatic equilibrium|4FC5XQA2RK]] is possible.
Example: for fully ionized hydrogen the opacity is that of electron scattering, $\kappa = \sigma_T / m_p$.
Here $\sigma_T$ is the Thomson cross-section and $m_p$ the proton mass.
Then $L_{\mathrm{Edd}} = 4 \pi G M m_p c / \sigma_T$, about $1.26 \times 10^{31} \, \mathrm{W}$, or $3.2 \times 10^4$ solar luminosities, per solar mass.
Non-example: a luminosity $L = 2 L_{\mathrm{Edd}}$ does not balance gravity, since the radiative force on each unit mass is then twice the gravitational force, and the gas is driven outward.
The ratio $L / L_{\mathrm{Edd}}$ is called the Eddington ratio.
