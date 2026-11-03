---
tag: XJFSEZEH0M
kind: problem
name: Chapman–Ferraro problem
msc: [86A25, 76W05]
uses: [Z13HPJFV1F, 2KPTTBM584, T8JWCBK9M6]
about: [Z13HPJFV1F]
sources:
  - url: https://en.wikipedia.org/wiki/Magnetopause
history:
  posed_by: Sydney Chapman and Vincenzo Ferraro
  first_stated: "1930"
---

## Problem

A stream of ionised gas from the Sun, of mass density $\rho$ and speed $v$, flows towards the Earth.
Outside the Earth, the Earth's field is close to the field of a [[magnetic dipole|2KPTTBM584]].
Treat the gas as a perfect conductor that the magnetic field cannot penetrate.
Determine the surface that separates the stream from the cavity filled by the Earth's field.
Determine also the electric currents on that surface and the resulting field inside the cavity.
On the surface, the pressure of the stream must balance the magnetic pressure $B^2/(2\mu_0)$ of the confined field, where $\mu_0$ is the vacuum permeability.

## Remarks

The surface is now called the magnetopause, and the currents on it are the Chapman–Ferraro currents.
It is a free-boundary problem: the shape of the surface determines the field, and the field determines the shape.
A first estimate uses the subsolar point.
If the particles reflect specularly, the stream exerts a pressure $2\rho v^2$ there.
Let $B_0$ be the equatorial surface field and $R_E$ the Earth's radius.
Assume the boundary currents double the dipole field $B_0 (R_E/r)^3$ just inside the surface.
Then the balance $2\rho v^2 = (2 B_0 (R_E/r)^3)^2/(2\mu_0)$ gives the stand-off distance
$$\frac{r}{R_E} = \left( \frac{B_0^2}{\mu_0 \rho v^2} \right)^{1/6}.$$
For typical solar-wind values this gives about ten Earth radii, in line with observations.
The full shape of the surface has been computed numerically.
Modern models also include the magnetic field carried by the solar wind and the reconnection that lets some of it enter.
Chapman and Ferraro posed the problem in their work on magnetic storms from 1930 on, before the continuous solar wind was known.

## Explanations

### L1 human

The Sun blows a wind of charged particles, and the [[Earth's magnetic field|Z13HPJFV1F]] stands in its way.
The wind cannot cross the field lines, so it pushes them back and wraps around them, like a river around a rock.
The field is squeezed into a cavity shaped like a comet, blunt on the day side and long on the night side.
The Chapman–Ferraro problem asks for the shape of this cavity.
