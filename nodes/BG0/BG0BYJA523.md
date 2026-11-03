---
tag: BG0BYJA523
kind: definition
name: Laughlin wavefunction
msc: [81V70, 81V27]
defines: 6YFHETS0B8
uses: [11AZ4RGXVN]
sources:
  - url: https://en.wikipedia.org/wiki/Laughlin_wavefunction
---

## Definition

Consider $N$ electrons in the plane in a perpendicular magnetic field, and measure lengths in units of the magnetic length $\ell_B = \sqrt{\hbar/(eB)}$.
Write the position of electron $j$ as the complex number $z_j = x_j + i y_j$.
Choose the orientation so that lowest Landau level states are $f(z) e^{-\abs{z}^2/4}$ with $f$ analytic.
For an odd integer $m \ge 1$, the *Laughlin wavefunction* is
$$\Psi_m(z_1, \dots, z_N) = \prod_{1 \le i < j \le N} (z_i - z_j)^m \, \exp\Big(-\frac14 \sum_{j=1}^{N} \abs{z_j}^2\Big).$$
It describes the [[quantum Hall|11AZ4RGXVN]] state at filling fraction $\nu = 1/m$.

## Remarks

The function is antisymmetric: exchanging $z_i$ and $z_j$ multiplies $(z_i - z_j)^m$ by $(-1)^m = -1$ and permutes the other factors.
It lies in the lowest Landau level, since its prefactor is a polynomial in the $z_j$.
The modulus squared $\abs{\Psi_m}^2$ is the Boltzmann weight of a two-dimensional one-component plasma, which shows that the state is a uniform liquid of density $1/(2\pi m)$ in these units.

Example: for $m = 1$, $\prod_{i<j}(z_i - z_j)$ is, up to sign, the Vandermonde determinant $\det(z_i^{j-1})$, so $\Psi_1$ is the Slater determinant of the orbitals $z^k e^{-\abs{z}^2/4}$, $0 \le k \le N - 1$: the filled lowest Landau level, $\nu = 1$.

Non-example: for $m = 2$ the same formula is symmetric under exchange, so it is not an admissible state of electrons, which are fermions; it describes bosons at $\nu = 1/2$.
