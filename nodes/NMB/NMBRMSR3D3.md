---
tag: NMBRMSR3D3
kind: definition
name: Optical aberration
msc: [78A05, 78A10]
defines: VG0GPBKP84
uses: [N111BHFQ2H, AQ5ZKPZ88R, 90F3NWRHVD]
sources:
  - url: https://en.wikipedia.org/wiki/Optical_aberration
---

## Definition

Consider an optical system with an exit pupil, in a medium of refractive index $n$ on the image side.
Let $P$ be an object point and let $P'$ be its Gaussian image point, that is, its image under the [[paraxial approximation|N111BHFQ2H]].
Let $\Sigma$ be the reference sphere: the sphere centred at $P'$ through the centre of the exit pupil.

1. The *wave aberration* $W(x, y)$ at a point $(x, y)$ of the exit pupil is an [[optical path length|AQ5ZKPZ88R]]. It is measured along the ray from $P$ through $(x, y)$, from the reference sphere $\Sigma$ to the actual wavefront through the centre of the pupil.
2. The *transverse ray aberration* of that ray is the vector from $P'$ to the point where the ray meets the Gaussian image plane.
3. The system has an *aberration* at $P$ when $W$ is not identically zero on the exit pupil.

## Remarks

If the system images $P$ perfectly at $P'$, the wavefront leaving the pupil is exactly the sphere $\Sigma$, so $W \equiv 0$ and all ray aberrations vanish.
A single converging lens with spherical surfaces fails this for points on its axis.
Rays through its rim focus closer to the lens than paraxial rays, and $W$ has a nonzero term in the fourth power of the pupil radius.
To first order the two measures are linked: the transverse ray aberration is $-(R/n) \nabla W$, where $R$ is the radius of $\Sigma$ (the sign depends on the convention).
Aberrations that occur for light of one wavelength are *monochromatic*; aberrations caused by the dependence of the [[refractive index|9VGK0SP6EQ]] on the wavelength are *chromatic*.

## Explanations

### L1 human

The ideal wave leaving a lens toward an image point is a piece of a sphere centred at that point.
The wave aberration measures, at each point of the lens opening, how far the real wave lags or leads this ideal sphere.
If this lag is zero everywhere, the lens forms a perfect point image.
