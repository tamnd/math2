---
tag: EJD5X520CQ
kind: definition
name: Beam propagation method
msc: [78A40, 78M20, 65M06]
defines: 21TRP92AWH
uses: [MNXKTXJ35G, 53DCTAEM5M, 9VGK0SP6EQ, DPVM34ADZV, S966EZX3ZT]
sources:
  - url: https://en.wikipedia.org/wiki/Beam_propagation_method
---

## Definition

Let $n(x, y, z) > 0$ be a [[refractive index|9VGK0SP6EQ]], let $k_0 > 0$ be the vacuum wave number, and let $\bar{n} > 0$ be a reference index.
A scalar field $\psi$ solves the [[Helmholtz equation|MNXKTXJ35G]] $\nabla^2 \psi + k_0^2 n^2 \psi = 0$.
Write $\psi = u \, e^{i \beta z}$ with $\beta = k_0 \bar{n}$, and drop the term $\partial_z^2 u$, which is small for a slowly varying envelope $u$.
This gives the [[paraxial wave equation|53DCTAEM5M]]
$$\partial_z u = \frac{i}{2\beta} \nabla_\perp^2 u + \frac{i k_0 (n^2 - \bar{n}^2)}{2 \bar{n}} u, \qquad \nabla_\perp^2 = \partial_x^2 + \partial_y^2.$$
The *beam propagation method* is the numerical solution of this equation as an evolution problem in $z$.
It starts from a given input field $u(x, y, 0)$ and computes $u$ on the planes $z = m \Delta z$, $m = 1, 2, \dots$, one step at a time.

## Remarks

Example: let $V = k_0 (n^2 - \bar{n}^2)/(2 \bar{n})$ on the plane $z$.
The split-step Fourier version takes the step
$$u(z + \Delta z) = \mathcal{F}^{-1}\left[ e^{-i (k_x^2 + k_y^2) \Delta z / (2 \beta)} \, \mathcal{F}\left[ e^{i V \Delta z} u(z) \right] \right],$$
where $\mathcal{F}$ is the [[Fourier transform|DPVM34ADZV]] in $(x, y)$, computed by the [[fast Fourier transform|S966EZX3ZT]].
Check: if $n = \bar{n}$ everywhere, then $V = 0$, and each Fourier mode $e^{i(k_x x + k_y y)}$ solves the equation with the factor $e^{-i(k_x^2 + k_y^2) z / (2\beta)}$; so the step is exact.
In general the error of the step comes from splitting the two terms, which do not commute.

Non-example: a structure with an abrupt end facet reflects part of the light backwards.
The method drops $\partial_z^2 u$ and so keeps only forward waves; it cannot compute the reflected wave.

Wide-angle versions replace the paraxial operator by better rational approximations, such as Padé approximants, of the one-way operator $\sqrt{\nabla_\perp^2 + k_0^2 n^2}$.

## Explanations

### L1 human

The method turns a hard problem in three dimensions into many easy problems in two.
It assumes the light goes forward, and it advances the beam across the structure one thin slice at a time.
In each slice, diffraction spreads the beam and the refractive index bends it.
