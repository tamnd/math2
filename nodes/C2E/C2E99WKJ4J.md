---
tag: C2E99WKJ4J
kind: example
name: Arago spot
msc: [78A45]
illustrates: [M8669NXXJS]
uses: [4JZ84R10NJ]
sources:
  - url: https://en.wikipedia.org/wiki/Arago_spot
same_as:
  wikidata: Q1807778
  wikipedia: Arago spot
---

## Example

Let a plane wave $e^{ikz}$, with $k = 2\pi/\lambda$, fall normally on an opaque disk of radius $a$ in the plane $z = 0$.
Take the field just behind the plane to be $1$ outside the disk and $0$ on it.
Compute the field on the axis at distance $z$ with the [[Fresnel diffraction integral|4JZ84R10NJ]].
In polar coordinates $\rho$ in the plane,
$$u(0, 0, z) = \frac{e^{ikz}}{i \lambda z} \int_a^\infty e^{i k \rho^2/(2z)} \, 2\pi \rho \, d\rho = \frac{\pi e^{ikz}}{i \lambda z} \int_{a^2}^\infty e^{i k w/(2z)} \, dw,$$
with $w = \rho^2$.
The last integral, taken as an Abel limit (with a factor $e^{-\varepsilon w}$, $\varepsilon \to 0^+$), equals $\frac{2 i z}{k} e^{i k a^2/(2z)}$.
Since $\frac{\pi}{i\lambda z} \cdot \frac{2 i z}{k} = 1$, one gets
$$u(0, 0, z) = e^{ikz} \, e^{i k a^2 / (2z)}, \qquad \abs{u}^2 = 1.$$
So the centre of the shadow is exactly as bright as the unobstructed wave.
This bright spot in the middle of the shadow is the *Arago spot*.

## Remarks

Geometrical optics predicts complete darkness on the axis behind the disk, so the spot is a pure wave effect.
Poisson derived the spot from Fresnel's wave theory as an argument against it, and Arago then observed it, which supported the theory.
In practice the spot is seen when the edge of the disk is smooth to within a small fraction of the Fresnel zone widths.

## Explanations

### L1 human

Put a small round coin in a laser beam and look at its shadow on a far wall.
At the very centre of the dark shadow there is a bright point.
Waves bending around the circular edge all travel the same distance to the centre, so they arrive in step and add up.
