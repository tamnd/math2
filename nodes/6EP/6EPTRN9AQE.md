---
tag: 6EPTRN9AQE
kind: concept
name: Boussinesq approximation for water waves
msc: [76B15, 35Q35]
sources:
  - url: https://en.wikipedia.org/wiki/Boussinesq_approximation_(water_waves)
same_as:
  wikidata: Q4950395
  wikipedia: Boussinesq approximation (water waves)
---

## Summary

The Boussinesq approximation for water waves is a family of model equations for long [[water waves|R9WC0Z7Z69]] of small amplitude in shallow water.
It keeps the leading effects of both nonlinearity and dispersion, assumed to be of the same small order, and drops the vertical coordinate.
The result is a system of equations in the horizontal variables only, which is far cheaper to solve than the full free boundary problem.
It contains the [[shallow water equations|NT73Y95RY5]] as its non-dispersive limit and leads to the [[Korteweg–de Vries equation|KTT75QC72Z]] for waves moving in one direction.

## Explanations

### L1 human

Near a beach, waves are long compared with the depth of the water.
In that case the water moves almost the same way at every depth, so one can describe it by its depth-averaged velocity.
The shallow water equations do this but forget that long and short waves travel at slightly different speeds.
Boussinesq's equations add back this small effect, and with it they can describe solitary waves that keep their shape.
