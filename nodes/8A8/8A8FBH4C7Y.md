---
tag: 8A8FBH4C7Y
kind: concept
name: Regularity of minimizers
msc: [49N60, 35J50, 35B65]
specializes: [N383CX7WKS]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%27s_nineteenth_problem
---

## Summary

Regularity of minimisers is the study of how smooth the minimisers of a variational problem are.
The direct method produces minimisers only in a Sobolev space, so it is a separate question whether they are continuous, differentiable, smooth or analytic.
It is the subject of [[Hilbert's nineteenth problem|QPMM2ZPWBW]], solved for scalar problems by the [[De Giorgi–Nash–Moser theorem|32C3D8FG9V]].
For vector-valued problems minimisers can be singular, and the theory proves partial regularity: smoothness outside a small closed set.
It is a central part of [[regularity theory|N383CX7WKS]] for elliptic equations.

## Explanations

### L1 human

Existence proofs in the calculus of variations give a minimiser that might have kinks, jumps in its derivative, or worse.
Regularity theory asks whether these defects really occur.
For the Dirichlet energy $\int \abs{\nabla u}^2 \, dx$ the minimisers are harmonic functions, which are smooth, even analytic, inside the domain.
For many energies of maps with several components, singular minimisers do exist; then one shows that the bad points form a small set.
