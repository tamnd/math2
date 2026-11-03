---
tag: WW2DTGE881
kind: statement
role: theorem
name: Stokes' law
msc: [76D07]
uses: [13CB7V2YM4, DF0M8YNQ3D, NM5Q4845Z4]
about: [13CB7V2YM4]
sources:
  - url: https://en.wikipedia.org/wiki/Stokes's_law
same_as:
  wikidata: Q824561
  wikipedia: Stokes's law
---

## Statement

Let a rigid sphere of radius $a > 0$ move with constant velocity $U \in \R^3$ through an unbounded fluid.
The fluid has dynamic [[viscosity|NM5Q4845Z4]] $\mu > 0$ and is at rest at infinity.
Assume that the fluid motion is a steady [[Stokes flow|13CB7V2YM4]] in the exterior of the sphere.
Assume that it satisfies the [[no-slip condition|DF0M8YNQ3D]] on the sphere and that its velocity tends to $0$ at infinity.
Then the force that the fluid exerts on the sphere is
$$F = -6 \pi \mu a U.$$

## Remarks

The proof writes the flow explicitly in the frame of the sphere.
It is the sum of a uniform stream, a Stokeslet and a potential dipole at the centre, with strengths chosen so that the velocity vanishes on the sphere.
Integrating the stress over the sphere gives the drag: one third, $2 \pi \mu a U$, comes from the pressure and two thirds, $4 \pi \mu a U$, from the viscous shear stress.
Example: a sphere of density $\rho_s$ settling under gravity $g$ in a fluid of density $\rho_f < \rho_s$ reaches the speed where drag balances weight minus buoyancy, $6 \pi \mu a V = \tfrac{4}{3} \pi a^3 (\rho_s - \rho_f) g$, so $V = \frac{2 (\rho_s - \rho_f) g a^2}{9 \mu}$.
In terms of the [[drag coefficient|NZ4E3K1J59]] based on the cross-section $\pi a^2$, the law reads $C_D = 24 / \mathrm{Re}$ with $\mathrm{Re} = 2 a \abs{U} \rho_f / \mu$.
The law describes real flows only when the [[Reynolds number|JH9EJ0HA0R]] is small; at larger values inertia adds to the drag, and Oseen's correction gives the next term.

## Explanations

### L1 human

A small ball moving slowly through a thick liquid feels a drag force proportional to its speed, its radius and the viscosity.
The constant in front is exactly $6 \pi$.
This is why fine dust and mist droplets fall so slowly: their weight shrinks like the cube of the radius, but the drag shrinks only like the radius.

### L2 human

Stokes' law is the classic exact result of [[Stokes flow|13CB7V2YM4]], and it calibrates many measurements: falling-ball viscometers and Millikan's oil-drop experiment both rely on it.
It is the leading term of the drag for small Reynolds numbers; the next correction comes from the [[Oseen equations|5632SYFZNF]].
The analogous problem in two dimensions, a cylinder, has no solution at all, which is [[Stokes' paradox|M1KHFRHCC1]].
Its linearity is behind the [[Lorentz reciprocal theorem|1GX3RJ9N14]] and the [[scallop theorem|8JZ39FW28G]].
