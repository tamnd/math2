---
tag: 8EV1G2Y6CC
kind: concept
name: Painlevé property
msc: [34M55, 34M04]
sources:
  - url: https://en.wikipedia.org/wiki/Painlev%C3%A9_transcendents
---

## Summary

An ordinary differential equation in the complex domain has the Painlevé property if its movable singularities are poles.
Here a singularity of a solution is movable when its position depends on the initial data.
Linear equations have it, since their solutions can be continued along every path that avoids the singular points of the coefficients.
Nonlinear equations with the property are rare, and Painlevé and his school classified those of second order of a certain rational type.
Six new equations appeared in this classification, the Painlevé equations, whose solutions define new special functions.
See the [[definition|H2E8KW6DB5]].

## Explanations

### L1 human

Solutions of nonlinear equations can blow up at places that move when the starting value changes.
For $y' = y^2$, the solution $y = \frac{1}{c - z}$ has a pole at $z = c$, and $c$ depends on the starting value.
A pole is harmless: the solution stays single-valued around it.
For $y' = y^3$, the solutions behave like $(c - z)^{-1/2}$, a square root, which branches at a moving point.
The Painlevé property forbids such moving branch points, so the solutions can be continued as single-valued meromorphic functions on suitable domains.
