---
tag: BDHTRF8RMF
kind: definition
name: Discrete dipole approximation
msc: [78A45, 78M99]
defines: V4H9V0EZRP
uses: [BANHMXD2TD, 8BQYB8H5CT, 743H0NT904]
sources:
  - url: https://en.wikipedia.org/wiki/Discrete_dipole_approximation
---

## Definition

Let a scatterer be illuminated by a time-harmonic incident electric field $E_{\mathrm{inc}}$ of angular frequency $\omega$.
Choose $N$ points $r_1, \dots, r_N$ that fill the scatterer, usually on a cubic lattice of spacing $d$ much smaller than the wavelength.
Give each point $r_j$ a polarizability $\alpha_j$, a complex $3 \times 3$ matrix or scalar.
For $j \ne l$, let $G_{jl}$ be a $3 \times 3$ matrix with the following property.
For each $p \in \C^3$, $G_{jl} p$ is the electric field at $r_j$ radiated by an oscillating [[electric dipole|BANHMXD2TD]] of moment $p$ at $r_l$.
The *discrete dipole approximation* takes the dipole moments $p_1, \dots, p_N \in \C^3$ to solve
$$p_j = \alpha_j \Big( E_{\mathrm{inc}}(r_j) + \sum_{l \ne j} G_{jl} \, p_l \Big), \qquad j = 1, \dots, N.$$
It takes the scattered field to be the sum of the fields radiated by these $N$ dipoles.

## Remarks

The system has $3N$ complex unknowns.
The polarizabilities are chosen so that the array mimics the material: a basic choice is the [[Clausius–Mossotti relation|743H0NT904]] with a small radiative correction.

Example: for $N = 1$, a small sphere is one dipole with $p_1 = \alpha_1 E_{\mathrm{inc}}(r_1)$, and the scattered field is the field of that dipole.
This recovers Rayleigh scattering by a small sphere.

Non-example: taking $p_j = \alpha_j E_{\mathrm{inc}}(r_j)$ for all $j$ when $N > 1$ drops the coupling terms $G_{jl} p_l$.
This is a first-order Born-type approximation, not the discrete dipole approximation.

The method converges to the exact solution as $d \to 0$ for fixed size and refractive index.
It needs $\abs{m} k d$ small, where $m$ is the refractive index of the material and $k$ the wavenumber in vacuum.
The large linear system is solved iteratively, with fast Fourier transforms for the lattice sums.
