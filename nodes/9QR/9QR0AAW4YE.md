---
tag: 9QR0AAW4YE
kind: definition
name: Limb darkening
msc: [85A25, 85A15]
defines: EM7C674YV6
uses: [TWF69TQH3S]
sources:
  - url: https://en.wikipedia.org/wiki/Limb_darkening
---

## Definition

Consider a spherical star seen from far away.
For a point on its visible disk, let $\theta$ be the angle between the line of sight and the outward normal to the surface there.
Let $\mu = \cos\theta \in [0, 1]$.
Let $I(\mu)$ be the specific intensity of the emergent radiation in the direction of the observer.
The star shows *limb darkening* when $I(\mu)$ is an increasing function of $\mu$, so that $I(\mu) < I(1)$ for $\mu < 1$; the ratio $I(\mu)/I(1)$ is the *limb-darkening law*.

## Remarks

Example: in a grey atmosphere in the Eddington approximation, the source function is linear in the [[optical depth|TWF69TQH3S]], $S(\tau) = a + b\tau$ with $b = 3a/2 > 0$.
The emergent intensity is then $I(\mu) = a + b\mu$, so $I(\mu)/I(1) = (2 + 3\mu)/5$.
This increases with $\mu$ and equals $2/5$ at the limb.
Non-example: a semi-infinite atmosphere with constant source function $S$ gives $I(\mu) = S$ for all $\mu$, so there is no limb darkening.
A common empirical form is the linear law $I(\mu)/I(1) = 1 - u(1 - \mu)$ with a coefficient $u$ that depends on wavelength.
The Eddington–Barbier relation $I(\mu) \approx S(\tau = \mu)$ explains the effect: the observer sees down to optical depth about $\mu$ along the normal.
