---
tag: 43HZJ7DRT0
kind: concept
name: Godunov's scheme
msc: [65M08, 35L65, 65M06]
sources:
  - url: https://en.wikipedia.org/wiki/Godunov%27s_scheme
same_as:
  wikidata: Q4291826
  wikipedia: Godunov's scheme
---

## Summary

Godunov's scheme is a finite volume method for hyperbolic systems of [[conservation laws|8RA7AMWSAF]].
It stores cell averages, solves the [[Riemann problem|GJWKX22VVE]] exactly at each cell interface, and averages the result again.
It is conservative, first-order accurate, and captures shocks without spurious oscillations.
Its idea of using Riemann solvers is the basis of many modern high-resolution schemes.
See the [[definition|FBJ4JCP5SR]].

## Explanations

### L1 human

Divide the line into cells and keep only the average of the solution in each cell.
At each cell boundary two constant values meet, and the exact evolution of such a jump is known.
Let these jumps evolve for one short time step, then compute the new average in each cell.
For the equation $u_t + a u_x = 0$ with $a > 0$, this gives the upwind scheme, which takes information from the left neighbour.
