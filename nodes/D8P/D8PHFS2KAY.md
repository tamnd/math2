---
tag: D8PHFS2KAY
kind: concept
name: Positive solutions of integral equations
msc: [45M20, 47B65]
sources:
  - url: https://en.wikipedia.org/wiki/Krein%E2%80%93Rutman_theorem
---

## Summary

A positive solution of an [[integral equation|R3SG1SN7JQ]] is a solution that is nonnegative and not identically zero, or in a stronger sense strictly positive.
In models of densities, concentrations, populations or probabilities only such solutions have a meaning, so existence of a positive solution is often the real question.
The main tools are order methods: the cone of nonnegative functions, [[positive operators|77020CY5ZW]] that map it into itself, and monotone iteration.
Fixed point and eigenvalue theorems on cones, such as the [[Krein–Rutman theorem|VADXDK3TKM]], complete the toolbox.
For linear equations with nonnegative kernels, positivity is closely tied to the spectral radius of the integral operator.

## Explanations

### L1 human

If the unknown is a density of particles, a negative value makes no sense, so one wants solutions that are never negative.
Integral operators with nonnegative kernels send nonnegative functions to nonnegative functions, and this helps.
But it is not enough: $\varphi(x) = 1 + 2\int_0^1 \varphi(t) \, dt$ on $[0, 1]$ has the unique solution $\varphi = -1$, although all its data are positive.
The trouble is that the integral term is too strong; with the factor $\frac12$ instead of $2$, the solution is $\varphi = 2$.
