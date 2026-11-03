---
tag: 2S0MXDT4YH
kind: concept
name: Poisson bracket
msc: [53D05, 37J39, 70H05]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson_bracket
same_as:
  wikidata: Q1052775
  wikipedia: Poisson bracket
---

## Summary

The Poisson bracket is an operation $\{f, g\}$ on pairs of smooth functions on a [[symplectic manifold|CAN490EPRT]], built from their [[Hamiltonian vector fields|C5EH3B4BEP]].
It is antisymmetric, satisfies the Jacobi identity and the Leibniz rule, so it makes the functions into a [[Lie algebra|5JJYBJ6A8K]].
In mechanics it gives the time derivative of an observable along the motion, and its abstract properties lead to [[Poisson manifolds|A2KQ49Y4NF]] and to quantization.

## Explanations

### L1 human

In mechanics, a state is a point $(q, p)$ of positions and momenta, and an observable is a function of the state.
The Poisson bracket of two observables measures how one changes when the system flows along the energy defined by the other.
On the plane, $\{f, g\} = \frac{\partial f}{\partial q} \frac{\partial g}{\partial p} - \frac{\partial f}{\partial p} \frac{\partial g}{\partial q}$.
For example $\{q, p\} = 1$, which is the classical shadow of the quantum rule that position and momentum do not commute.
A quantity $g$ is conserved by the motion with energy $H$ exactly when $\{g, H\} = 0$.
