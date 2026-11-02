---
tag: EETVA6QYX4
kind: concept
name: Dirichlet boundary condition
msc: [34B05, 35J25]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_boundary_condition
same_as:
  wikidata: Q1193699
  wikipedia: Dirichlet boundary condition
---

## Summary

A Dirichlet boundary condition prescribes the values of the unknown function on the boundary of the domain.
For an ordinary differential equation on $[a, b]$, it fixes $y(a)$ and $y(b)$.
For a partial differential equation on a domain $\Omega$, it fixes $u$ on the boundary $\partial \Omega$.
It is the most common type of condition in a [[boundary value problem|TM8VQJWGHZ]], next to the Neumann and Robin conditions.
See the [[definition|G3XFT0MWKH]].

## Explanations

### L1 human

A Dirichlet condition says what the solution must be at the edges.
A string with both ends nailed at height $0$ satisfies $y(a) = y(b) = 0$.
A metal plate whose edge is held at a fixed temperature gives a Dirichlet condition for the heat equation.
For $y'' = 0$ on $[0, 1]$ with $y(0) = 1$ and $y(1) = 3$, the solution is the straight line $y = 1 + 2x$.
