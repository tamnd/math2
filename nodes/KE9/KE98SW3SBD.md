---
tag: KE98SW3SBD
kind: concept
name: Preconditioner
msc: [65F08, 65F10]
sources:
  - url: https://en.wikipedia.org/wiki/Preconditioner
same_as:
  wikidata: Q1754327
  wikipedia: Preconditioner
---

## Summary

A preconditioner for a linear system $A x = b$ is an invertible matrix $P$ that is close to $A$ in a suitable sense.
Systems $P z = r$ must be cheap to solve.
One replaces the system by $P^{-1} A x = P^{-1} b$, or by a similar transformed system.
The new matrix has a smaller [[condition number|AB3S6MHJ8X]] or better clustered eigenvalues.
Iterative methods then converge in far fewer steps.
For large sparse systems, the choice of preconditioner usually matters more than the choice of iterative method.

## Explanations

### L1 human

An iterative solver is slow when the matrix is badly scaled or ill-conditioned.
A preconditioner is a cheap rough approximation of the matrix that is easy to invert.
Applying its inverse first turns the problem into a nicer one with the same solution.
The simplest example is the diagonal of $A$: dividing each equation by its diagonal entry often helps already.
