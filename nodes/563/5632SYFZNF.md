---
tag: 5632SYFZNF
kind: concept
name: Oseen equations
msc: [76D07, 35Q35]
sources:
  - url: https://en.wikipedia.org/wiki/Oseen_equations
same_as:
  wikidata: Q2033185
  wikipedia: Oseen equations
---

## Summary

The Oseen equations are a linear approximation of the [[Navier–Stokes equations|18KXZHVF4M]] for a slow viscous flow past a body that moves with constant velocity.
They keep the convection of the disturbance by the uniform stream, which the [[Stokes equations|13CB7V2YM4]] drop.
Carl Wilhelm Oseen introduced them in 1910 to correct the Stokes approximation far from the body.

## Explanations

### L1 human

Near a small slow body, viscosity dominates, and the Stokes equations are accurate.
Far away, the main effect is that the fluid streams past at constant speed and carries the disturbance downstream.
The Oseen equations keep both effects and stay linear.
They predict a wake behind the body, which the Stokes equations miss, and they resolve [[Stokes' paradox|M1KHFRHCC1]] for a cylinder.
