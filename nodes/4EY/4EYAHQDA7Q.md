---
tag: 4EYAHQDA7Q
kind: concept
name: Reynolds-averaged Navier–Stokes equations
msc: [76F55, 76D05]
sources:
  - url: https://en.wikipedia.org/wiki/Reynolds-averaged_Navier–Stokes_equations
same_as:
  wikidata: Q1536235
  wikipedia: Reynolds-averaged Navier–Stokes equations
---

## Summary

The Reynolds-averaged Navier–Stokes equations, or RANS equations, are the equations of motion for the mean flow of a [[turbulent|VY307F8Z0S]] fluid.
They are obtained by applying the [[Reynolds decomposition|V47TX9AFKF]] to the [[Navier–Stokes equations|18KXZHVF4M]] and averaging.
They look like the Navier–Stokes equations for the mean velocity, with an extra term, the divergence of the [[Reynolds stress|FDQE4PF63G]].
Closing them with a turbulence model is the most common way to compute turbulent flows in engineering.

## Explanations

### L1 human

Engineers designing a car or a pipe rarely need every swirl of the turbulent flow; they need the average flow.
The RANS equations are equations for that average flow.
Averaging the exact equations leaves behind one new term that records how the swirls move momentum around.
That term is unknown, so it has to be estimated by a model before the equations can be solved.
