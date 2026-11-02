---
tag: 5TRXQKP7DY
kind: concept
name: Hamilton–Jacobi equation
msc: [35F21, 70H20, 49L12]
specializes: [GC5BDZ6QBC]
sources:
  - url: https://en.wikipedia.org/wiki/Hamilton–Jacobi_equation
same_as:
  wikidata: Q1060137
  wikipedia: Hamilton–Jacobi equation
---

## Summary

A Hamilton–Jacobi equation is a first-order nonlinear [[partial differential equation|GC5BDZ6QBC]] of the form $u_t + H(\nabla u, x) = 0$, where $H$ is a given function called the Hamiltonian.
It comes from classical mechanics, where its solutions generate the motions of a [[Hamiltonian system|0EDKGA2FAK]].
It also appears in optimal control, geometric optics and front propagation.
Classical solutions usually stop existing after some time, and the right notion of global solution is the [[viscosity solution|H1ERJ3T75T]].
See the [[definition|4H1E4KW1JX]].

## Explanations

### L1 human

Imagine many travellers who all want to reach a goal as cheaply as possible.
Let $u(x, t)$ be the least cost of a journey that ends at the point $x$ at time $t$.
The Hamilton–Jacobi equation is the rule that this least cost must obey when one moves $x$ or $t$ a little.
For $H(p) = \abs{p}^2/2$ the equation reads $u_t + \tfrac12 \abs{\nabla u}^2 = 0$, and for example $u(x, t) = \abs{x}^2 / (2(t + 1))$ is a solution for $t > -1$.
