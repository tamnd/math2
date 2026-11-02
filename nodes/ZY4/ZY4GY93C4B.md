---
tag: ZY4GY93C4B
kind: concept
name: Riemann solver
msc: [65M08, 35L65]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_solver
same_as:
  wikidata: Q6153788
  wikipedia: Riemann solver
---

## Summary

A Riemann solver is a procedure that computes, exactly or approximately, the solution of a [[Riemann problem|GJWKX22VVE]] for a [[hyperbolic conservation law|XN081NCPF5]].
In numerical schemes it computes the flux between two neighbouring cells from the two cell values.
It is the main ingredient of [[Godunov's scheme|43HZJ7DRT0]] and of the higher-order schemes built on it.
Exact solvers are expensive for systems such as the Euler equations, so approximate solvers such as the [[Roe solver|TNM5CFSZM6]] and the HLL solver are common.
See the [[definition|9PTJWSCFS5]].

## Explanations

### L1 human

At each wall between two cells of a grid, the state on the left differs from the state on the right.
A Riemann solver answers one question: if these two constant states meet at time zero, what flows through the wall just after?
Doing this at every wall tells the scheme how much of each conserved quantity moves from cell to cell.
For the transport equation $u_t + a u_x = 0$ with $a > 0$, the answer is simple: the left state moves through the wall, and the flux is $a u_l$.
