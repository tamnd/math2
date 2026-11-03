---
tag: XB97XC2Q4Q
kind: definition
name: Strong gravitational lensing
msc: [85A04, 83C99]
defines: 20XXW00SHF
uses: [C02XZJBFSY, 4K4NMJCPD5]
sources:
  - url: https://en.wikipedia.org/wiki/Strong_gravitational_lensing
---

## Definition

Consider a thin gravitational lens with [[lens equation|C02XZJBFSY]] $\beta = \theta - \alpha(\theta)$, where $\theta, \beta \in \R^2$ are the image and source positions and $\alpha$ is the reduced deflection.
A source at position $\beta$ is *strongly lensed* if the equation $\beta = \theta - \alpha(\theta)$ has more than one solution $\theta$.
*Strong gravitational lensing* is lensing in this regime.
It includes the strongly distorted images, arcs and rings near the critical curves, where the Jacobian $\det(\partial \beta / \partial \theta)$ vanishes.

## Remarks

Example: for a point mass with [[Einstein radius|4K4NMJCPD5]] $\theta_E$ and a source at $\beta \ne 0$ on the positive axis, the equation reduces to $\theta^2 - \beta \theta - \theta_E^2 = 0$ along that axis.
It has the two real roots $\theta_\pm = \tfrac{1}{2}\left(\beta \pm \sqrt{\beta^2 + 4 \theta_E^2}\right)$, of opposite signs, so every source is strongly lensed by a point mass.
The images are bright only when $\beta$ is comparable with $\theta_E$ or smaller.

Non-example: take a circularly symmetric lens whose surface density is everywhere much smaller than the critical density $\Sigma_{cr}$.
Its lens map is one-to-one, so every source has exactly one image, only slightly distorted, and the lensing is weak.

For a transparent lens with a smooth mass distribution, the number of images of a source not on a caustic is odd.
Observed systems with two or four images have a further faint image that is hidden or demagnified.
