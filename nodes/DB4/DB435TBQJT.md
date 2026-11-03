---
tag: DB435TBQJT
kind: object
name: Airy disk
msc: [78A45, 33C10]
uses: [C1JFRZEPWR, CZCMRDWDYW]
sources:
  - url: https://en.wikipedia.org/wiki/Airy_disk
same_as:
  wikidata: Q851016
  wikipedia: Airy disk
---

## Description

Let a plane monochromatic wave of wavelength $\lambda$ and wavenumber $k = 2\pi/\lambda$ fall normally on a circular aperture of radius $a$.
Let $J_1$ be the [[Bessel function of the first kind|CZCMRDWDYW]] of order $1$, and let $I_0$ be the intensity on the axis.
In the [[Fraunhofer regime|C1JFRZEPWR]], the intensity at angle $\theta$ from the axis is
$$I(\theta) = I_0 \left( \frac{2 J_1(x)}{x} \right)^2, \qquad x = k a \sin\theta.$$
The pattern is a bright central disk surrounded by fainter rings.
The *Airy disk* is the central bright disk, bounded by the first dark ring.
This ring lies at the first positive zero $x \approx 3.8317$ of $J_1$, that is, at
$$\sin\theta \approx 1.22 \, \frac{\lambda}{D}, \qquad D = 2a.$$

## Remarks

The formula comes from the Fourier transform of the indicator function of a disk: in polar coordinates its angular integral gives $J_0$, and $\int_0^x s J_0(s) \, ds = x J_1(x)$.
Since $2 J_1(x)/x \to 1$ as $x \to 0$, the expression is normalised so that $I(0) = I_0$.
About $84\%$ of the light lies inside the Airy disk.
The size of the Airy disk sets the resolving power of a telescope or microscope with a circular aperture.
In the Rayleigh criterion, two point sources are just resolved when the centre of one Airy pattern falls on the first dark ring of the other.

## Explanations

### L1 human

Even a perfect lens cannot focus a star to a point.
Because light is a wave and the lens has a finite size, the star appears as a small bright disk with faint rings around it.
The bigger the lens, the smaller the disk, which is why large telescopes see finer detail.
