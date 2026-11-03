---
tag: V1JTB52E8C
kind: concept
name: Density matrix
msc: ["81P16", "47B10", "46N50"]
specializes: [Z2CP530WDE]
sources:
  - url: https://en.wikipedia.org/wiki/Density_matrix
same_as:
  wikidata: Q831774
  wikipedia: Density matrix
---

## Summary

A density matrix, or density operator, is a positive [[trace class operator|Z2CP530WDE]] of trace $1$ on a complex Hilbert space.
It describes a general [[quantum state|4NQN47A92F]], pure or [[mixed|CKCMBP5S2P]].
The expectation value of a bounded observable $A$ in the state $\rho$ is $\operatorname{tr}(\rho A)$.
Density matrices are needed for statistical ensembles and for the state of a subsystem of a larger system.

## Explanations

### L1 human

A state vector describes a quantum system that is prepared exactly.
When the preparation is random, one averages the projections onto the possible state vectors, weighted by their probabilities, and gets a density matrix.
In finite dimension it is a Hermitian matrix with eigenvalues $\ge 0$ that add up to $1$.
The eigenvalues are the probabilities of the pure states that make up the mixture along the eigenvectors.
For a spin prepared "up" with probability $3/4$ and "down" with probability $1/4$, the density matrix is $\mathrm{diag}(3/4, 1/4)$.
