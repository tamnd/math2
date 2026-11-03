---
tag: VZACRS73RY
kind: concept
name: Controllable canonical form
msc: [93B10, 93B17, 93C05]
sources:
  - url: https://en.wikipedia.org/wiki/State-space_representation
---

## Summary

The controllable canonical form is a standard state-space model of a single-input single-output linear system, read off directly from the coefficients of its [[transfer function|86JKV3TRFD]].
Its state matrix is a [[companion matrix|0ZCWPNZTQ3]] of the denominator, and its input matrix is the last standard basis vector.
Its output matrix lists the coefficients of the numerator.
A model in this form is always [[controllable|A9WFM77Z4P]], and every controllable single-input system can be brought to this form by a change of coordinates.
It makes pole placement by state feedback a direct computation.

## Explanations

### L1 human

A transfer function is a fraction of two polynomials in $s$.
The controllable canonical form turns this fraction into differential equations that form a chain.
Each state variable is the derivative of the previous one, and the input drives the last one.
The denominator fills the last row of the matrix, and the numerator says how to combine the states into the output.
For $G(s) = 1/(s^2 + 3s + 2)$, the form is $x_1' = x_2$, $x_2' = -2 x_1 - 3 x_2 + u$, $y = x_1$.
