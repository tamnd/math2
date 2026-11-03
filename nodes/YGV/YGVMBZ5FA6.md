---
tag: YGVMBZ5FA6
kind: definition
name: Thermodynamic limit
msc: [82B05, 82B03, 82B20]
defines: FPYQWE8X12
uses: [G1P1A0N7NZ]
sources:
  - url: https://en.wikipedia.org/wiki/Thermodynamic_limit
---

## Definition

Let $\Lambda_L = \set{1, \dots, L}^d \subset \Z^d$ for $L \ge 1$, or let $\Lambda_L = [0, L]^d \subset \R^d$ for a continuum system.
Write $\abs{\Lambda_L}$ for the number of sites, or for the volume.
Suppose that for each $L$ a system is given in $\Lambda_L$, with $N_L$ particles where $N_L / \abs{\Lambda_L} \to \rho$ for a fixed density $\rho$.
Let $A_L$ be a real quantity of the system in $\Lambda_L$.
The quantity has a *thermodynamic limit* $a$ if
$$\lim_{L \to \infty} \frac{A_L}{\abs{\Lambda_L}} = a.$$
Taking this limit is called passing to the thermodynamic limit.

## Remarks

The main example is $A_L = \ln Z_L$, with $Z_L$ the [[canonical|G1P1A0N7NZ]] or grand canonical partition function; the limit is the free energy or the pressure per unit volume, up to a factor.
Example: $L^d$ independent spins $\sigma_i = \pm 1$ in a field $h$ have $Z_L = (2 \cosh \beta h)^{L^d}$.
So $\ln Z_L / L^d = \ln (2 \cosh \beta h)$ for every $L$, and the limit exists.
Non-example: for a system of $N$ particles in which every pair attracts with the same energy $-J < 0$, the energy of the ground state is $-J N (N - 1) / 2$.
This grows like $N^2$, so the energy per volume has no finite thermodynamic limit at fixed density.
More general sequences of regions, the van Hove sequences, are often allowed; they grow in all directions so that the boundary is small compared with the volume.
