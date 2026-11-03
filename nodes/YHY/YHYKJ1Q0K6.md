---
tag: YHYKJ1Q0K6
kind: definition
name: Reynolds number
msc: [76M55, 76D05, 76F06]
defines: JH9EJ0HA0R
uses: [T3R5FWV91P, NM5Q4845Z4, 18KXZHVF4M]
sources:
  - url: https://en.wikipedia.org/wiki/Reynolds_number
---

## Definition

Consider a flow of a fluid with density $\rho$ and dynamic [[viscosity|NM5Q4845Z4]] $\mu$.
Let $U$ be a characteristic speed and $L$ a characteristic length of the flow.
The *Reynolds number* of the flow is
$$\mathrm{Re} = \frac{\rho U L}{\mu} = \frac{U L}{\nu},$$
where $\nu = \mu / \rho$ is the kinematic viscosity.

## Remarks

It is a [[dimensionless number|T3R5FWV91P]]: $[U L] = \mathsf{L}^2 \mathsf{T}^{-1} = [\nu]$.
Example: water with $\nu \approx 10^{-6}\ \mathrm{m^2/s}$ flowing at $U = 1\ \mathrm{m/s}$ past an object of size $L = 1\ \mathrm{cm}$ has $\mathrm{Re} \approx 10^{4}$.
Non-example: the ratio $U / \nu$ is not a Reynolds number; it has dimension $\mathsf{L}^{-1}$ because the length scale is missing.
In the variables $x' = x/L$, $t' = t U / L$, $\mathbf{u}' = \mathbf{u}/U$, the incompressible [[Navier–Stokes equations|18KXZHVF4M]] contain the viscous term with the factor $1/\mathrm{Re}$ and no other parameter.
The value of $\mathrm{Re}$ depends on the choice of $U$ and $L$, so a value is meaningful only together with this choice.
In pipe flow, for example, one uses the diameter and the mean speed.
