---
tag: E9WK6KJ4SM
kind: concept
name: Wave function
msc: ["81Q05", "81P16"]
specializes: [4NQN47A92F]
sources:
  - url: https://en.wikipedia.org/wiki/Wave_function
same_as:
  wikidata: Q2362761
  wikipedia: Wave function
---

## Summary

A wave function is a pure [[quantum state|4NQN47A92F]] written as a complex-valued square-integrable function, usually of the positions of the particles.
For one particle in $\R^n$, it is a function $\psi$ in [[$L^2(\R^n)$|SASP14MA1Z]] with $\int \abs{\psi}^2 = 1$, and $\abs{\psi(x)}^2$ is the [[probability density|0ZY9DX8FBF]] of the position.
Its time evolution is given by the [[Schrödinger equation|EPZR6H2WJN]].
Two wave functions that differ by a constant factor of modulus $1$ describe the same state.

## Explanations

### L1 human

The wave function assigns a complex number to each point of space.
Its squared modulus says how likely it is to find the particle near that point.
A wave function concentrated around one point describes a particle that is almost surely found there; a spread-out one describes a particle whose position is very uncertain.
For example, $\psi(x) = \pi^{-1/4} e^{-x^2/2}$ on the line gives the bell-shaped density $\pi^{-1/2} e^{-x^2}$, centred at $0$.
