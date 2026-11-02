---
tag: DWK5N5SKTK
kind: concept
name: Poisson's equation
msc: [35J05, 31B35]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson%27s_equation
same_as:
  wikidata: Q827688
  wikipedia: Poisson's equation
---

## Summary

Poisson's equation is the partial differential equation $\Delta u = f$, where $\Delta$ is the [[Laplacian|0E0B6RA8K0]] and $f$ is a given function.
With $f = 0$ it is [[Laplace's equation|S8RG6N1PRT]], so it is the inhomogeneous version of the equation of harmonic functions.
It describes a potential created by a source: the gravitational potential of a mass density, or the electrostatic potential of a charge density.
On the whole space a solution is given by convolving $f$ with the [[fundamental solution of the Laplacian|BSJ8X2XRN9]].
On bounded domains it is solved with Green's functions.

## Explanations

### L1 human

Laplace's equation describes a steady state with no sources inside, such as the temperature in a plate with no heater.
Poisson's equation allows sources: the right-hand side $f$ says how much heat is produced, or how much charge sits, at each point.
For example, $u = (x^2 + y^2)/4$ solves $\Delta u = 1$ in the plane, a constant source everywhere.
Two solutions differ by a harmonic function, so on a bounded domain the boundary values pin down a single solution.
