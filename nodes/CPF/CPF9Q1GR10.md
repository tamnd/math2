---
tag: CPF9Q1GR10
kind: example
name: Electric field integral equation
msc: [78A45, 78M15, 45A05]
instance_of: [ZDS77Q0F06]
sources:
  - url: https://en.wikipedia.org/wiki/Electric-field_integral_equation
same_as:
  wikidata: Q5357276
  wikipedia: Electric-field integral equation
---

## Example

Let $S$ be the smooth closed surface of a perfectly conducting body in $\R^3$, with outward unit normal $n$.
Let a time-harmonic incident field $E^{\mathrm{inc}}$ with time factor $e^{-i\omega t}$ illuminate the body in a medium with permittivity $\varepsilon$ and permeability $\mu$, and let $k = \omega \sqrt{\varepsilon \mu}$.
Let $G(x, y) = \frac{e^{ik\abs{x - y}}}{4\pi \abs{x - y}}$.
The unknown is the tangential surface current density $J$ on $S$.
The electric field integral equation is
$$n(x) \times E^{\mathrm{inc}}(x) = -i\omega\mu \, n(x) \times \left[\int_S G(x, y) J(y) \, dS(y) + \frac{1}{k^2} \nabla_x \int_S G(x, y) \, (\nabla_S \cdot J)(y) \, dS(y)\right], \quad x \in S.$$
The unknown $J$ appears only under the integrals, so it is an [[integral equation of the first kind|ZDS77Q0F06]].

Check: the current $J$ radiates the scattered field $E^{\mathrm{s}} = i\omega A - \nabla \Phi$.
Here $A = \mu \int_S G J \, dS$ is the vector potential and $\Phi = \frac{1}{\varepsilon} \int_S G \sigma \, dS$ the scalar potential.
The charge density is $\sigma = \frac{1}{i\omega} \nabla_S \cdot J$ by the continuity equation.
Since $\frac{1}{i\omega\varepsilon} = \frac{-i\omega\mu}{k^2}$, this gives $E^{\mathrm{s}} = i\omega\mu \left[\int_S G J \, dS + \frac{1}{k^2} \nabla \int_S G \, \nabla_S \cdot J \, dS\right]$.
On a perfect conductor the tangential total field vanishes, $n \times (E^{\mathrm{inc}} + E^{\mathrm{s}}) = 0$ on $S$, which is the equation above.

## Remarks

The equation is uniquely solvable except at the countably many wavenumbers $k$ at which the interior of $S$ has a nonzero cavity resonance field.
Near these wavenumbers numerical solutions become unstable; combining it with the magnetic field integral equation removes the problem.
Discretized with the method of moments, it is a standard tool for computing radar scattering and antenna fields.

## Explanations

### L1 human

When a radio wave hits a metal object, it drives electric currents on the surface, and these currents send out the reflected wave.
On metal the total electric field along the surface must be zero.
This condition gives an equation for the unknown surface currents, in which each current element contributes through an integral over the whole surface.
