---
tag: 1V2N8MFSHC
kind: concept
name: Riesz potential
msc: [31B15, 47G40, 26A33]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz_potential
same_as:
  wikidata: Q7333166
  wikipedia: Riesz potential
---

## Summary

The Riesz potential of order $\alpha$, for $0 < \alpha < n$, is the operator $I_\alpha$ that convolves a function on $\R^n$ with a constant multiple of $\abs{x}^{\alpha - n}$.
It is the inverse of the [[fractional Laplacian|F8RSNQBMBE]] $(-\Delta)^{\alpha/2}$, so it integrates a function to the fractional order $\alpha$.
For $\alpha = 2$ and $n \ge 3$ it is, up to a constant factor, the [[Newtonian potential|DCMFQ01QGS]], which solves Poisson's equation.
Its main estimate is the [[Hardy–Littlewood–Sobolev inequality|HG65C9R1SP]], which underlies the Sobolev embedding theorem.

## Explanations

### L1 human

Taking a derivative makes a function rougher, and integrating makes it smoother.
The Riesz potential is a way to integrate "a fraction of a time" in several variables.
It averages the function with a weight $\abs{x - y}^{\alpha - n}$ that is large near $x$ and decays with distance.
The larger $\alpha$ is, the slower the decay and the smoother the result.
In $\R^3$ with $\alpha = 2$ the weight is $1/\abs{x - y}$, the gravitational potential of a point mass.
