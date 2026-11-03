---
tag: EWJNRCTB9Z
kind: definition
name: Radiative forcing
msc: [86A08, 86A10]
defines: B8HRNPHNZF
uses: [M49PQ7BDYN]
sources:
  - url: https://en.wikipedia.org/wiki/Radiative_forcing
---

## Definition

Let $N$ be the net downward radiative flux at the top of the atmosphere, in $\mathrm{W/m^2}$.
It is absorbed solar minus outgoing infrared radiation, averaged over the globe and over a year.
Consider an imposed change of an external factor of the climate system.
Examples are the concentration of a greenhouse gas, the amount of aerosols or the solar output.
The *radiative forcing* $\Delta F$ of the change is the resulting change of $N$, with the global mean surface temperature held at its prior value.

Variants differ in what else is held fixed:

1. the *instantaneous forcing* holds the whole state of the atmosphere fixed;
2. the *stratospheric-adjusted forcing* lets the temperature of the stratosphere adjust to radiative equilibrium, and measures the flux at the tropopause;
3. the *effective radiative forcing* lets the atmosphere and land adjust, as computed in a [[climate model|M49PQ7BDYN]], with the sea surface temperature held fixed.

## Remarks

Example: a widely used fit for carbon dioxide at concentration $c$, relative to a reference $c_0$, is $\Delta F = 5.35 \ln(c / c_0) \ \mathrm{W/m^2}$.
For a doubling, $c / c_0 = 2$, it gives $\Delta F = 5.35 \ln 2 \approx 3.7 \ \mathrm{W/m^2}$.
The logarithm reflects the saturation of the strongest absorption bands of carbon dioxide.

Non-example: the extra infrared emission of a planet that has already warmed is not a forcing but part of the response, since the definition holds the surface temperature fixed.

A positive forcing makes $N > 0$, so the climate system gains energy and warms until $N$ returns to $0$.
