---
tag: SDR8DZ25E9
kind: example
name: Fabry–Pérot interferometer
msc: [78A10, 78A40]
instance_of: [KX1EXRW47E]
uses: [AQ5ZKPZ88R, 9VGK0SP6EQ]
sources:
  - url: https://en.wikipedia.org/wiki/Fabry%E2%80%93P%C3%A9rot_interferometer
same_as:
  wikidata: Q1359945
  wikipedia: Fabry–Pérot interferometer
---

## Example

A Fabry–Pérot interferometer is a pair of parallel, partially reflecting mirrors at distance $\ell$, with a medium of [[refractive index|9VGK0SP6EQ]] $n$ between them.
Assume the mirrors are lossless, with intensity reflectance $R \in (0, 1)$ and transmittance $1 - R$.
Light of vacuum wavelength $\lambda$ crosses the gap at angle $\theta$ to the normal.
Let $\delta = \frac{2\pi}{\lambda} \, 2 n \ell \cos\theta$ be the phase delay of one round trip, from the [[optical path length|AQ5ZKPZ88R]].
The transmitted intensity, as a fraction of the incident one, is
$$T(\delta) = \frac{1}{1 + F \sin^2(\delta / 2)}, \qquad F = \frac{4R}{(1 - R)^2}.$$

Check: the transmitted wave is the sum of the beams that bounce back and forth $0, 1, 2, \dots$ times.
Each round trip multiplies the amplitude by $R \, e^{i\delta}$, and the two passes through the mirrors give the factor $1 - R$.
The geometric series gives the amplitude $(1 - R) / (1 - R e^{i\delta})$.
Its squared modulus is $(1 - R)^2 / ((1 - R)^2 + 4R \sin^2(\delta/2))$, which equals $T(\delta)$.

So $T = 1$ exactly when $\delta \in 2\pi\Z$, that is when $2 n \ell \cos \theta = m \lambda$ for an integer $m$: all the beams interfere constructively.
Between these peaks $T$ drops to $1/(1 + F)$, which is small when $R$ is close to $1$.
At normal incidence the peaks are spaced in frequency by the free spectral range $c / (2 n \ell)$, where $c$ is the speed of light in vacuum.
The ratio of this spacing to the width of a peak at half height is the finesse, approximately $\pi \sqrt{R} / (1 - R)$ when $R$ is close to $1$.

## Explanations

### L1 human

Two facing mirrors that let a little light through trap light between them, where it bounces many times.
Only light whose wavelength fits a whole number of times into the round trip adds up in step and passes through.
Other wavelengths cancel themselves out and are reflected back.
The more reflective the mirrors, the sharper the selection, which is why such a device makes a very fine colour filter.
Lasers use the same idea in their cavities.
