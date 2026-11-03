---
tag: DFRH1H193H
kind: definition
name: Green–Ampt infiltration model
msc: [76S05, 86A05]
defines: CZDB84HJ2Q
uses: [DX8RV2XG6H, 0NT64JV96A]
sources:
  - url: https://en.wikipedia.org/wiki/Infiltration_(hydrology)
---

## Definition

Consider a uniform soil with saturated hydraulic conductivity $K > 0$, initial water content $\theta_i$ and saturated water content $\theta_s > \theta_i$.
From time $0$ on, its surface is kept ponded with negligible depth.
Set $\Delta\theta = \theta_s - \theta_i$ and let $\psi > 0$ be the suction head at the wetting front.
The *Green–Ampt model* assumes that:

1. the soil above a sharp wetting front at depth $L(t)$ is saturated and the soil below has water content $\theta_i$;
2. the flow in the saturated zone obeys [[Darcy's law|DX8RV2XG6H]] with conductivity $K$ and a head difference $L + \psi$ over the length $L$.

The cumulative infiltration is $F(t) = \Delta\theta \, L(t)$, and the infiltration rate $f = dF/dt$ satisfies the [[ordinary differential equation|0NT64JV96A]]
$$f = \frac{dF}{dt} = K \Big( 1 + \frac{\psi \, \Delta\theta}{F} \Big), \qquad F(0) = 0.$$

## Remarks

Example: separating variables, $dt = \frac{F \, dF}{K (F + \psi \Delta\theta)}$, and integrating from $0$ gives the implicit solution
$$K t = F - \psi \, \Delta\theta \, \ln \Big( 1 + \frac{F}{\psi \, \Delta\theta} \Big).$$
For small $t$ this gives $F \approx \sqrt{2 K \psi \Delta\theta \, t}$, and for large $t$ the rate $f$ tends to $K$.

Non-example: a soil made of a clay layer over sand does not satisfy the uniformity assumption, and a single front with one value of $K$ does not describe its infiltration.

The model is a sharp-front approximation of Richards' equation; a non-negligible ponding depth $h_0$ adds $h_0$ to the head difference in clause 2.
Under rainfall at a constant rate $p$, the surface ponds only if $p > K$, and the model then applies only from the time of ponding on.
