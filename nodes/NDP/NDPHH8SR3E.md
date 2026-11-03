---
tag: NDPHH8SR3E
kind: definition
name: Earth's magnetic field
msc: [86A25]
defines: Z13HPJFV1F
uses: [XRED3C547P, 2K5D5HH89T, 0H7C3T1GJY, S8RG6N1PRT]
sources:
  - url: https://en.wikipedia.org/wiki/Earth%27s_magnetic_field
---

## Definition

*Earth's magnetic field* is the [[magnetic field|XRED3C547P]] $B(x, t)$ at points $x$ in and near the Earth, at time $t$.
It is the sum of an internal part and an external part.
The internal part comes from sources inside the Earth, mainly the core and also the crust.
The external part comes from currents in the ionosphere and magnetosphere.
At a point of the surface, in the local frame with axes to geographic north, east and vertically down, write $B = (X, Y, Z)$.
The *elements* of the field are:

1. the horizontal intensity $H = \sqrt{X^2 + Y^2}$ and the total intensity $F = \sqrt{X^2 + Y^2 + Z^2}$;
2. the declination $D$, the angle from geographic north to the horizontal component, measured eastward, so $(X, Y) = H (\cos D, \sin D)$;
3. the inclination $I$, the angle of $B$ below the horizontal, so $\tan I = Z / H$.

## Remarks

In a region without electric currents, $\nabla \times B = 0$, and by [[Gauss's law for magnetism|2K5D5HH89T]] $\nabla \cdot B = 0$.
So on a current-free spherical shell around the Earth, $B = -\nabla V$ for a [[scalar potential|0H7C3T1GJY]] $V$ that solves [[Laplace's equation|S8RG6N1PRT]].
Example: $X = 20\,000$ nT, $Y = 0$ and $Z = 20\,000$ nT give $H = 20\,000$ nT, $F \approx 28\,284$ nT, $D = 0^\circ$ and $I = 45^\circ$.
Non-example: the field of a bar magnet in a laboratory is a magnetic field, but it is not part of the Earth's field.
The magnetic field is often reported in nanotesla (nT), with $1$ nT $= 10^{-9}$ T.

## Explanations

### L1 human

The Earth's field at a place is an arrow with a direction and a length.
Declination tells how far a compass points away from true north, inclination how steeply the arrow dips, and intensity how strong it is.
