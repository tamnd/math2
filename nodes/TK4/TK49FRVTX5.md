---
tag: TK49FRVTX5
kind: definition
name: Einstein radius
msc: [85A04, 83C99]
defines: 4K4NMJCPD5
uses: [C02XZJBFSY, JJCKCYTBXD, YDWH956TJA]
sources:
  - url: https://en.wikipedia.org/wiki/Einstein_radius
---

## Definition

Let a point mass $M$ lens a source.
Let $D_d$, $D_s$ and $D_{ds}$ be the angular diameter distances, as in [[distance measures|YDWH956TJA]].
They are measured to the lens, to the source, and from the lens to the source.
The *Einstein radius* of the lens is the angle
$$\theta_E = \sqrt{\frac{4 G M}{c^2} \, \frac{D_{ds}}{D_d \, D_s}},$$
where $G$ is the gravitational constant and $c$ is the speed of light.

## Remarks

By the [[lens equation|C02XZJBFSY]] for a point mass, $\beta = \theta - \theta_E^2 \theta / \abs{\theta}^2$, a source at $\beta = 0$ is imaged onto the whole circle $\abs{\theta} = \theta_E$.
The check: on that circle, $\theta_E^2 \theta / \abs{\theta}^2 = \theta$, so $\beta = 0$.
The [[deflection|JJCKCYTBXD]] at the ring is $\hat\alpha = 4 G M / (c^2 D_d \theta_E)$.

Example: a lens of one solar mass halfway to a source at $8$ kpc has $D_d = D_{ds} = 4$ kpc and $D_s = 8$ kpc.
With $4 G M_\odot / c^2 \approx 5.9$ km, one gets $\theta_E \approx 4.9 \times 10^{-9}$ rad, about $1$ milliarcsecond.

For an extended lens with circular symmetry the Einstein radius is the radius inside which the mean surface density equals the critical density $\Sigma_{cr} = c^2 D_s / (4 \pi G D_d D_{ds})$.
Non-example: an axially symmetric lens whose mean surface density is below $\Sigma_{cr}$ at every radius has no such radius; it forms no Einstein ring.
