---
tag: Y46NWBWB5C
kind: definition
name: Rayleigh criterion
msc: [78A10, 78A45]
defines: K9GR534B1N
uses: [HHWESQD7QB, DB435TBQJT, CZCMRDWDYW]
sources:
  - url: https://en.wikipedia.org/wiki/Angular_resolution
---

## Definition

Let an aberration-free optical system with a circular aperture of diameter $D$ image two incoherent point sources of the same wavelength $\lambda$.
Let $\theta$ be the angle between the directions of the two sources.
By the *Rayleigh criterion*, the two sources are *just resolved* when the following holds.
The centre of the [[Airy disk|DB435TBQJT]] of one source lies on the first dark ring of the Airy pattern of the other.
This happens when
$$\sin \theta = \frac{j_{1,1}}{\pi} \, \frac{\lambda}{D} \approx 1.22 \, \frac{\lambda}{D},$$
where $j_{1,1} \approx 3.8317$ is the first positive zero of the [[Bessel function|CZCMRDWDYW]] $J_1$.
The sources are *resolved* when $\theta$ is at least this value.

## Remarks

The constant comes from the [[point spread function|HHWESQD7QB]] of the circular aperture.
At angle $\vartheta$ from the centre it is proportional to $(2 J_1(v)/v)^2$ with $v = \pi D \sin(\vartheta) / \lambda$.
Its first zero is at $v = j_{1,1}$, which gives the formula.
For a slit of width $a$ the same rule gives $\sin \theta = \lambda / a$, since the first zero of $(\sin u / u)^2$ is at $u = \pi$.

Example: a telescope with $D = 0.1$ m at $\lambda = 500$ nm resolves two stars when $\theta \ge 1.22 \times 5 \times 10^{-6}$ rad, that is about $6.1 \times 10^{-6}$ rad.

Non-example: two sources at half this angle are not resolved by the criterion, since the centre of each pattern lies inside the central disc of the other.

The criterion is a convention, not a theorem; other conventions, such as the Sparrow criterion, use a slightly different separation.
