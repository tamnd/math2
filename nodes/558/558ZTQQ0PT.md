---
tag: 558ZTQQ0PT
kind: definition
name: Rayleigh scattering
msc: [78A45, 78A40]
defines: CVKPJ23EYR
uses: [8BQYB8H5CT, SW593EA0A2, BANHMXD2TD, F768YN0P2V]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh_scattering
---

## Definition

Let a homogeneous sphere of radius $a$ lie in a homogeneous medium, with [[permittivity|F768YN0P2V]] $\varepsilon_r$ relative to the medium.
Let it be illuminated by a monochromatic plane wave of wavenumber $k = 2\pi/\lambda$ in the medium.
*Rayleigh scattering* is the [[electromagnetic scattering|8BQYB8H5CT]] in the regime $ka \ll 1$ and $\abs{\varepsilon_r}^{1/2} ka \ll 1$, where the sphere is treated as an induced point [[electric dipole|BANHMXD2TD]].
In this regime the scattering cross-section is
$$C_{\mathrm{sca}} = \frac{8\pi}{3} k^4 a^6 \left| \frac{\varepsilon_r - 1}{\varepsilon_r + 2} \right|^2 .$$

## Remarks

Check: a sphere in a uniform field $\mathbf{E}_0$ gets the dipole moment $\mathbf{p} = 4\pi\varepsilon a^3 \dfrac{\varepsilon_r - 1}{\varepsilon_r + 2} \mathbf{E}_0$, where $\varepsilon$ is the permittivity of the surrounding medium.
An oscillating dipole radiates power $\dfrac{c k^4 \abs{\mathbf{p}}^2}{12\pi\varepsilon}$ with $c$ the speed of light in the medium, and dividing by the incident intensity $\frac{1}{2} c\, \varepsilon \abs{\mathbf{E}_0}^2$ gives the formula above.
For unpolarized incident light the scattered intensity varies with the scattering angle $\theta$ as $1 + \cos^2\theta$, and at $\theta = 90^\circ$ the scattered light is fully polarized.
Example: for blue light at $450$ nm and red light at $700$ nm, the ratio of cross-sections is $(700/450)^4 \approx 5.9$.
Non-example: cloud droplets have radii of several micrometres, so $ka$ is much larger than $1$.
Their scattering is described by the [[Mie solution|DEBPQR1ZSH]] instead.
It depends only weakly on wavelength, which is why clouds are white.
