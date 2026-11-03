---
tag: H53TSRFWQ4
kind: concept
name: Von Neumann entropy
msc: [81P17, 94A17]
sources:
  - url: https://en.wikipedia.org/wiki/Von_Neumann_entropy
same_as:
  wikidata: Q6961323
  wikipedia: Von Neumann entropy
---

## Summary

The von Neumann entropy of a [[density matrix|V1JTB52E8C]] $\rho$ is $S(\rho) = -\tr(\rho \log \rho)$, the Shannon entropy of the eigenvalues of $\rho$.
It measures how mixed a quantum state is: it vanishes exactly on pure states and is largest for the maximally mixed state.
It is the quantum analogue of Shannon entropy and the basic quantity of quantum information theory.
For a pure bipartite state, the entropy of either reduced state measures its entanglement.

## Explanations

### L1 human

Entropy measures uncertainty.
A pure quantum state is known completely, so its entropy is $0$.
A qubit that is equally likely to be $|0\rangle$ or $|1\rangle$, with no coherence, has entropy $\log 2$, one bit, like a fair coin.
For a general state, one diagonalizes the density matrix and computes the Shannon entropy of its eigenvalues as if they were probabilities.
