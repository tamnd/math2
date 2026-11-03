---
tag: GXV36FWN8F
kind: definition
name: Elastic wave scattering
msc: [74J20, 74B05, 35P25]
defines: YRYPCEDBN2
uses: [80737NDZ4V, EEPJJHC5JZ, GZ7E9GHQYB, MNXKTXJ35G]
sources:
  - url: https://en.wikipedia.org/wiki/Seismic_wave
---

## Definition

Let $\R^3$ be filled with a homogeneous isotropic linear elastic medium with [[Lamé parameters|80737NDZ4V]] $\lambda, \mu > 0$ and density $\rho > 0$.
Let $D \subset \R^3$ be a bounded domain with smooth boundary such that $\R^3 \setminus \overline{D}$ is connected, and let $\omega > 0$ be a frequency.
Put $c_p = \sqrt{(\lambda + 2\mu)/\rho}$, $c_s = \sqrt{\mu/\rho}$, $k_p = \omega / c_p$ and $k_s = \omega / c_s$.
Let $u^{\mathrm{in}}$ be an incident displacement field that solves the time-harmonic Navier equation
$$\mu \Delta u + (\lambda + \mu) \nabla (\nabla \cdot u) + \rho \omega^2 u = 0$$
in all of $\R^3$, for example a plane [[P-wave|EEPJJHC5JZ]] or [[S-wave|GZ7E9GHQYB]].
The *scattering problem* for the rigid obstacle $D$ asks for a scattered field $u^{\mathrm{sc}}$ such that:

1. $u^{\mathrm{sc}}$ solves the Navier equation in $\R^3 \setminus \overline{D}$.
2. The total field $u = u^{\mathrm{in}} + u^{\mathrm{sc}}$ vanishes on $\partial D$.
3. The parts $u_p = -k_p^{-2} \nabla (\nabla \cdot u^{\mathrm{sc}})$ and $u_s = u^{\mathrm{sc}} - u_p$ satisfy the Kupradze radiation condition $r (\partial_r u_p - i k_p u_p) \to 0$ and $r (\partial_r u_s - i k_s u_s) \to 0$ as $r = \abs{x} \to \infty$, uniformly in the direction.

## Remarks

Other scatterers change only clause 2.
A cavity requires the traction of $u$ on $\partial D$ to vanish, and a penetrable inclusion with other constants requires continuity of displacement and traction across $\partial D$.
The field $u_p$ is curl-free and solves the [[Helmholtz equation|MNXKTXJ35G]] with wavenumber $k_p$, and $u_s$ is divergence-free and solves it with wavenumber $k_s$.

Example: if the incident field is zero, then $u^{\mathrm{sc}} = 0$ satisfies all three clauses.

Non-example: $u^{\mathrm{sc}} = -u^{\mathrm{in}}$ for a plane wave $u^{\mathrm{in}}$ satisfies clauses 1 and 2, but fails clause 3, since a plane wave does not decay like an outgoing spherical wave.

Far from $D$ the scattered field behaves like $e^{i k_p r}/r$ times a vector pattern plus $e^{i k_s r}/r$ times another, and these two far-field patterns are the data of inverse scattering.
