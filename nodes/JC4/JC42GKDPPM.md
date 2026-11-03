---
tag: JC42GKDPPM
kind: definition
name: Free-air anomaly
msc: [86A30, 86A20]
defines: WDMHD6BW8Y
uses: [J6V1B7SP0Q, R9XX7TNJCH]
sources:
  - url: https://en.wikipedia.org/wiki/Free-air_gravity_anomaly
---

## Definition

Let $P$ be a station at height $h$ above sea level, and let $g_P$ be the magnitude of gravity measured at $P$.
Let $\gamma_0$ be the normal gravity of the [[reference ellipsoid|R9XX7TNJCH]] at the foot point of $P$ on the ellipsoid.
Let $\partial\gamma/\partial h$ be the vertical gradient of normal gravity, which is about $-0.3086$ mGal per metre.
The *free-air anomaly* at $P$ is
$$\Delta g_{\mathrm{FA}} = g_P - \frac{\partial \gamma}{\partial h}\, h - \gamma_0 \approx g_P + 0.3086\, h - \gamma_0,$$
with $g_P$ and $\gamma_0$ in mGal and $h$ in metres.

## Remarks

Example: at $h = 500$ m with $g_P = 979\,700.0$ mGal and $\gamma_0 = 979\,800.0$ mGal, the free-air anomaly is $979\,700.0 + 154.3 - 979\,800.0 = 54.3$ mGal.
Non-example: the raw difference $g_P - \gamma_0 = -100.0$ mGal of the same station is not a free-air anomaly, because the height term is missing.
The term $-(\partial\gamma/\partial h)\, h$ is the free-air correction.
The free-air anomaly is a [[gravity anomaly|J6V1B7SP0Q]] in which the reduction to the geoid uses the normal gradient only.
