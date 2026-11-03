---
tag: PR8C073VWY
kind: concept
name: Left regular representation
msc: ["22D10", "43A65"]
specializes: [74BPYJNZTM]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_representation
---

## Summary

The left regular representation of a locally compact group is the action of the group on square-integrable functions on itself by left translation.
It is a [[unitary representation|74BPYJNZTM]], and it contains, in a suitable sense, the irreducible representations that matter for harmonic analysis on the group.
Its decomposition into irreducibles is the content of Plancherel theorems.
Many properties of the group, such as [[amenability|CEAT9BESKK]], can be read off from it.

## Explanations

### L1 human

A group acts on itself by multiplying on the left, and so it acts on functions defined on the group by moving their graphs.
Translation does not change the integral of $\abs{f}^2$, so this action is by unitary operators.
For the circle, the translations of functions are rotations, and Fourier series break this action into one-dimensional pieces $e^{in\theta}$.
For a finite group, the regular representation contains every irreducible representation, each as many times as its dimension.
