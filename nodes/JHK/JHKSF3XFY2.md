---
tag: JHKSF3XFY2
kind: concept
name: Potential of a measure
msc: [31C15, 31B15]
sources:
  - url: https://en.wikipedia.org/wiki/Potential_theory
---

## Summary

The potential of a measure $\mu$ with respect to a kernel $k$ is the function $x \mapsto \int k(x, y) \, d\mu(y)$.
It describes the field of a distribution of mass or charge $\mu$.
Here $k(x, y)$ is the effect at $x$ of a unit mass at $y$.
With the [[Newtonian kernel|6TJTWQ5HCR]] one gets the Newtonian potential, with the [[logarithmic kernel|VDZ5FKYC2T]] the logarithmic potential, and with $\abs{x - y}^{\alpha - n}$ the Riesz potentials.
Energy, capacity, equilibrium measures and balayage are all defined through potentials of measures.

## Explanations

### L1 human

Spread some mass over space, perhaps unevenly.
Each small piece of mass creates a small potential around it, given by the kernel.
The potential of the whole measure is the sum of all these small contributions, which is an integral.
For a single point mass at $a$, the potential is just $k(x, a)$.
