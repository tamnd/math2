---
tag: 3039GWNHWS
kind: concept
name: Higher-order differences
msc: [39A70, 39A12]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_difference
---

## Summary

Higher-order differences are obtained by applying a difference operator several times.
The $n$-th forward difference $\Delta_h^n f$ is the discrete analogue of the $n$-th derivative.
They detect polynomial behaviour, appear in Newton's interpolation formula, and express linear difference equations in operator form.

## Explanations

### L1 human

Take a list of numbers, write down the gaps between neighbours, then the gaps between those gaps, and so on.
Each new row is a difference of higher order.
For the cubes $0, 1, 8, 27, 64, 125$ the rows are $1, 7, 19, 37, 61$, then $6, 12, 18, 24$, then $6, 6, 6$.
The third row is constant, which reflects that $x^3$ has degree $3$.
