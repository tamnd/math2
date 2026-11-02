---
tag: 7YW5WB3BY4
kind: concept
name: Zernike polynomials
msc: [33C45, 78A10]
sources:
  - url: https://en.wikipedia.org/wiki/Zernike_polynomials
same_as:
  wikidata: Q132146
  wikipedia: Zernike polynomials
---

## Summary

The Zernike polynomials are an orthogonal family of polynomials on the closed unit disk.
In polar coordinates each one is a radial polynomial times $\cos(m\varphi)$ or $\sin(m\varphi)$.
They are the standard basis in optics for describing the aberrations of a wavefront through a circular lens or mirror.
Their radial parts are [[Jacobi polynomials|TRD7DSF2KR]] in disguise.

## Explanations

### L1 human

The light passing through a round lens arrives with small delays that vary across the disk of the lens.
Optical engineers write this delay map as a sum of standard patterns on the disk, the Zernike polynomials.
Each pattern has a name: $2\rho^2 - 1$ is "defocus", a bowl shape, and $\rho \cos \varphi$ is "tilt", a plane sloping in one direction.
Because the patterns are orthogonal, the size of each defect can be read off separately.
