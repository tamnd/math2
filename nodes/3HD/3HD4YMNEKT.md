---
tag: 3HD4YMNEKT
kind: definition
name: Scale height
msc: [86A10]
defines: F74BY6CT91
uses: [0J0FCWV32D]
sources:
  - url: https://en.wikipedia.org/wiki/Scale_height
---

## Definition

Let a layer of ideal gas have absolute temperature $T$ and mean molar mass $M$, under a gravitational acceleration $g$.
Let $R$ be the molar gas constant.
The *scale height* of the gas is
$$H = \frac{R T}{M g}.$$

## Remarks

Equivalently, $H = k_B T/(m g)$, with $k_B$ the Boltzmann constant and $m$ the mean mass of a molecule.
If the layer is in hydrostatic balance $dp/dz = -\rho g$ and obeys the ideal gas law $p = \rho R T/M$, then $dp/dz = -p/H$.
So for constant $T$ the pressure is $p(z) = p(0) \, e^{-z/H}$, an [[exponential function|0J0FCWV32D]], and it falls by the factor $e$ over each height $H$.
Example: for dry air, $M = 0.02896$ kg/mol, with $T = 288$ K, $g = 9.81$ m/s² and $R = 8.314$ J/(mol K), one gets $H \approx 8.4$ km.
Non-example: in a layer whose temperature changes with height, $H$ is a function of height, and the pressure is not a single exponential in $z$.
