---
tag: S1PZ23YAXQ
kind: statement
role: proposition
name: Jeans instability
msc: [85A30, "76E20", 85A15]
uses: [KCDJ1QXTEQ, SN4J6KP03C, RW0JK9VDZE, DWK5N5SKTK, R5P8M6SBG7]
about: [KCDJ1QXTEQ]
sources:
  - url: https://en.wikipedia.org/wiki/Jeans_instability
same_as:
  wikidata: Q1130216
  wikipedia: Jeans instability
---

## Statement

Consider an infinite, uniform, static gas of density $\rho_0 > 0$ with [[sound speed|SN4J6KP03C]] $c_s > 0$.
Let it obey the [[Euler equations|RW0JK9VDZE]] of a barotropic fluid and its own gravity through [[Poisson's equation|DWK5N5SKTK]], with gravitational constant $G$.
Assume, as in Jeans's treatment, that the unperturbed state is an equilibrium, ignoring the gravitational field of the uniform background.
Then small perturbations proportional to $e^{i(k \cdot x - \omega t)}$ satisfy the [[dispersion relation|R5P8M6SBG7]]
$$\omega^2 = c_s^2 \abs{k}^2 - 4\pi G \rho_0.$$
Hence a perturbation of wavelength $\lambda = 2\pi / \abs{k}$ grows exponentially if and only if $\lambda > \lambda_J$, where $\lambda_J = c_s \sqrt{\pi / (G \rho_0)}$ is the [[Jeans length|KCDJ1QXTEQ]].

## Remarks

Linearise the continuity equation, the momentum equation and Poisson's equation, and eliminate the velocity and the potential: the density perturbation $\rho_1$ satisfies $\partial_t^2 \rho_1 = c_s^2 \nabla^2 \rho_1 + 4\pi G \rho_0 \rho_1$.
A plane wave then gives the dispersion relation.
For $\abs{k} > k_J = \sqrt{4\pi G \rho_0}/c_s$, $\omega$ is real and the perturbation is a sound wave modified by gravity.
For $\abs{k} < k_J$, $\omega$ is imaginary and one solution grows like $e^{\abs{\omega} t}$.
The growth rate approaches $\sqrt{4\pi G \rho_0}$ for long waves.
Example: take a molecular cloud core at $10$ K with about $10^4$ hydrogen molecules per cubic centimetre.
Its Jeans length is about $0.2$ parsec, so larger regions tend to collapse.
The assumption about the background is not consistent, since a uniform static medium cannot be in equilibrium under its own gravity.
Consistent treatments confirm the conclusion, for example the [[Jeans instability in an expanding universe|SWR6C8DMAR]].

## Explanations

### L1 human

Gravity tries to pull a cloud of gas together, and pressure tries to push it apart.
For a small clump, pressure wins and the clump just oscillates like a sound wave.
For a large enough clump, gravity wins and the clump collapses.
The dividing size is the Jeans length, and it explains why stars form in big, cold, dense clouds.

### L2 human

The criterion compares the time a sound wave needs to cross a region with the time gravity needs to make it collapse, the [[free-fall time|5XFR43WNTN]].
The same dispersion relation, with a correction for rotation, gives the stability criteria for galactic disks.
The Jeans mass is, in one common convention, the mass inside a sphere of diameter $\lambda_J$.
It is the minimum mass that can collapse; it decreases as the density grows, which suggests fragmentation of collapsing clouds.
For a cloud of finite size bounded by external pressure, the corresponding threshold is the [[Bonnor–Ebert mass|MEFJ35FV3F]].
