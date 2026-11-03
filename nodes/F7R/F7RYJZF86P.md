---
tag: F7RYJZF86P
kind: definition
name: Gravitational microlensing
msc: [85A04, 83C99]
defines: Y3MA49EB2H
uses: [C02XZJBFSY, 4K4NMJCPD5, K38DHGRW6D]
sources:
  - url: https://en.wikipedia.org/wiki/Gravitational_microlensing
---

## Definition

Consider a compact lens of mass $M$ with [[Einstein radius|4K4NMJCPD5]] $\theta_E$, and a point source at angular separation $\beta$ from it.
Write $u = \beta / \theta_E$.
*Gravitational microlensing* is lensing in which the images of the [[lens equation|C02XZJBFSY]] are closer than the angular resolution of the observation.
So only the total magnification of the source is observed.
For a point lens and a point source this total magnification is
$$A(u) = \frac{u^2 + 2}{u \sqrt{u^2 + 4}}.$$
Let the lens and source move with constant relative [[proper motion|K38DHGRW6D]] $\mu_{rel}$.
Then
$$u(t) = \sqrt{u_0^2 + \left( \frac{t - t_0}{t_E} \right)^2}, \qquad t_E = \frac{\theta_E}{\mu_{rel}},$$
where $u_0$ is the minimal separation, reached at time $t_0$, and $t_E$ is the Einstein crossing time.

## Remarks

The magnification is the sum, over the two images, of $1 / \abs{\det(\partial \beta / \partial \theta)}$.
Example: at $u = 1$, when the source is on the Einstein ring, $A = 3 / \sqrt{5} \approx 1.34$.
As $u \to \infty$, $A \to 1$, and as $u \to 0$, $A \approx 1/u$ grows without bound for a point source.

Non-example: a galaxy lensing a quasar with images an arcsecond apart is resolved by telescopes; the images are seen separately, so it is strong lensing, not microlensing.

The light curve $A(u(t))$ is symmetric in time and does not depend on wavelength, which distinguishes microlensing from variable stars.
