---
tag: A2X0FXC6HK
kind: problem
name: Turbulence closure problem
msc: [76F55]
uses: [4EYAHQDA7Q, FDQE4PF63G, V47TX9AFKF]
about: [VY307F8Z0S, 4EYAHQDA7Q]
sources:
  - url: https://en.wikipedia.org/wiki/Turbulence_modeling
history:
  posed_by: "Osborne Reynolds"
  first_stated: "1895"
---

## Problem

Averaging the Navier–Stokes equations of an incompressible turbulent flow gives the [[Reynolds-averaged Navier–Stokes equations|4EYAHQDA7Q]] for the mean velocity $\bar u_i$ and mean pressure $\bar p$.
These contain the correlations $\overline{u_i' u_j'}$ of the [[Reynolds decomposition|V47TX9AFKF]], which give the [[Reynolds stress|FDQE4PF63G]] tensor.
The mean equations do not determine these correlations.
Equations for the second moments $\overline{u_i' u_j'}$, derived in the same way, contain third moments $\overline{u_i' u_j' u_k'}$.
In general the equations for moments of order $n$ contain moments of order $n + 1$.
The *closure problem* asks for a way to express the unknown higher moments in terms of lower ones.
The aim is a finite system of equations, for the mean flow or for finitely many statistics, that determines the turbulent statistics.

## Remarks

Reynolds' 1895 paper introduced the averaged equations together with the unknown turbulent stresses.
No exact closure derived from the Navier–Stokes equations is known, and the problem is open as a question of mathematical physics.
In practice it is handled by turbulence models, which are approximate closures with empirical constants.
Examples are eddy viscosity models such as the Boussinesq hypothesis and the $k$–$\varepsilon$ model, Reynolds stress transport models, and subgrid models in large eddy simulation.
These models work well in flows similar to those used to calibrate them and can fail in others, for example in strongly rotating or separated flows.

## Explanations

### L1 human

To predict the average flow of a turbulent fluid, one averages the exact equations.
The averaging leaves an unknown term describing the eddies.
Writing an equation for that term produces a new unknown, and so on without end.
The closure problem is to cut this chain in a reliable way, and nobody knows how to do it exactly.
