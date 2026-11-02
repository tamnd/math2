---
tag: 74BPYJNZTM
kind: concept
name: Unitary representation
msc: ["22D10", "43A65"]
specializes: [WYGRXCG2RN]
sources:
  - url: https://en.wikipedia.org/wiki/Unitary_representation
same_as:
  wikidata: Q10359539
  wikipedia: Unitary representation
---

## Summary

A unitary representation of a [[topological group|92700QAB5Y]] $G$ is a homomorphism from $G$ to the [[unitary operators|MM0EJ2GDE4]] on a [[Hilbert space|HM2HHE3J51]].
It must be continuous in the strong operator topology.
It is the kind of [[group representation|WYGRXCG2RN]] used for infinite groups in analysis and physics, because unitary operators preserve lengths and angles.
Harmonic analysis on a locally compact group is largely the study of its unitary representations.
In quantum mechanics, symmetry groups act on state spaces in this way.

## Explanations

### L1 human

A unitary operator is a rotation of a possibly infinite-dimensional space: it keeps all lengths and angles.
A unitary representation assigns such a rotation to each element of a group, so that the product of two elements goes to the composition of their rotations.
For example, the real line acts on the space $L^2(\R)$ of square-integrable functions by shifting: the number $t$ sends $f$ to the function $x \mapsto f(x - t)$.
Shifting does not change the integral of $\abs{f}^2$, so each shift is unitary, and shifting by a small amount changes $f$ only a little.
