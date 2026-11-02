---
tag: M923VKQVZM
kind: concept
name: Nonlinear potential theory
msc: [31C45, 35J92]
specializes: [9PM8Q2E30Q]
sources:
  - url: https://en.wikipedia.org/wiki/P-Laplacian
---

## Summary

Nonlinear potential theory extends [[potential theory|9PM8Q2E30Q]] from the Laplace equation to nonlinear equations, above all the [[p-Laplace equation|XJMYGY0ZZF]].
Its objects are [[p-harmonic functions|7BKQT71FYZ]], $p$-superharmonic functions, $p$-capacities and nonlinear potentials such as the [[Wolff potential|EBD8TWFNS0]].
Without linearity there is no superposition, so the tools are variational methods, comparison principles and estimates instead of Green's functions.
Many classical results survive, including a Wiener criterion for regular boundary points.

## Explanations

### L1 human

Classical potential theory studies harmonic functions, which minimize the energy $\int \abs{\nabla u}^2$.
Nonlinear potential theory studies functions that minimize energies such as $\int \abs{\nabla u}^p$ with $p \ne 2$.
For these equations the sum of two solutions is no longer a solution, so a potential cannot be built by adding up the effects of point charges.
Even so, one can define the size of a set, its capacity, and decide which boundary points are well behaved, much as in the classical case.
The Wiener criterion for the $p$-Laplacian was proved sufficient by Maz'ya and necessary by Kilpeläinen and Malý.
