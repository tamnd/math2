---
tag: 8GF20Z4KDC
kind: statement
role: proposition
name: Bruns formula
msc: [86A30]
uses: [5Y2BWNY6MF, 999BYZY0ZG, R9XX7TNJCH]
about: [999BYZY0ZG]
sources:
  - url: https://en.wikipedia.org/wiki/Physical_geodesy
---

## Statement

Let $W$ be the [[geopotential|5Y2BWNY6MF]] of the Earth and let the [[geoid|999BYZY0ZG]] be the level surface $W = W_0$.
Let $U$ be the normal potential of a [[reference ellipsoid|R9XX7TNJCH]], chosen so that $U = W_0$ on the ellipsoid.
Let $\gamma$ be the magnitude of normal gravity on the ellipsoid.
Let $T = W - U$ be the disturbing potential.
Let $P$ be a point of the geoid, and let $Q$ be the point of the ellipsoid on the ellipsoidal normal through $P$.
Let $N$ be the geoid height, the signed distance from $Q$ to $P$.
Then, to first order in $N$,
$$N = \frac{T(P)}{\gamma(Q)}.$$

## Remarks

The proof is a one-term Taylor expansion of $U$ along the ellipsoidal normal.
Normal gravity points inward along this normal, so $U(P) \approx U(Q) - \gamma(Q) N = W_0 - \gamma(Q) N$.
Since $W(P) = W_0$, this gives $T(P) = W(P) - U(P) \approx \gamma(Q) N$.
The neglected terms are of order $N^2$ times the second derivative of $U$, which is negligible because $N$ is at most about $100$ m.
Example: a disturbing potential $T(P) = 98\ \mathrm{m^2/s^2}$ with $\gamma \approx 9.8\ \mathrm{m/s^2}$ gives a geoid height of $10$ m.

## Explanations

### L1 human

The geoid rises above the ellipsoid where the true gravity potential is larger than the model potential.
Bruns formula says how much it rises: divide the potential excess by gravity.
This is the same rule as "work equals force times distance", read backwards.

### L2 human

Bruns formula turns the geoid problem into a problem about the harmonic function $T$.
Combined with the boundary condition $\partial T/\partial r + 2T/R = -\Delta g$ for the [[gravity anomaly|J6V1B7SP0Q]], it leads to the [[geodetic boundary value problem|1F4S3G1R6J]] and to [[Stokes' formula|MNK0GW8ZM6]].
It is also used in reverse, to turn a global spherical harmonic model of $T$ into geoid heights.
