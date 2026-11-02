---
tag: RCNY89A4NY
kind: concept
name: Semilinear PDE
msc: [35A99, 35J61, 35K58]
specializes: [7X9N9H3RK6]
sources:
  - url: https://en.wikipedia.org/wiki/Nonlinear_partial_differential_equation
---

## Summary

A semilinear PDE is a [[partial differential equation|GC5BDZ6QBC]] whose highest-order part is linear with coefficients depending only on the variables.
Its lower-order terms may be nonlinear.
The principal part, which decides the type of the equation, is then the same as for a linear equation.
Many models of physics and biology have this form, such as reaction–diffusion equations and nonlinear wave equations.
See the [[definition|X3P4TQZ9X2]].

## Explanations

### L1 human

Think of a linear equation such as the heat equation, and add a nonlinear source term that depends on the unknown itself.
For example, $\partial_t u = \partial_x^2 u + u(1 - u)$ is [[Fisher's equation|AXV2PH7FEZ]].
The second derivatives enter linearly, but the term $u(1 - u)$ does not.
Because the highest derivatives behave as in a linear equation, much of the linear theory still applies.
