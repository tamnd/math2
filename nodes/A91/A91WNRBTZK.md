---
tag: A91WNRBTZK
kind: definition
name: Density wave theory
msc: [85A05, 85A30]
defines: 9G3VNW5ZP0
uses: [GK34V4WF2V, FJR64ZRB4E, R5P8M6SBG7, DWK5N5SKTK]
sources:
  - url: https://en.wikipedia.org/wiki/Density_wave_theory
---

## Definition

Consider a thin, differentially rotating disc with surface density $\Sigma_0(R)$, angular velocity $\Omega(R)$ and sound speed $c_s(R)$.
Let $\kappa(R)$ be its [[epicyclic frequency|GK34V4WF2V]], and let gravity be given by [[Poisson's equation|DWK5N5SKTK]].
A *spiral density wave* is a small perturbation of the surface density of the form
$$\Sigma_1(R, \varphi, t) = \operatorname{Re}\left[ S(R) \, e^{i (m \varphi - \omega t + \Phi(R))} \right],$$
with $m \ge 1$ arms and pattern speed $\Omega_p = \omega / m$.
Its radial wavenumber $k = \Phi'(R)$ is assumed to satisfy $\abs{k} R \gg 1$ (tight winding).
In this limit the waves obey the [[dispersion relation|R5P8M6SBG7]] of Lin and Shu for a fluid disc,
$$(\omega - m \Omega)^2 = \kappa^2 - 2 \pi G \Sigma_0 \abs{k} + c_s^2 k^2.$$
*Density wave theory* is the hypothesis that the spiral arms of disc galaxies are such waves, quasi-stationary in a frame rotating with $\Omega_p$.

## Remarks

Example: at corotation $\omega = m \Omega$ the left side vanishes, and the relation reads $\kappa^2 - 2 \pi G \Sigma_0 \abs{k} + c_s^2 k^2 = 0$.
At a [[Lindblad resonance|FJR64ZRB4E]] the left side equals $\kappa^2$, so the relation gives $k = 0$ or $\abs{k} = 2 \pi G \Sigma_0 / c_s^2$.
Waves propagate in the region between the inner and outer Lindblad resonances, apart from a zone around corotation where $k$ can be complex.

Non-example: a material arm made of a fixed set of stars has the angular velocity of those stars, which depends on $R$.
Its pitch angle shrinks with time, so it is not a pattern with a single pattern speed.

For a stellar disc, the term $c_s^2 k^2$ is replaced by a reduction factor that depends on the velocity dispersion of the stars.
