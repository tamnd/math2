---
tag: 10WBPH9ANN
kind: concept
name: Cahn–Hilliard–Navier–Stokes diffuse interface model
msc: [76T06, 35Q35]
specializes: [A3Q9SNF86Q]
sources:
  - url: https://en.wikipedia.org/wiki/Cahn%E2%80%93Hilliard_equation
---

## Summary

The Cahn–Hilliard–Navier–Stokes model describes the flow of two immiscible incompressible fluids with an interface of small but positive thickness.
A phase field $\phi$ takes values near $+1$ in one fluid and near $-1$ in the other, and it varies smoothly across the interface.
The phase field evolves by the [[Cahn–Hilliard equation|DKN15NVKSB]] with an extra transport by the flow.
The flow obeys the [[Navier–Stokes equations|18KXZHVF4M]] with a capillary force coming from the phase field.
The model handles the breakup and merging of drops without tracking the interface explicitly; with matched densities it is known as model H.

## Explanations

### L1 human

Instead of a sharp line between oil and water, imagine a very thin blurred zone where one fluid turns into the other.
A single number at each point, the phase field, says how much of each fluid is there.
The fluids move the blurred zone along, and the zone in turn pulls on the fluids the way surface tension does.
Because nothing is sharp, drops can split and merge without any special treatment, which makes the model popular in computer simulations.
