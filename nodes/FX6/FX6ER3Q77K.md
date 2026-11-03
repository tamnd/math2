---
tag: FX6ER3Q77K
kind: definition
name: Stellar pulsation
msc: [85A15, "76E20"]
defines: QW9QPV0HHG
uses: [4FC5XQA2RK, JVM27J1FTF, 3F32Y21HP4]
sources:
  - url: https://en.wikipedia.org/wiki/Stellar_pulsation
---

## Definition

Consider a spherically symmetric star in [[hydrostatic equilibrium|4FC5XQA2RK]], modelled as a self-gravitating fluid.
Linearise the equations of fluid motion, of gravity and of energy about this equilibrium.
A *pulsation mode* of the star is a [[normal mode|JVM27J1FTF]] of the linearised equations.
For a non-rotating star the radial component of its displacement field has the form
$$\xi_r(r, \theta, \phi, t) = \operatorname{Re}\big( \xi_{n\ell}(r) \, Y_\ell^m(\theta, \phi) \, e^{-i \omega t} \big).$$
Its horizontal components are proportional to the angular derivatives of $Y_\ell^m$.
Here $(r, \theta, \phi)$ are spherical coordinates and $Y_\ell^m$ is a [[spherical harmonic|3F32Y21HP4]].
The integer $n$ is the radial order, which counts the radial nodes of $\xi_{n\ell}$.
The number $\omega$ is the frequency.
*Stellar pulsation* is the oscillation of a star as a superposition of such modes.
The mode is *radial* if $\ell = 0$ and *non-radial* if $\ell \ge 1$.

## Remarks

For example, in a radial mode with $\ell = 0$ the star expands and contracts while staying spherical; the classical Cepheid variables pulsate in this way.
A non-example is a star whose light changes because of eclipses by a companion: there is no oscillation of the star about equilibrium.
Modes with pressure as the main restoring force are called p modes, and modes with buoyancy as the restoring force are called g modes.
In the adiabatic approximation the frequencies $\omega$ are real and the problem is a self-adjoint eigenvalue problem; non-adiabatic effects make $\omega$ complex and decide whether a mode grows or decays.
