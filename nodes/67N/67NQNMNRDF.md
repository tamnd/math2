---
tag: 67NQNMNRDF
kind: definition
name: Speed of sound
msc: [76N15, 76Q05]
defines: SN4J6KP03C
uses: [5EHD2XBQDG, RW0JK9VDZE]
sources:
  - url: https://en.wikipedia.org/wiki/Speed_of_sound
---

## Definition

Let a fluid have an equation of state $p = p(\rho, s)$.
It gives the pressure $p$ in terms of the density $\rho > 0$ and the specific entropy $s$, with $\partial p / \partial \rho > 0$.
The *speed of sound* in the state $(\rho, s)$ is the number $c > 0$ with
$$c^2 = \left(\frac{\partial p}{\partial \rho}\right)_{s}.$$
So $c^2$ is the derivative of the pressure with respect to the density at constant entropy.

## Remarks

Linearise the compressible [[Euler equations|RW0JK9VDZE]] about a fluid at rest with uniform density $\rho_0$.
Then small perturbations $p'$ of the pressure solve the [[wave equation|5EHD2XBQDG]] $\partial_t^2 p' = c^2 \Delta p'$, so they travel at speed $c$.
Example: for an ideal gas with constant ratio of specific heats $\gamma$, isentropic changes satisfy $p = K \rho^\gamma$, so $c^2 = \gamma p / \rho = \gamma R T$, with $R$ the specific gas constant and $T$ the temperature.
For air, $\gamma = 1.4$ and $R \approx 287\ \mathrm{J/(kg\,K)}$, and at $T = 293\ \mathrm{K}$ this gives $c \approx 343\ \mathrm{m/s}$.
Non-example: Newton's value $\sqrt{(\partial p / \partial \rho)_T} = \sqrt{p / \rho} \approx 290\ \mathrm{m/s}$ uses the derivative at constant temperature instead of constant entropy.
It is too low, because sound waves are too fast for heat to flow between compressed and expanded regions.
