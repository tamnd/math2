---
tag: VDQ32JT7ZS
kind: concept
name: Random integral equation
msc: [45R05, 60H20, 45A05]
specializes: [R3SG1SN7JQ]
sources:
  - url: https://en.wikipedia.org/wiki/Stochastic_differential_equation
---

## Summary

A random integral equation is an [[integral equation|R3SG1SN7JQ]] whose kernel, forcing term or both depend on a random parameter.
For each outcome of the randomness one gets an ordinary integral equation, and the solution is a [[stochastic process|0QH5ENKZM1]].
The basic questions are existence, uniqueness and measurability of such random solutions, and the laws of the solutions.
Such equations model systems with uncertain coefficients, such as materials with random properties.
They differ from stochastic integral equations with Itô integrals, where the integral against a [[Wiener process|22735FGJV6]] is not defined path by path.

## Explanations

### L1 human

Suppose that the coefficients of an integral equation are measured with uncertainty and are modelled as random variables.
For each possible value of the coefficients the equation has a solution, so the solution itself is random.
For example, with a random number $Y$ between $0$ and $1$, the equation $x(t) = 1 + \frac{Y}{2} \int_0^1 x(s) \, ds$ has the solution $x(t) = 2/(2 - Y)$.
The solution is a random variable, and one can ask for its mean or its distribution.
