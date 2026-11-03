---
tag: GBDFSDV23C
kind: concept
name: Norm residue symbol
msc: [11S31, 19F15]
sources:
  - url: https://en.wikipedia.org/wiki/Symbol_(number_theory)
---

## Summary

Let $K$ be a local field that contains the group $\mu_n$ of $n$-th roots of unity.
The norm residue symbol of degree $n$ is a pairing $(a, b)_n$ of two nonzero elements of $K$ with values in $\mu_n$.
It is defined with the reciprocity map of local class field theory, and $(a, b)_n = 1$ exactly when $a$ is a norm from $K(\sqrt[n]{b})$.
For $n = 2$ it is the Hilbert symbol.
It is a Steinberg symbol, so it factors through $K_2(K)$, and it is the local ingredient of the general reciprocity laws.

## Explanations

### L1 human

The Hilbert symbol asks whether a number is a norm from a quadratic extension, and answers with $\pm 1$.
The norm residue symbol does the same for extensions obtained by adjoining an $n$-th root, and answers with an $n$-th root of unity.
The answer $1$ means that $a$ is a norm.
Other roots of unity measure in a precise way how far $a$ is from being a norm.
