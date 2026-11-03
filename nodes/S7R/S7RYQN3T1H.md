---
tag: S7RYQN3T1H
kind: concept
name: K-epsilon turbulence model
msc: [76F60, 76F55]
sources:
  - url: https://en.wikipedia.org/wiki/K-epsilon_turbulence_model
same_as:
  wikidata: Q17148242
  wikipedia: K-epsilon turbulence model
---

## Summary

The $k$–$\varepsilon$ model is a two-equation turbulence model for the [[Reynolds-averaged Navier–Stokes equations|4EYAHQDA7Q]].
It solves transport equations for the turbulent kinetic energy $k$ and its dissipation rate $\varepsilon$, and builds an eddy viscosity $\nu_t = C_\mu k^2 / \varepsilon$ from them.
Combined with the [[Boussinesq eddy viscosity hypothesis|4K9W1VP58R]], this closes the averaged equations.
Its standard form, with constants fitted to simple flows, has long been one of the most widely used models in industrial computational fluid dynamics.

## Explanations

### L1 human

To estimate how strongly turbulence mixes a flow, one needs a size and a speed for the eddies.
The model tracks two quantities through the flow: how much energy the eddies hold, $k$, and how fast they lose it, $\varepsilon$.
From these two numbers it gets an eddy speed $\sqrt{k}$ and an eddy size $k^{3/2} / \varepsilon$, and so an effective viscosity.
Each quantity is carried along by the mean flow, spread by the eddies, created by the mean shear and destroyed by dissipation.
