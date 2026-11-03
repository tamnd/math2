---
tag: 9WC6A9VMZD
kind: concept
name: Markov parameters and the Hankel matrix of a system
msc: [93B15, 93B20, 15B05]
sources:
  - url: https://en.wikipedia.org/wiki/Realization_(systems)
---

## Summary

The Markov parameters of a linear time-invariant system are the coefficients of the expansion of its [[transfer function|86JKV3TRFD]] in powers of $1/s$.
For a state-space model $(A, B, C, D)$ they are $D$ and the matrices $C A^{k-1} B$, and in discrete time they are the values of the impulse response.
Arranged in a block [[Hankel matrix|PQ1D8FQB3E]], they encode the whole input-output behaviour.
The rank of this Hankel matrix is the dimension of a [[minimal realization|3SNPPX5SAZ]], which makes it the starting point of realization and identification algorithms.

## Explanations

### L1 human

In discrete time, hit a system with a single unit pulse and record what comes out at each step: these numbers are the Markov parameters.
Write them in a table where each row is the row above shifted by one step.
If the system has only a few internal states, this table has small rank, because later responses are combinations of earlier ones.
In continuous time they are the coefficients of the transfer function in powers of $1/s$: for $G(s) = 1/(s + 1)$ they are $1, -1, 1, -1, \ldots$ after the constant term $0$.
Their table has rank $1$, matching the single state of $x' = -x + u$.
