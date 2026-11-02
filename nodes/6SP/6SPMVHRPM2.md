---
tag: 6SPMVHRPM2
kind: concept
name: Rigged Hilbert space
msc: [46C99, 46A11, 81Q10]
sources:
  - url: https://en.wikipedia.org/wiki/Rigged_Hilbert_space
same_as:
  wikidata: Q1262627
  wikipedia: Rigged Hilbert space
---

## Summary

A rigged Hilbert space, or Gelfand triple, is a chain $\Phi \subset H \subset \Phi'$.
Here $H$ is a Hilbert space, $\Phi$ is a dense subspace with a finer topology, and $\Phi'$ is the dual of $\Phi$.
It gives a rigorous home to objects such as the Dirac delta and plane waves, which are not vectors of $H$.
With a nuclear space $\Phi$, it carries the spectral theorem in terms of generalized eigenvectors.

## Explanations

### L1 human

Quantum mechanics likes to speak of states of exact position, but such states are not square-integrable functions.
A rigged Hilbert space adds a small space of very nice functions and a large space of generalized functions around the Hilbert space.
The usual example is Schwartz functions inside $L^2(\R)$ inside tempered distributions.
The delta function $\delta_a$ lives in the large space and is an eigenvector of the position operator there.
