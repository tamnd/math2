---
tag: 87RE4BVJFG
kind: definition
name: Whispering-gallery wave
msc: [78A40, 78A50]
defines: JQYE9SWR7F
uses: [GS6CP71X4K, 9VGK0SP6EQ, CZCMRDWDYW]
sources:
  - url: https://en.wikipedia.org/wiki/Whispering-gallery_wave
---

## Definition

Let a dielectric cylinder of radius $R$ and [[refractive index|9VGK0SP6EQ]] $n > 1$ stand in vacuum.
Consider fields independent of the axial coordinate, with time factor $e^{-i\omega t}$ and vacuum wavenumber $k_0 = \omega/c$.
In polar coordinates $(r, \varphi)$, the axial field component $u$ satisfies the Helmholtz equation $\Delta u + n(r)^2 k_0^2 u = 0$.
Its separated solutions inside the cylinder are $u = J_m(n k_0 r) \, e^{im\varphi}$ with $m \in \Z$.
Here $J_m$ is the [[Bessel function of the first kind|CZCMRDWDYW]].
A *whispering-gallery mode* is a resonant mode of this form, outgoing outside the cylinder, with a large azimuthal number $\abs{m}$.
Its resonant frequency satisfies $\abs{m} < n k_0 R$ with $\abs{m}$ close to $n k_0 R$.
Then the field is concentrated in a thin annulus inside the boundary.
A *whispering-gallery wave* is the travelling wave $e^{i(m\varphi - \omega t)}$ circulating around the rim that such a mode describes.

## Remarks

The function $J_m(\rho)$ is exponentially small for $0 < \rho < \abs{m}$ when $\abs{m}$ is large, so the mode lives only in the annulus $\abs{m}/(n k_0) < r < R$.
Outside, the field must tunnel through the region $R < r < \abs{m}/k_0$ before it can radiate, which makes the radiation loss tiny and the quality factor very large.
The approximate resonance condition is $m \lambda / n \approx 2\pi R$, a whole number of wavelengths in the medium around the circumference.
In ray terms, the light hits the boundary at an angle of incidence $\theta$ with $\sin\theta \approx \abs{m}/(n k_0 R)$, above the critical angle of [[total internal reflection|GS6CP71X4K]].
Example: a glass disk with $R = 50\ \mu$m and $n = 1.45$ at vacuum wavelength $1.55\ \mu$m has whispering-gallery modes with $m$ near $2\pi n R / \lambda \approx 294$.
Non-example: the mode with $m = 0$ has its largest values on the axis of the cylinder, so it is a resonant mode of the cylinder but not a whispering-gallery mode.
