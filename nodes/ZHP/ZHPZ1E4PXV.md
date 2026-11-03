---
tag: ZHPZ1E4PXV
kind: concept
name: Transonic small disturbance equation
msc: [76H05, 35M10]
specializes: [GC5BDZ6QBC]
sources:
  - url: https://en.wikipedia.org/wiki/Transonic
---

## Summary

The transonic small disturbance equation is the simplest model of steady [[transonic flow|20G6N8JGEH]] past a thin body.
It is a nonlinear partial differential equation for the perturbation potential.
It keeps the one nonlinear term that matters when the free stream Mach number is close to $1$.
It is elliptic where the flow is subsonic and hyperbolic where it is supersonic, so it changes type across the sonic line.
It was used in early numerical computations of transonic flows with shocks.

## Explanations

### L1 human

Near the speed of sound, the simple linear rules for slow flow break down, because the speed of sound itself changes with the flow.
The transonic small disturbance equation fixes this with one extra term that lets the type of the equation switch between "smooth spreading" and "wave travelling" depending on the local speed.
It assumes that the body is thin, so that it disturbs the air only a little.
For example, it can describe the supersonic pocket and shock over a thin wing at Mach $0.85$.
