---
tag: DAVT2ZWAF7
kind: concept
name: Solving linear difference equations by the Z-transform
msc: [39A06, 44A55]
sources:
  - url: https://en.wikipedia.org/wiki/Z-transform
    locator: Linear constant-coefficient difference equation
---

## Summary

The Z-transform method solves a [[linear recurrence with constant coefficients|0NDVHBVBXB]] with given initial values.
One applies the [[unilateral Z-transform|EPG6JPVJE7]] to the equation, solves the resulting algebraic equation for the transform of the unknown, and inverts.
The initial values enter by themselves through the [[shift property|JWH2KYCGBQ]].
It is the discrete analogue of the Laplace transform method for linear differential equations.

## Explanations

### L1 human

A recurrence such as $y_{n+2} = y_{n+1} + y_n$ ties each term to earlier ones.
After the Z-transform, each shift becomes multiplication by $z$, so the recurrence becomes an equation that one solves with ordinary algebra.
The answer is a rational function of $z$.
Splitting it into simple fractions and reading each one back as a geometric sequence gives a closed formula for $y_n$.
