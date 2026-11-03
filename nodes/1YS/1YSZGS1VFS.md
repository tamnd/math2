---
tag: 1YSZGS1VFS
kind: definition
name: Halo mass function
msc: [85A40]
defines: 6K40RAVSAT
uses: [EC34EJYV16, FWRHZ27J6Q]
sources:
  - url: https://en.wikipedia.org/wiki/Halo_mass_function
---

## Definition

Consider a universe that is statistically homogeneous on large scales.
Assume that its dark matter halos have been identified and assigned masses by a fixed convention, such as the [[virial mass|EC34EJYV16]].
The *halo mass function* at redshift $z$ is the function $n(M, z) \ge 0$ such that the comoving number density of halos with mass in $[M, M + dM]$ is $n(M, z) \, dM$.
It is also written $dn/dM$.

## Remarks

Often one uses $dn/d\ln M = M \, n(M, z)$ instead.
Many models write it in the form
$$n(M, z) = f(\sigma) \, \frac{\bar\rho}{M} \, \abs{\frac{d \ln \sigma}{dM}} .$$
Here $\bar\rho$ is the mean comoving matter density and $f$ is a function to be modelled or fitted.
The quantity $\sigma = \sigma(M, z)$ is the standard deviation of the linear density field smoothed on the mass scale $M$.
It is computed from the [[matter power spectrum|FWRHZ27J6Q]].

Example: the Press–Schechter formalism gives $f(\sigma) = \sqrt{2/\pi} \, (\delta_c/\sigma) \, e^{-\delta_c^2/(2\sigma^2)}$ with $\delta_c \approx 1.686$; this $f$ is positive and integrable, and $\int n(M, z) \, M \, dM = \bar\rho$ for it.

Non-example: the galaxy luminosity function counts galaxies per unit volume and per unit luminosity.
It counts different objects by a different quantity, so it is not a halo mass function, even if the two are related through models of galaxy formation.

The value of $n$ depends on the halo mass convention.
For example, the mass within the radius where the mean density is $200$ times the critical density differs from the virial mass.
