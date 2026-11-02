---
tag: 1C2TEAKJHJ
kind: concept
name: Parry measure
msc: [37B10, 37A35]
specializes: [B232EZ1FMB]
sources:
  - url: https://en.wikipedia.org/wiki/Subshift_of_finite_type
---

## Summary

The Parry measure is a special shift-[[invariant measure|B232EZ1FMB]] on an irreducible [[subshift of finite type|624XDXX8FN]].
It is the unique invariant probability measure of maximal entropy.
So its [[Kolmogorov–Sinai entropy|X1D1C7VH6P]] equals the [[topological entropy|BDZYBXBFDE]] $\log \lambda$, where $\lambda$ is the Perron eigenvalue of the transition matrix.
It is a Markov measure built from the left and right Perron eigenvectors.
It shows the [[variational principle for entropy|HHR8HP3R6G]] at work in the simplest case.

## Explanations

### L1 human

A subshift of finite type allows some words and forbids others.
Among all ways to pick an allowed sequence at random, the Parry measure is the one that is as unpredictable as possible.
It does not give each symbol equal weight; it weights them by how many long allowed words pass through them.
For the golden mean shift, where $11$ is forbidden, it gives the symbol $0$ probability $\varphi^2/(\varphi^2 + 1)$, with $\varphi$ the golden ratio.
See the [[definition|BE3E2AH0EV]].
