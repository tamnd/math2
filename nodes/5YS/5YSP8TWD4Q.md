---
tag: 5YSP8TWD4Q
kind: concept
name: Rayleigh–Ritz method
msc: [49R05, 65N25, 65F15]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh%E2%80%93Ritz_method
same_as:
  wikidata: Q852247
  wikipedia: Rayleigh–Ritz method
---

## Summary

The Rayleigh–Ritz method approximates the [[eigenvalues|0BQAA2BK3Q]] of a self-adjoint operator by restricting its [[Rayleigh quotient|06WHP8SE98]] to a finite-dimensional space of trial vectors.
This reduces the problem to a small matrix eigenvalue problem.
By the [[min-max theorem|G11NE3AT6E]], each approximate eigenvalue is an upper bound for the corresponding true one, and the bounds improve as the trial space grows.
The method underlies the finite element computation of vibration modes and many iterative eigenvalue solvers.

## Explanations

### L1 human

The lowest frequency of a vibrating string or drum is the smallest value of an energy ratio over all possible shapes.
If you only try a few shapes, you get a number that is too large, but often close.
The Rayleigh–Ritz method tries all combinations of a few chosen shapes at once and solves a small matrix problem for the best ones.
For a string of length $1$ fixed at both ends, the single trial shape $x(1 - x)$ gives $10$, close to the true value $\pi^2 \approx 9.87$.
