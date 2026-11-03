---
tag: HFN7D2CZM0
kind: definition
name: Thomson scattering
msc: [78A45, 78A40]
defines: Z7BN231HNA
uses: [8BQYB8H5CT, S3RZRCH0T5, EHYKJXF899, NM024G378A]
sources:
  - url: https://en.wikipedia.org/wiki/Thomson_scattering
---

## Definition

Let a free particle of charge $q$ and mass $m$ be at rest in vacuum.
Let a monochromatic [[plane wave|NM024G378A]] of angular frequency $\omega$ fall on it, with $\hbar \omega \ll m c^2$ and with field amplitude small enough that the particle stays non-relativistic.
*Thomson scattering* is the scattering in which:

1. the particle moves by the [[Lorentz force|S3RZRCH0T5]] of the incident electric field, $m \ddot{x} = q E(t)$, with the magnetic force and the radiation reaction neglected;
2. the accelerated particle radiates by the [[Larmor formula|EHYKJXF899]];
3. the radiated wave has the same frequency $\omega$ as the incident wave.

## Remarks

Let $r_q = \dfrac{q^2}{4\pi\varepsilon_0 m c^2}$, the classical radius of the particle.
For a linearly polarized incident wave, the differential cross-section is $\dfrac{d\sigma}{d\Omega} = r_q^2 \sin^2 \chi$, where $\chi$ is the angle between the incident electric field and the direction of observation.
For unpolarized light, it is $\dfrac{d\sigma}{d\Omega} = r_q^2 \dfrac{1 + \cos^2\theta}{2}$, where $\theta$ is the scattering angle.
The total cross-section is the Thomson cross-section $\sigma_T = \dfrac{8\pi}{3} r_q^2$.

Example: for an electron, $r_e \approx 2.82 \times 10^{-15}$ m and $\sigma_T \approx 6.65 \times 10^{-29}$ m$^2$.
Check: $\frac{8\pi}{3} (2.82 \times 10^{-15})^2 \approx 8.38 \times 2.82^2 \times 10^{-30} \approx 6.66 \times 10^{-29}$.

Non-example: X-rays or gamma rays with $\hbar \omega$ comparable to $m_e c^2$ on electrons.
Clause 3 fails: the photon loses energy to the recoiling electron, and the process is Compton scattering, with the Klein–Nishina cross-section in place of $\sigma_T$.
