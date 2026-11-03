---
tag: P7XHYM4KYQ
kind: definition
name: Thermal conductivity
msc: [80A19, 80A17]
defines: XBQBT9E7JT
uses: [SW8X60GYZT, 1Y36434YTE, KK46Q2YV1D, 0ABK9V9Y64]
sources:
  - url: https://en.wikipedia.org/wiki/Thermal_conductivity_and_resistivity
---

## Definition

Let a homogeneous isotropic material conduct heat, with [[temperature|KK46Q2YV1D]] field $T$ and [[heat flux|1Y36434YTE]] $\mathbf{q}$ of [[conduction|SW8X60GYZT]].
Assume that $\mathbf{q}$ is proportional to the [[gradient|0ABK9V9Y64]] $\nabla T$ at each point.
The *thermal conductivity* of the material is the number $k$ such that
$$\mathbf{q} = -k \, \nabla T.$$
Its unit is $\mathrm{W \, m^{-1} \, K^{-1}}$.
The reciprocal $1/k$ is the *thermal resistivity*.

## Remarks

Example: a slab of thickness $L = 0.1$ metres conducts a heat flux of $200$ watts per square metre when its faces differ by $20$ kelvin.
Then $\abs{\nabla T} = 20 / 0.1 = 200$ kelvin per metre, so $k = 200 / 200 = 1$ watt per metre per kelvin.

Non-example: the ratio $Q / \Delta T$ of a whole wall, in watts per kelvin, is not the conductivity.
It depends on the size and shape of the wall; it is the thermal conductance.

The second law of thermodynamics forces $k \ge 0$.
In general $k$ depends on temperature, and in an anisotropic material it is replaced by a tensor.
