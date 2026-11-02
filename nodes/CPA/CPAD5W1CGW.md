---
tag: CPAD5W1CGW
kind: concept
name: Invertible operator
msc: [47A05]
specializes: [0ZNZH0EXFX]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_element
---

## Summary

A bounded operator between normed spaces is invertible when it has a bounded inverse.
Invertibility is the basic notion behind the spectrum: a number $\lambda$ lies in the spectrum of $T$ exactly when $T - \lambda I$ is not invertible.
In infinite dimensions, an injective operator need not be surjective, and a bijective operator needs a theorem to have a bounded inverse.

## Explanations

### L1 human

An operator is invertible when it can be undone by another bounded operator.
Think of a change of coordinates that can be reversed without blowing up small errors.
For example, the map $x \mapsto 2x$ on any normed space is invertible, with inverse $x \mapsto \tfrac12 x$.
The right shift on sequences is not invertible: it is injective but misses every sequence with a nonzero first entry.
