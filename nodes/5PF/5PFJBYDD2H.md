---
tag: 5PFJBYDD2H
kind: concept
name: Discrete Painlevé equations
msc: [39A36, 34M55, 37K60]
sources:
  - url: https://en.wikipedia.org/wiki/Painlev%C3%A9_transcendents
---

## Summary

Discrete Painlevé equations are integrable nonlinear second-order difference equations that play the role of the [[Painlevé equations|AZ17JCMRKB]] for recurrences.
They are non-autonomous, and in a suitable continuum limit they tend to one of the six Painlevé differential equations.
Their integrability shows up as singularity confinement, as a Lax pair of linear problems, and as a description by birational maps of rational surfaces.
They arose in the theory of orthogonal polynomials and random matrix models, where recurrence coefficients satisfy them.

## Explanations

### L1 human

The Painlevé equations are special nonlinear differential equations whose solutions behave unusually well.
Discrete Painlevé equations are recurrences with the same good behaviour: each new term is a rational function of the two previous ones and of the step number.
A typical one is $x_{n+1} + x_n + x_{n-1} = (\alpha n + \beta)/x_n + \gamma$, with constants $\alpha, \beta, \gamma$.
If a term happens to be $0$, the next terms blow up for a moment, but the recursion recovers after a few steps instead of losing information.
