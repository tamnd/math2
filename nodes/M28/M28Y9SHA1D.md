---
tag: M28Y9SHA1D
kind: definition
name: Proper motion
msc: [85A04]
defines: K38DHGRW6D
uses: [RHNFB0HEW4, 5HD86E1TEH]
sources:
  - url: https://en.wikipedia.org/wiki/Proper_motion
---

## Definition

Let $\alpha(t)$ and $\delta(t)$ be the barycentric [[right ascension|RHNFB0HEW4]] and [[declination|5HD86E1TEH]] of a star in a fixed reference frame.
Here parallax, aberration, precession and nutation are removed.
The *proper motion* of the star is the pair
$$\mu_{\alpha*} = \frac{d\alpha}{dt}\cos\delta, \qquad \mu_\delta = \frac{d\delta}{dt}.$$
Its *total proper motion* is $\mu = \sqrt{\mu_{\alpha*}^2 + \mu_\delta^2}$.

## Remarks

The factor $\cos\delta$ makes $\mu_{\alpha*}$ an angle on the sky; a change in right ascension near the pole is a small angle.
So $\mu$ is the angular speed of the star's direction on the celestial sphere.
With $\mu$ in arcseconds per year and the distance $d$ in parsecs, the tangential velocity is $v_t \approx 4.74\, \mu\, d$ km/s.
The factor $4.74$ is one astronomical unit per year in km/s.
Example: Barnard's Star has $\mu \approx 10.4''$ per year at $d \approx 1.83$ pc, so $v_t \approx 90$ km/s.
Non-example: the yearly back-and-forth ellipse traced by a nearby star is parallax, not proper motion; it is periodic, while proper motion is a steady drift.
The velocity along the line of sight is the radial velocity, measured by the Doppler effect, not by positions.
