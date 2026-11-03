---
tag: XNFPYQM7XX
kind: definition
name: Hartmann number
msc: [76W05, 76M55]
defines: ZP0MJ10VXV
uses: [T8JWCBK9M6, T3R5FWV91P, NM5Q4845Z4]
sources:
  - url: https://en.wikipedia.org/wiki/Hartmann_number
---

## Definition

Consider a flow in [[magnetohydrodynamics|T8JWCBK9M6]] of a fluid with electrical conductivity $\sigma$, dynamic [[viscosity|NM5Q4845Z4]] $\mu$, density $\rho$ and kinematic viscosity $\nu = \mu / \rho$.
Let $B_0$ be a characteristic magnetic field strength and $L$ a characteristic length.
The *Hartmann number* is
$$\mathrm{Ha} = B_0 L \sqrt{\frac{\sigma}{\mu}} = B_0 L \sqrt{\frac{\sigma}{\rho \nu}}.$$

## Remarks

It is a [[dimensionless number|T3R5FWV91P]]: $\sigma B_0^2$ has the units of a force per volume per speed, as does $\mu / L^2$, so $\mathrm{Ha}^2 = \sigma B_0^2 L^2 / \mu$ has no units.
Example, Hartmann flow: a fluid driven by a constant pressure gradient between the planes $y = \pm L$, in a transverse field $B_0 \mathbf{e}_y$.
In the limit of small magnetic Reynolds number, its velocity profile is proportional to $\cosh(\mathrm{Ha}) - \cosh(\mathrm{Ha} \, y / L)$.
For large $\mathrm{Ha}$ this is flat in the middle and drops to $0$ in layers of thickness about $L / \mathrm{Ha}$ near the walls.
For $\mathrm{Ha} \to 0$ the profile becomes the parabola of plane Poiseuille flow.
Non-example: $\sigma B_0^2 L / (\rho U)$ is the Stuart number, or interaction parameter, which compares the Lorentz force with inertia, not with viscosity; it equals $\mathrm{Ha}^2 / \mathrm{Re}$.
