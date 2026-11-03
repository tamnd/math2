---
tag: Q6XWE6DKXA
kind: definition
name: Fermi acceleration
msc: [85A30, 76X05, 82D10]
defines: T0N4CTZERC
uses: [JSDMGGTG7G, 04VZE3FZXF]
sources:
  - url: https://en.wikipedia.org/wiki/Fermi_acceleration
---

## Definition

Let charged particles move in a plasma that contains magnetic irregularities moving with speeds much smaller than the speed of light $c$.
*Fermi acceleration* is the process in which a particle gains energy by many elastic reflections off these moving irregularities, as follows.

1. In the frame of each irregularity the reflection keeps the particle energy unchanged.
2. Because the irregularities move, the reflection changes the energy $E$ in the frame of the plasma.
   The mean relative gain per cycle of reflections is positive.
3. The particle performs a [[random walk|04VZE3FZXF]] of such cycles and escapes from the accelerating region after a random number of cycles.

It is of *second order* when the irregularities are clouds moving in random directions with speed $V$.
For relativistic particles with isotropic directions, the mean gain per collision is then $\langle \Delta E / E \rangle = \frac{8}{3} (V/c)^2$.
It is of *first order*, or *diffusive shock acceleration*, when the particles cross a [[shock wave|JSDMGGTG7G]] back and forth.
Let $u_1$ and $u_2 < u_1$ be the upstream and downstream flow speeds in the shock frame.
The mean gain per round trip across the shock is then $\langle \Delta E / E \rangle = \frac{4}{3} (u_1 - u_2)/c$.

## Remarks

Assume that each cycle multiplies the energy by a constant $\beta > 1$ and that the particle stays for the next cycle with probability $P < 1$.
After $k$ cycles a particle has energy $E_0 \beta^k$, and a fraction $P^k$ of the particles reach it.
Eliminating $k$ gives the integral spectrum
$$N(\ge E) \propto \left( \frac{E}{E_0} \right)^{\ln P / \ln \beta},$$
a power law.
For a strong shock in a monatomic gas the compression ratio is $u_1/u_2 = 4$, and the differential spectrum is $N(E) \, dE \propto E^{-2} \, dE$, independent of the details of the scattering.

Example: let a fast particle be reflected head-on by a magnetic mirror that moves toward it with speed $V$.
By the Lorentz transformation into and out of the mirror frame, it gains energy, as in clause 2.

Non-example: reflections off magnetic structures at rest in the plasma frame satisfy clause 1 but give no change of energy, so they fail clause 2 and produce no acceleration.
