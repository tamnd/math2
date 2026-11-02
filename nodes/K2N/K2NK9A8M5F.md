---
tag: K2NK9A8M5F
kind: concept
name: Fundamental solution
msc: [35A08, "35E05"]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_solution
same_as:
  wikidata: Q1474123
  wikipedia: Fundamental solution
---

## Summary

A fundamental solution of a linear differential operator $P$ is a distribution $E$ with $P E = \delta$, the Dirac delta at the origin.
For an operator with constant coefficients, convolving $E$ with a source $f$ gives a solution of $P u = f$.
Fundamental solutions are the Green's functions of the whole space, and they underlie potential theory, the [[heat kernel|KD404MF042]] and the theory of wave propagation.
See the [[definition|ZY724M2NKQ]].

## Explanations

### L1 human

A fundamental solution is the response of a physical system to a point source.
For gravity or electrostatics in space, the potential of a point mass is proportional to $1/\abs{x}$.
Up to a constant factor, this function is the fundamental solution of the Laplace operator.
A general mass distribution is a sum of point masses, so its potential is a sum, or integral, of shifted copies of $1/\abs{x}$.
That is why one fundamental solution solves the equation for all sources.
