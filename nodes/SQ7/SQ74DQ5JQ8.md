---
tag: SQ74DQ5JQ8
kind: definition
name: Energy cascade
msc: [76F05, 76F02]
defines: YQ2KYDWRD0
uses: [VY307F8Z0S, 18KXZHVF4M, NM5Q4845Z4, NYRS1BJKRQ]
sources:
  - url: https://en.wikipedia.org/wiki/Energy_cascade
---

## Definition

Consider statistically stationary, homogeneous [[turbulence|VY307F8Z0S]] in three dimensions, governed by the incompressible [[Navier–Stokes equations|18KXZHVF4M]].
Let $\nu$ be the kinematic [[viscosity|NM5Q4845Z4]], and let a force act at wavenumbers near $k_f$.
Let $\varepsilon$ be the mean rate of energy dissipation per unit mass.
For a wavenumber $k$, let $\Pi(k)$ be the mean rate of nonlinear energy transfer from modes with $\abs{\mathbf{k}} < k$ to modes with $\abs{\mathbf{k}} > k$.
Let $\eta$ be the [[Kolmogorov length|NYRS1BJKRQ]].
The flow has a (direct) *energy cascade* when, at high Reynolds number, $\Pi(k) \approx \varepsilon$ on a range $k_f \ll k \ll 1/\eta$, called the inertial range.

## Remarks

The nonlinear term conserves total kinetic energy, so it only moves energy between scales; the force injects energy at large scales and viscosity removes it mainly at scales near $\eta$.
In a stationary state the flux through each scale of the inertial range must therefore equal the dissipation rate.
The dimensional estimate $\varepsilon \sim u^3 / L$, with $u$ and $L$ the speed and size of the large eddies, is independent of $\nu$; this is the observed dissipation anomaly.

Example: in homogeneous isotropic turbulence the flux is positive and constant across the inertial range, and the energy spectrum there follows the Kolmogorov law $E(k) \propto \varepsilon^{2/3} k^{-5/3}$.
Non-example: in two-dimensional turbulence, enstrophy is also conserved by the nonlinear term.
There energy goes mainly to larger scales, an inverse cascade, while enstrophy cascades to smaller scales, and $\Pi(k)$ is negative in the energy inertial range.
