---
tag: HFHE56NYH1
kind: definition
name: Taylor–Couette instability
msc: ["76E07"]
defines: 2A3F7MSEMH
uses: [18KXZHVF4M, H028A17Z55, JH9EJ0HA0R]
sources:
  - url: https://en.wikipedia.org/wiki/Taylor–Couette_flow
---

## Definition

Consider a viscous incompressible fluid with kinematic viscosity $\nu > 0$ in the gap $R_1 < r < R_2$ between two coaxial cylinders, in cylindrical coordinates $(r, \theta, z)$.
The inner cylinder rotates at angular velocity $\Omega_1$ and the outer one at $\Omega_2$.
The [[Navier–Stokes equations|18KXZHVF4M]] with no-slip conditions have the steady solution called circular Couette flow, with azimuthal velocity
$$v(r) = A r + \frac{B}{r}, \qquad A = \frac{\Omega_2 R_2^2 - \Omega_1 R_1^2}{R_2^2 - R_1^2}, \qquad B = \frac{(\Omega_1 - \Omega_2) R_1^2 R_2^2}{R_2^2 - R_1^2}.$$
The *Taylor–Couette instability* is the loss of stability of circular Couette flow as $\Omega_1$ increases past a critical value.
This value depends on $\nu$, $\Omega_2$, $R_1$ and $R_2$.
Beyond this value the flow is unstable to axisymmetric disturbances.
A new steady flow appears, the Taylor vortex flow, made of toroidal vortices periodic in $z$.

## Remarks

For an inviscid fluid, Rayleigh's circulation criterion says that a rotating flow $v(r)$ is stable to axisymmetric disturbances exactly when $(r v)^2$ does not decrease with $r$.
For circular Couette flow with $\Omega_2 = 0$ and $\Omega_1 > 0$, the quantity $r v$ decreases from $R_1^2 \Omega_1$ to $0$ across the gap.
So the inviscid flow is unstable, and viscosity delays the instability to a finite critical rotation rate.
The threshold is usually expressed by a Taylor number or a [[Reynolds number|JH9EJ0HA0R]] $\Omega_1 R_1 (R_2 - R_1) / \nu$ based on the gap width.

Example: with the outer cylinder at rest, there is a critical inner rotation rate beyond which Taylor vortices appear, and Taylor's linear theory predicted it in agreement with his experiments.
Non-example: with the inner cylinder at rest and the outer cylinder rotating, $\Omega_1 = 0 < \Omega_2$, the quantity $(r v)^2$ increases outward.
So the flow satisfies Rayleigh's criterion, and there is no centrifugal instability of this kind.
