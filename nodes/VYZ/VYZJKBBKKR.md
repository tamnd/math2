---
tag: VYZJKBBKKR
kind: definition
name: Fresnel number
msc: [78A45]
defines: AK3TF7B3ZW
uses: [JE101TDP4Q]
sources:
  - url: https://en.wikipedia.org/wiki/Fresnel_number
---

## Definition

Consider monochromatic light of wavelength $\lambda$ passing through an aperture of characteristic size $a$, such as the radius of a circular aperture.
The light is observed on a screen at distance $L$ from the aperture.
The *Fresnel number* is
$$N_F = \frac{a^2}{L \lambda}.$$

## Remarks

Example: $a = 1$ mm, $\lambda = 500$ nm and $L = 1$ m give $N_F = 10^{-6} / (5 \cdot 10^{-7}) = 2$.
For a circular aperture of radius $a$ and a point on the axis, the $m$-th Fresnel zone has outer radius about $\sqrt{m \lambda L}$.
So $N_F$ is the number of Fresnel zones that fit in the aperture.
The regimes are: $N_F \ll 1$ for Fraunhofer diffraction, $N_F \gtrsim 1$ for Fresnel diffraction, and $N_F \gg 1$ for the geometrical shadow.
The number depends on the choice of $a$ (radius or diameter), so only its order of magnitude matters.

## Explanations

### L1 human

The Fresnel number compares the area of the aperture with the product of the distance and the wavelength.
Small values mean far away, where the pattern is a pure Fourier transform of the aperture.
