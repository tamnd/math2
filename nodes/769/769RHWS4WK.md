---
tag: 769RHWS4WK
kind: concept
name: Mutually unbiased bases
msc: [81P55, 81P18, 05B25]
sources:
  - url: https://en.wikipedia.org/wiki/Mutually_unbiased_bases
same_as:
  wikidata: Q17160413
  wikipedia: Mutually unbiased bases
---

## Summary

Two orthonormal bases of $\C^d$ are mutually unbiased if every vector of one has the same overlap with every vector of the other.
A measurement in one basis then gives no information about a state prepared in the other.
At most $d + 1$ such bases exist, and $d + 1$ exist when $d$ is a prime power.
They are used in quantum key distribution and in state tomography.

## Explanations

### L1 human

For a qubit, the eigenbases of the three Pauli matrices are mutually unbiased.
If a qubit is prepared as $\lvert 0 \rangle$ and measured in the basis $(\lvert 0 \rangle \pm \lvert 1 \rangle)/\sqrt2$, the two outcomes are equally likely.
So knowing the answer in one basis says nothing about the answer in the other.
This is the property that the BB84 key distribution protocol uses.
Whether a full set of $7$ such bases exists in dimension $6$ is a famous open problem.
