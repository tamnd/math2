---
tag: KRR89E9XW0
kind: definition
name: Froude number
msc: [76M55, 76B15]
defines: R2QQEFPTP8
uses: [T3R5FWV91P]
sources:
  - url: https://en.wikipedia.org/wiki/Froude_number
---

## Definition

Consider a flow under gravity with acceleration $g$, and let $U$ be a characteristic speed and $L$ a characteristic length of the flow.
The *Froude number* is
$$\mathrm{Fr} = \frac{U}{\sqrt{g L}}.$$
For flow in an open channel of depth $h$, one takes $L = h$; the flow is *subcritical* if $\mathrm{Fr} < 1$ and *supercritical* if $\mathrm{Fr} > 1$.

## Remarks

It is a [[dimensionless number|T3R5FWV91P]]: $[g L] = \mathsf{L}^2 \mathsf{T}^{-2} = [U^2]$.
Some authors call $U^2 / (g L)$ the Froude number; this is the square of the definition above.
Example: water of depth $h = 0.1\ \mathrm{m}$ flowing at $U = 2\ \mathrm{m/s}$ has $\mathrm{Fr} = 2 / \sqrt{0.981} \approx 2.0$, so the flow is supercritical.
Non-example: $U / (g L)$ is not a Froude number; it has dimension $\mathsf{L}^{-1} \mathsf{T}$.
In shallow water, $\sqrt{g h}$ is the speed of long surface waves, so $\mathrm{Fr}$ compares the current with the wave speed.
