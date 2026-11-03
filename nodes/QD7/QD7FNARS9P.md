---
tag: QD7FNARS9P
kind: definition
name: Thin-film interference
msc: [78A10, 78A40]
defines: K8VR0H7M9X
uses: [KX1EXRW47E, 9VGK0SP6EQ, AQ5ZKPZ88R, QDV9SBK6W0]
sources:
  - url: https://en.wikipedia.org/wiki/Thin-film_interference
---

## Definition

Let a film of thickness $d$ and [[refractive index|9VGK0SP6EQ]] $n_f$ lie between two media.
The medium on the incident side has index $n_1$, and the medium on the other side has index $n_2$.
Light of vacuum wavelength $\lambda$ falls on the film, and $\theta_t$ is the angle of the refracted ray in the film, given by [[Snell's law|QDV9SBK6W0]].
The waves reflected at the top and at the bottom of the film have the [[optical path length|AQ5ZKPZ88R]] difference
$$\Delta = 2 n_f d \cos \theta_t.$$
At normal incidence, a reflection off a medium of higher index adds a phase of $\pi$.
A reflection off a medium of lower index adds no phase.
*Thin-film interference* is the [[interference|KX1EXRW47E]] of these two reflected waves.
Their phase difference is $2\pi\Delta/\lambda$ plus the difference of the reflection phases.

## Remarks

If $n_f$ is larger than both $n_1$ and $n_2$, exactly one reflection adds $\pi$.
Then the reflection is strongest when $\Delta = (m + \tfrac12)\lambda$ and weakest when $\Delta = m\lambda$, for integers $m \ge 0$.
If $n_1 < n_f < n_2$, both reflections add $\pi$, and the two conditions are exchanged.
The two-beam picture neglects the waves reflected several times inside the film, which is accurate when the surfaces reflect weakly.

Example: a quarter-wave antireflection coating has $n_1 < n_f < n_2$ and $n_f d = \lambda / 4$.
At normal incidence $\Delta = \lambda/2$, so the two reflected waves are in opposite phase and the reflection is reduced.
It vanishes exactly when $n_f = \sqrt{n_1 n_2}$, because then the two reflected amplitudes are equal.

Non-example: a glass plate several millimetres thick, lit by sunlight, shows no colours.
Its path difference is much longer than the coherence length of sunlight, so the two reflected waves do not interfere.
