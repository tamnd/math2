---
tag: 7J2GMYHYVD
kind: definition
name: Superfluidity
msc: [82D50, 76Y05]
defines: 4PZBRJ78X4
uses: [F5EAWFMC8A, EPZR6H2WJN]
sources:
  - url: https://en.wikipedia.org/wiki/Superfluidity
---

## Definition

Consider a homogeneous quantum fluid of particles of mass $m$ at zero temperature.
Assume that its elementary excitations of momentum $\mathbf{p}$ have energy $\varepsilon(\abs{\mathbf{p}}) > 0$.
Its *Landau critical velocity* is
$$v_c = \inf_{p > 0} \frac{\varepsilon(p)}{p}.$$
The fluid is *superfluid* if $v_c > 0$.
Then, by Landau's criterion, the fluid can flow past a wall at any relative speed $v < v_c$ without creating excitations.
That is, it flows without viscous dissipation.

## Remarks

The argument: let the fluid flow with velocity $\mathbf{v}$ relative to a wall.
An excitation of momentum $\mathbf{p}$, measured in the fluid frame, has energy $\varepsilon(p) + \mathbf{p} \cdot \mathbf{v}$ in the wall frame.
It can appear spontaneously only if this energy is negative, which requires $\abs{\mathbf{v}} > \varepsilon(p)/p$.
Example: for the weakly interacting Bose gas of [[Gross–Pitaevskii|F5EAWFMC8A]] theory, the Bogoliubov spectrum is $\varepsilon(p) = \sqrt{c^2 p^2 + (p^2 / 2m)^2}$ with sound speed $c > 0$; then $\varepsilon(p)/p = \sqrt{c^2 + p^2/(4m^2)} \ge c$, so $v_c = c > 0$.
Non-example: for the ideal Bose gas, $\varepsilon(p) = p^2 / 2m$, so $\varepsilon(p)/p = p/(2m) \to 0$ and $v_c = 0$; it has a condensate but is not superfluid.
In the hydrodynamic description, the superfluid is described by a wave function $\psi = \sqrt{n} \, e^{i\theta}$ and has velocity $\mathbf{v}_s = (\hbar / m) \nabla \theta$, where $\hbar$ is the reduced Planck constant.
At positive temperature the two-fluid model splits the fluid into a superfluid part and a normal viscous part.
In helium-4 the observed critical speeds are usually much lower than Landau's value, because vortices are created first.
