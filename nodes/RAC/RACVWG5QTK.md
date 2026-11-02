---
tag: RACVWG5QTK
kind: concept
name: Hamiltonian of an optimal control problem
msc: [49K15, 93C15]
sources:
  - url: https://en.wikipedia.org/wiki/Hamiltonian_(control_theory)
same_as:
  wikidata: Q5645293
  wikipedia: Hamiltonian (control theory)
---

## Summary

The Hamiltonian of an optimal control problem is a function that combines the dynamics and the running cost with a vector of multipliers, the costate.
It has the form $H = p \cdot f - \lambda_0 L$, or $H = L + p \cdot f$ in the sign convention of the minimum principle.
[[Pontryagin's maximum principle|7RPV2T29CF]] says that an optimal control maximizes the Hamiltonian at almost every time.
It plays the role that the Hamiltonian of [[Hamiltonian systems|0EDKGA2FAK]] plays in mechanics.

## Explanations

### L1 human

The Hamiltonian is a bookkeeping device that weighs the immediate cost of a control against its effect on the future.
The costate $p$ acts as a price for each unit of change in the state.
A control is good at an instant if it gives a high value of "price times rate of change minus cost".
For example, for $x' = u$ with cost $\int u^2/2 \, dt$, the Hamiltonian is $H = p u - u^2/2$, which is largest at $u = p$.
