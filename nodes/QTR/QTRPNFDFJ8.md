---
tag: QTRPNFDFJ8
kind: concept
name: Natural boundary condition
msc: [49K05, 49K10, 35A15]
sources:
  - url: https://en.wikipedia.org/wiki/Calculus_of_variations
---

## Summary

A natural boundary condition is a boundary condition that a minimiser satisfies automatically at an end where no value is prescribed.
For $J(y) = \int_a^b L(x, y, y') \, dx$ with $y(b)$ free, it reads $L_p = 0$ at $x = b$.
It comes from the [[first variation|5B8NFYB2XQ]], not from the statement of the problem.
For the Dirichlet energy in several variables, it is the [[Neumann boundary condition|GS3KT2H645]].

## Explanations

### L1 human

If one end of a curve is free to move up and down, the best curve has to be best also with respect to that freedom.
This gives an extra condition at the free end, which nobody imposed by hand.
Think of a hanging string with one end on a frictionless vertical rail.
The rail cannot push along the string, so the string settles with its end meeting the rail at a right angle.
