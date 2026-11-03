---
tag: DEBPQR1ZSH
kind: statement
role: theorem
name: Mie scattering
msc: [78A45, 35Q61]
uses: [8BQYB8H5CT, SW593EA0A2, NM024G378A, 9VGK0SP6EQ, CZCMRDWDYW, 3F32Y21HP4]
about: [8BQYB8H5CT]
sources:
  - url: https://en.wikipedia.org/wiki/Mie_scattering
same_as:
  wikidata: Q901737
  wikipedia: Mie scattering
---

## Statement

Let a homogeneous, isotropic, non-magnetic sphere of radius $a$ lie in a homogeneous non-magnetic medium, with complex [[refractive index|9VGK0SP6EQ]] $m$ relative to the medium.
Assume $\operatorname{Re} m > 0$ and $\operatorname{Im} m \ge 0$.
Let it be illuminated by a monochromatic [[plane wave|NM024G378A]] with wavenumber $k$ in the medium and time factor $e^{-i\omega t}$, and put $x = ka$.
Let $\psi_n(\rho) = \rho\, j_n(\rho)$ and $\xi_n(\rho) = \rho\, h_n^{(1)}(\rho)$ be the Riccati–Bessel functions built from the spherical Bessel function $j_n$ and the spherical Hankel function $h_n^{(1)}$.
Then the [[scattering problem|8BQYB8H5CT]] has a unique solution.
Its scattered field is a series over $n \ge 1$ of vector spherical wave functions with coefficients given by
$$a_n = \frac{m\, \psi_n(mx)\, \psi_n'(x) - \psi_n(x)\, \psi_n'(mx)}{m\, \psi_n(mx)\, \xi_n'(x) - \xi_n(x)\, \psi_n'(mx)}, \qquad b_n = \frac{\psi_n(mx)\, \psi_n'(x) - m\, \psi_n(x)\, \psi_n'(mx)}{\psi_n(mx)\, \xi_n'(x) - m\, \xi_n(x)\, \psi_n'(mx)}.$$
The scattering and extinction cross-sections are
$$C_{\mathrm{sca}} = \frac{2\pi}{k^2} \sum_{n=1}^{\infty} (2n + 1)\left( \abs{a_n}^2 + \abs{b_n}^2 \right), \qquad C_{\mathrm{ext}} = \frac{2\pi}{k^2} \sum_{n=1}^{\infty} (2n + 1) \operatorname{Re}(a_n + b_n).$$

## Remarks

The proof separates variables in spherical coordinates.
The incident plane wave is expanded in vector spherical wave functions built from [[spherical harmonics|3F32Y21HP4]] and spherical [[Bessel functions|CZCMRDWDYW]].
The internal field uses $j_n(mkr)$ and the scattered field uses $h_n^{(1)}(kr)$.
Continuity of the tangential components of $\mathbf{E}$ and $\mathbf{H}$ on the sphere gives, for each $n$, two decoupled pairs of linear equations whose solutions are $a_n$ and $b_n$.
The solution is named after Gustav Mie, who published it in 1908.
For $x \ll 1$ the leading coefficient $a_1$ dominates and the cross-section reduces to that of [[Rayleigh scattering|CVKPJ23EYR]].
For $x \gg 1$ and an absorbing or non-absorbing sphere, the extinction efficiency $C_{\mathrm{ext}}/(\pi a^2)$ tends to $2$, twice the geometric cross-section, the extinction paradox.
In practice the series is truncated after about $x + 4x^{1/3} + 2$ terms.

## Explanations

### L1 human

Mie scattering is the exact answer to a simple question: how does a ball of glass, water or metal scatter a light wave?
It works for spheres of any size, from much smaller than the wavelength to much larger.
It explains the white of clouds, the colours of the glory around an airplane's shadow, and the colours of gold nanoparticles in stained glass.

### L2 human

The solution is a model case of separation of variables for Maxwell's equations and a benchmark for numerical scattering codes.
Its coefficients $a_n$ and $b_n$ are the electric and magnetic multipole responses of the sphere; resonances in them give the ripple structure of the cross-sections.
Small spheres give Rayleigh scattering, and very large spheres approach geometrical optics with diffraction.
The same method extends to coated spheres and, via the T-matrix method, to non-spherical particles.
