---
tag: WTVYA5Y5NJ
kind: statement
role: theorem
name: Van Cittert–Zernike theorem
msc: [78A10, 78A45, 42B10]
uses: [VQCMBT9YSK, DPVM34ADZV, CZCMRDWDYW, HE51RF4XB9, D7YGBADRV9]
about: [VQCMBT9YSK]
sources:
  - url: https://en.wikipedia.org/wiki/Van_Cittert%E2%80%93Zernike_theorem
same_as:
  wikidata: Q2298452
  wikipedia: Van Cittert–Zernike theorem
---

## Statement

Let a planar, spatially incoherent, quasi-monochromatic source of mean wavelength $\bar\lambda$ lie in the plane $z = 0$.
Let its intensity be $I(\xi, \eta) \ge 0$, integrable with compact support and with $\int I > 0$.
Observe the field in the plane at distance $z > 0$, and assume the paraxial (Fresnel) approximation for propagation from the source to this plane.
Assume that all path differences involved are much smaller than the coherence length of the light.
Let $P_1 = (x_1, y_1)$ and $P_2 = (x_2, y_2)$ be two points of the observation plane, with $\Delta x = x_2 - x_1$ and $\Delta y = y_2 - y_1$.
Then the complex [[degree of coherence|VQCMBT9YSK]] $\mu_{12}$ of the field at $P_1$ and $P_2$, at zero delay, satisfies
$$\abs{\mu_{12}} = \frac{\abs{\displaystyle\iint I(\xi, \eta) \exp\!\left(-\frac{2\pi i}{\bar\lambda z}(\Delta x \, \xi + \Delta y \, \eta)\right) d\xi \, d\eta}}{\displaystyle\iint I(\xi, \eta) \, d\xi \, d\eta}.$$
Moreover $\mu_{12}$ itself is this normalised [[Fourier transform|DPVM34ADZV]] of $I$ times a phase factor of modulus $1$.
This factor depends only on $P_1$, $P_2$, $z$ and $\bar\lambda$.

## Remarks

Proof idea: the field at each observation point is a superposition of the source field, propagated by the [[Huygens–Fresnel principle|HE51RF4XB9]].
The mutual intensity at $P_1, P_2$ is then a double integral over pairs of source points.
Spatial incoherence makes the mutual intensity of the source proportional to $I(\xi, \eta)$ times a delta function on the diagonal, so the double integral collapses to a single one.
In the paraxial approximation the remaining phase is linear in $(\xi, \eta)$ up to terms that depend only on $P_1$ and $P_2$, which gives a Fourier transform.

Example: a uniform circular source of radius $a$ gives $\abs{\mu_{12}} = \abs{2 J_1(v) / v}$ with $v = 2\pi a d / (\bar\lambda z)$ and $d = \abs{P_1 P_2}$, where $J_1$ is the [[Bessel function|CZCMRDWDYW]] of order $1$.
The first zero of $J_1$ at $v \approx 3.832$ gives the distance $d \approx 0.61 \, \bar\lambda z / a$ at which the coherence first vanishes.
This is how the Michelson stellar interferometer measures the angular diameter $2a/z$ of a star.

Without spatial incoherence the result fails: a laser beam across the source plane is coherent everywhere, whatever its intensity profile.

## Explanations

### L1 human

Light from a hot source, such as a star, comes from many points that shine independently.
Still, far from the source, the light at two nearby places is partly in step.
The theorem says exactly how much: the degree of coherence is given by the Fourier transform of the brightness of the source.
So a small source produces light that is coherent over a wide area, and a large source over a small one.

### L2 human

The theorem has the same mathematical form as [[Fraunhofer diffraction|D7YGBADRV9]], with the source intensity in the role of the aperture.
This is why the coherence pattern of a uniform disc looks like the Airy pattern of a circular hole.
In radio astronomy the theorem is the basis of aperture synthesis.
Correlating the signals of pairs of antennas samples the Fourier transform of the sky brightness, which is then inverted to form an image.
In optics it explains why light from an extended thermal source becomes partially coherent after propagation, and how large a source may be for a given coherence area.
Its hypotheses are quasi-monochromatic light and small path differences; for broadband light, one applies it frequency by frequency.
