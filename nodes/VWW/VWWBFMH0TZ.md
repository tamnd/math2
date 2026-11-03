---
tag: VWWBFMH0TZ
kind: definition
name: Lapse rate
msc: [86A10]
defines: ZPXXA62VQB
uses: [0ABK9V9Y64]
sources:
  - url: https://en.wikipedia.org/wiki/Lapse_rate
---

## Definition

Let $T(z)$ be the temperature of the atmosphere at height $z$ above a point of the surface, a differentiable function of $z$.
The *lapse rate* at height $z$ is
$$\Gamma(z) = -\frac{dT}{dz}(z).$$
It is minus the vertical component of the [[gradient|0ABK9V9Y64]] of the temperature field, so it is positive when temperature decreases with height.

## Remarks

The *dry adiabatic lapse rate* is $\Gamma_d = g/c_p$, where $g$ is the gravitational acceleration and $c_p$ the specific heat of dry air at constant pressure.
It follows from the energy balance $c_p \, dT = dp/\rho$ of a rising parcel without heat exchange together with hydrostatic balance $dp = -\rho g \, dz$, which give $dT/dz = -g/c_p$.
With $g = 9.81$ m/s² and $c_p = 1004$ J/(kg K), $\Gamma_d \approx 9.8$ K/km.
Example: in the International Standard Atmosphere, $T(z) = 288.15 - 0.0065 z$ in kelvin, with $z$ in metres, up to 11 km, so $\Gamma = 6.5$ K/km.
Non-example: the rate $-\partial T/\partial t$ at which the air at a fixed place cools at night is not a lapse rate.
It is a derivative in time, not in height.
In a temperature inversion the temperature increases with height, so $\Gamma < 0$ there.
For dry air, a layer with $\Gamma < \Gamma_d$ is statically stable and a layer with $\Gamma > \Gamma_d$ is unstable.
