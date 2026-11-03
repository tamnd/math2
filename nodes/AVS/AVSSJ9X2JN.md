---
tag: AVSSJ9X2JN
kind: definition
name: Rossby number
msc: [76U05, 76M55, 86A10]
defines: SCYK4FMY59
uses: [T3R5FWV91P]
sources:
  - url: https://en.wikipedia.org/wiki/Rossby_number
---

## Definition

Consider a flow in a frame that rotates with angular speed $\Omega$, and let $f$ be the Coriolis parameter.
On a planet at latitude $\varphi$, $f = 2 \Omega \sin \varphi$.
Let $U$ be a characteristic speed and $L$ a characteristic horizontal length of the flow.
The *Rossby number* is
$$\mathrm{Ro} = \frac{U}{f L}.$$

## Remarks

It is a [[dimensionless number|T3R5FWV91P]]: $[f L] = \mathsf{T}^{-1} \mathsf{L} = [U]$.
Example: a mid-latitude weather system with $U = 10\ \mathrm{m/s}$, $L = 10^6\ \mathrm{m}$ and $f = 10^{-4}\ \mathrm{s}^{-1}$ has $\mathrm{Ro} = 0.1$, so rotation dominates.
Non-example: $U / f$ alone is not a Rossby number; it has dimension $\mathsf{L}$.
The Rossby number is the ratio of the advective acceleration $U^2 / L$ to the Coriolis acceleration $f U$.
