---
tag: 2Y4AJSNYDB
kind: definition
name: Gravity anomaly
msc: [86A30, 86A20]
defines: J6V1B7SP0Q
uses: [5Y2BWNY6MF, 999BYZY0ZG, R9XX7TNJCH]
sources:
  - url: https://en.wikipedia.org/wiki/Gravity_anomaly
---

## Definition

Let $W$ be the [[geopotential|5Y2BWNY6MF]] of the Earth, so that $g = \norm{\nabla W}$ is the magnitude of gravity.
Let $U$ be the normal potential of a [[reference ellipsoid|R9XX7TNJCH]], chosen so that the ellipsoid is a level surface of $U$.
Let $\gamma = \norm{\nabla U}$ be the normal gravity.
Let $P$ be a point on the [[geoid|999BYZY0ZG]], and let $Q$ be the point of the ellipsoid on the ellipsoidal normal through $P$.
The *gravity anomaly* at $P$ is
$$\Delta g(P) = g(P) - \gamma(Q).$$

## Remarks

Example: if gravity on the geoid at $P$ is $9.80700\ \mathrm{m/s^2}$ and normal gravity at $Q$ is $9.80650\ \mathrm{m/s^2}$, then $\Delta g(P) = 5 \cdot 10^{-4}\ \mathrm{m/s^2} = 50$ mGal.
Non-example: the difference $g(P) - \gamma(P)$, with both values taken at the same point $P$, is not the gravity anomaly.
It is called the gravity disturbance $\delta g(P)$, and it differs from $\Delta g(P)$ by about $0.3086$ mGal per metre of geoid height.
In geophysics the word is used more loosely for observed gravity minus gravity predicted by any model, after a reduction such as the [[free-air|WDMHD6BW8Y]] or [[Bouguer|NMH22NTFJT]] reduction.
The unit is the milligal: $1$ mGal $= 10^{-5}\ \mathrm{m/s^2}$.
