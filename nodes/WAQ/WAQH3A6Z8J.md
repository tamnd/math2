---
tag: WAQH3A6Z8J
kind: definition
name: Heat transfer
msc: [80A19, 80A21]
defines: FN55BYEGZZ
uses: [CY4GJQGF06, KK46Q2YV1D, 1Y36434YTE]
sources:
  - url: https://en.wikipedia.org/wiki/Heat_transfer
---

## Definition

*Heat transfer* is the transfer of energy as [[heat|CY4GJQGF06]] across a surface, caused by a difference of [[temperature|KK46Q2YV1D]] between the two sides.
Its rate is given by the [[heat flux|1Y36434YTE]] vector $q$.
The heat crossing a surface with unit normal $n$, per unit area and unit time, is $q \cdot n$.
It occurs by three modes.

1. Conduction: transfer through matter without bulk motion, by molecular collisions, lattice vibrations and free electrons.
2. Convection: transfer by the bulk motion of a fluid together with conduction within it.
3. Radiation: transfer by electromagnetic waves emitted by matter because of its temperature; it needs no medium.

## Remarks

Example: for conduction in an isotropic solid, Fourier's law gives $q = -k \nabla T$ with conductivity $k > 0$.
Take a wall of thickness $L = 0.2$ m and conductivity $k = 1\ \mathrm{W/(m\,K)}$, with faces at $20\,^\circ\mathrm{C}$ and $0\,^\circ\mathrm{C}$.
It carries the flux $\abs{q} = k \Delta T / L = 1 \cdot 20 / 0.2 = 100\ \mathrm{W/m^2}$, where $\Delta T = 20$ kelvin.
Let $T_s$ be the temperature of a surface and $T_\infty$ that of its surroundings.
For convection, Newton's law of cooling gives $q \cdot n = h (T_s - T_\infty)$, with heat transfer coefficient $h > 0$.
For radiation from a grey surface to large surroundings, the Stefan–Boltzmann law gives $q \cdot n = \varepsilon \sigma (T_s^4 - T_\infty^4)$, with emissivity $\varepsilon$ and Stefan–Boltzmann constant $\sigma$.
Non-example: work done by a piston on a gas is a transfer of energy, but it is not heat transfer, since it is not driven by a temperature difference.
