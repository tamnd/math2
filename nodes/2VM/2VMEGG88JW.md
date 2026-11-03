---
tag: 2VMEGG88JW
kind: definition
name: Geophysical fluid dynamics
msc: [76U60, 86A05, 86A10]
defines: 2MNWD70JN3
uses: [F2JRWJNYN4, 18KXZHVF4M, SCYK4FMY59]
sources:
  - url: https://en.wikipedia.org/wiki/Geophysical_fluid_dynamics
---

## Definition

*Geophysical fluid dynamics* is the study of flows of fluids on a rotating planet, typically the atmosphere and the oceans.
The flows are described in a frame that rotates with the planet at angular velocity $\Omega$.
In this frame the [[Navier–Stokes|18KXZHVF4M]] momentum equation is
$$\frac{D u}{D t} + 2 \Omega \times u = -\frac{1}{\rho} \nabla p + g + \nu \Delta u.$$
Here $u$ is the velocity relative to the rotating frame, $\rho$ the density and $p$ the pressure.
Here $g$ is the effective gravity including the centrifugal force, and $\nu$ is the kinematic viscosity.
The subject concerns the regime where the Coriolis term $2 \Omega \times u$ and the buoyancy forces are of leading order.
This means a small or moderate [[Rossby number|SCYK4FMY59]] and a stable stratification.

## Remarks

On a sphere of latitude $\varphi$ the vertical component of $2 \Omega$ is the Coriolis parameter $f = 2 \abs{\Omega} \sin \varphi$, about $10^{-4}$ s$^{-1}$ at mid-latitudes on the Earth.

Example: a mid-latitude weather system with speed $U = 10$ m/s and size $L = 1000$ km has Rossby number $U / (f L) \approx 0.1$, so rotation dominates and it belongs to the subject.

Non-example: the flow of water out of a bathtub drain has $L$ of a few centimetres and Rossby number in the thousands.
The rotation of the Earth is negligible there, and it is not a geophysical flow in this sense.
