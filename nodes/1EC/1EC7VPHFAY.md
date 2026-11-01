---
tag: 1EC7VPHFAY
kind: concept
name: Malliavin calculus
msc: [60H07]
sources:
  - url: https://en.wikipedia.org/wiki/Malliavin_calculus
same_as:
  wikidata: Q6744166
  wikipedia: Malliavin calculus
---

## Summary

Malliavin calculus is a differential calculus for random variables that are functions of a [[Brownian motion|22735FGJV6]] path.
Its basic operator is the Malliavin derivative $D$, which measures how a random variable changes when the path is perturbed in directions of finite energy.
Its adjoint is the Skorokhod integral, which extends the [[Itô integral|JA95NH206E]] to integrands that are not adapted.
It is used to prove that laws of solutions of stochastic differential equations have smooth densities, and to compute sensitivities in finance.

## Explanations

### L1 human

A random variable built from a Brownian path is a function on the space of all paths, an infinite-dimensional space.
Malliavin calculus defines derivatives of such functions, much like partial derivatives in many variables.
For example, the value $B_T$ of the path at time $T$ has derivative $1$ at each time $t \le T$.
Indeed, a small push of the path at time $t$ moves $B_T$ by the same amount.
An integration by parts formula then turns questions about densities into questions about expectations.
