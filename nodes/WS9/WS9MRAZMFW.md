---
tag: WS9MRAZMFW
kind: concept
name: Costate equation
msc: [49K15, 93C15]
sources:
  - url: https://en.wikipedia.org/wiki/Costate_equation
same_as:
  wikidata: Q5175070
  wikipedia: Costate equation
---

## Summary

The costate equation is the differential equation satisfied by the multipliers, or costates, of an optimal control problem along an optimal trajectory.
It reads $p' = -\partial H / \partial x$, where $H$ is the [[Hamiltonian of the problem|RACVWG5QTK]].
Together with the state equation $x' = \partial H / \partial p$ it forms a Hamiltonian system in [[Pontryagin's maximum principle|7RPV2T29CF]].
It is affine in $p$, and its linear part is the adjoint of the linearized state equation.

## Explanations

### L1 human

The costate $p(t)$ tells how much the optimal remaining cost would change if the state at time $t$ were nudged.
It is like a price that changes with time.
The costate equation says how this price evolves, and it is usually solved backward from the final time.
For example, if nothing in the cost or dynamics depends on the state, the price stays constant.
